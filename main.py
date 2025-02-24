import socket
import threading

class Peer:
    # List of static peers to attempt connection at startup
    STATIC_PEERS = [("10.206.4.122", 1255), ("10.206.5.228", 6555)]
    
    def __init__(self, name, port):
        self.name = name  # Peer name
        self.port = port  # Port for communication
        self.peers = {}  # Dictionary to store active peers {(ip, port): name}
        
        # Start the server thread to listen for connections
        threading.Thread(target=self.start_server, daemon=True).start()
        
        # Connect to static peers on startup
        self.connect_to_static_peers()

    def start_server(self):
        """Start the peer's server to receive messages."""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", self.port))  # Bind to all interfaces
        server_socket.listen(5)
        print(f"Server listening on port {self.port}...")

        while True:
            client_socket, addr = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket, addr), daemon=True).start()

    def handle_client(self, client_socket, addr):
        """Handle incoming messages from peers."""
        try:
            data = client_socket.recv(1024).decode()
            if data:
                sender_ip, sender_port, sender_name, message = data.split(" ", 3)
                sender_port = int(sender_port)

                if message.strip().lower() == "exit":
                    # Remove peer if it disconnects
                    if (sender_ip, sender_port) in self.peers:
                        del self.peers[(sender_ip, sender_port)]
                        print(f"[INFO] {sender_name} ({sender_ip}:{sender_port}) disconnected.")
                else:
                    # Update peer information
                    self.peers[(sender_ip, sender_port)] = sender_name
                    print(f"[{sender_name} ({sender_ip}:{sender_port})]: {message}")

                    if message.strip().lower() == "connect":
                        self.send_message(sender_ip, sender_port, "connect_ack")
                    
                    if message.strip().lower() == "connect_ack":
                        print(f"[INFO] Peer {sender_name} ({sender_ip}:{sender_port}) is now active.")
            
            client_socket.close()
        except Exception as e:
            print(f"Error handling client {addr}: {e}")

    def send_message(self, target_ip, target_port, message):
        """Send a message to a peer."""
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(3)
            client_socket.connect((target_ip, target_port))
            formatted_message = f"{socket.gethostbyname(socket.gethostname())} {self.port} {self.name} {message}"
            client_socket.sendall(formatted_message.encode())
            client_socket.close()

            if message.strip().lower() == "connect_ack":
                self.peers[(target_ip, target_port)] = self.name

            if message.strip().lower() == "exit":
                if (target_ip, target_port) in self.peers:
                    del self.peers[(target_ip, target_port)]
                    print(f"[INFO] You disconnected from {target_ip}:{target_port}.")

            return True
        except Exception:
            print(f"[ERROR] Cannot send message to {target_ip}:{target_port}.")
            return False

    def connect_to_static_peers(self):
        """Attempt to connect to predefined static peers."""
        for ip, port in self.STATIC_PEERS:
            success = self.send_message(ip, port, "connect")
            if success:
                print(f"[SUCCESS] Connected to static peer {ip}:{port}")
            else:
                print(f"[WARNING] Could not connect to {ip}:{port}.")

    def check_peer_status(self):
        """Check and remove inactive peers."""
        disconnected_peers = []
        for (ip, port) in list(self.peers.keys()):
            try:
                test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                test_socket.settimeout(2)
                test_socket.connect((ip, port))
                test_socket.close()
            except Exception:
                disconnected_peers.append((ip, port))

        for peer in disconnected_peers:
            del self.peers[peer]
            print(f"[INFO] Peer {peer[0]}:{peer[1]} removed due to inactivity.")

    def query_peers(self):
        """Display a list of active peers."""
        self.check_peer_status()
        if self.peers:
            print("\nActive Peers:")
            for (ip, port), name in self.peers.items():
                print(f"- {name} ({ip}:{port})")
        else:
            print("\nNo active peers found.")

    def connect_to_peers(self):
        """Notify all active peers of connection."""
        self.check_peer_status()
        if not self.peers:
            print("No active peers to connect to.")
            return
        for (ip, port) in self.peers.keys():
            self.send_message(ip, port, "connect")
        print("Connected to all active peers.")

    def menu(self):
        """User interface menu."""
        while True:
            print("\n***** Menu *****")
            print("1. Send message")
            print("2. Query active peers")
            print("3. Connect to active peers")
            print("0. Quit")
            choice = input("Enter choice: ")

            if choice == "1":
                target_ip = input("Enter recipient's IP address: ")
                target_port = int(input("Enter recipient's port number: "))
                message = input("Enter your message: ")
                self.send_message(target_ip, target_port, message)
            elif choice == "2":
                self.query_peers()
            elif choice == "3":
                self.connect_to_peers()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

# Initialize the peer
if __name__ == "__main__": 
    print("TEAM NAME : CRYPTOKNIGHTS ")
    name = input("Enter your name: ")
    port = int(input("Enter your port number: "))
    peer = Peer(name, port)
    peer.menu()
