# CryptoKnights

<h3>Assignment :  Peer-to-Peer Chat Application </h3> 

<h3>Team Name   -   "CryptoKnights" </h3>

<h3>Team Members : </h3>
  Janapareddy Vidya Varshini  -    mc230041013 <br>
  Korubilli Vaishnavi         -    mc230041016 <br>
  Mullapudi Namaswi           -    mc230041023 <br>

 <h3> ✦ Note :  Our code handles the Bonus question also. </h3>

✦Through this code we implemented a peer-to-peer chat program in Python using sockets and threading that enables simultaneous 
sending and receiving messages, supports multiple peers, and allows users to query 
and retrieve the list of peers from which it had received messages. It also maintains a list of active peers and ensures connectivity with predefined static peers. Multiple instances of the code can be run in seperate terminal environments to form a peer to peer chat network. 

<h3>✦🚀 Features: </h3>
1.Establish a server that listens for incoming connections from peers.<br>
2.Send and receive messages between peers.<br>
3.Automatically connect to a list of static peers upon startup.<br>
4.Maintain a list of active peers and remove inactive ones.<br>
5.User-friendly menu for managing connections and messaging.<br>
6.Supports peer disconnection handling.<br>

<h3>📌 How It Works</h3>
Each peer runs a *TCP server* on a specified port to listen for incoming connections. When a new peer starts, it attempts to connect to **static peers** and maintains an updated list of active peers.  

<h3>✦ Concepts Involved: </h3> 
  1. Peer-to-Peer Networking <br>
  2. Socket Programming <br>
  3. Multithreading <br>
  4. Message Formatting and Serialization <br>
  5. Peer Discovery <br>
  6. Static Peers <br>
  7. Connection Management <br>
  8. User Interface <br>
 
<h3>✦ How to run the code : </h3> 
 1. Run the python file in the command prompt or in terminal. <br>
 2. Enter your name.(Ex:Peer1) <br>
 3. Enter your port number.<br>
 4. Once a peer is running, the following options are available: 
 <br>
 
     <table>
  <tr>
    <th>Option Description</th>
  </tr>
  <tr>
    <td>1. Send a message to a specific peer</td>
  </tr>
  <tr>
    <td>2. Display the list of active peers</td>
  </tr>
  <tr>
    <td>3. Connect to all active peers</td>
  </tr>
  <tr>
    <td>0. Exit the application</td>
  </tr>
</table>
    You can select the above options <br>
    If you select the option  1: <br>
        •Enter the recipients IP address <br>
        •Enter the recipients port number <br>
    
      



