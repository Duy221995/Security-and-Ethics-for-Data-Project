# Security-and-Ethics-for-Data-Project
### Student: Nguyen Dinh Duy, ID: ICT20220203
# End-to-End Encrypted Chat Server & Client
This simple chat system consists of a server and clients that connects to each other. We implement and end-to-end encryption of the chat messages using the RSA algorithm (from the cryptography package), ensuring the privacy of the communications.

# Architecture
Server: The server is responsible for accepting new connections from clients, broadcasting messages to all connected clients, and managing client disconnections. Wehn the server starts, we generate a pair of RSA keys (public and private).

Client: Clients connect to the server and can send/receive messages. Upon connection, they receive the server's public key and use it to encrypt the messages before sending.

The client and server communicate over TCP sockets. Messages are encoded as ASCII text before being sent.


# Cryptography algorithm
The system uses RSA, a widely-used public key cryptography algorithm. The encryption/decryption process is as follows:
Key Generation (Server): When we start the server, the server generates a pair of RSA keys. The public key is sent to any client that connects.
Encryption (Client): When a client wants to send a message, we encrypt the message using the server's public key received upon connection. This encrypted message can only be decrypted using the corresponding private key.
Decryption (Server): Upon receiving an encrypted message, the server uses its private key to decrypt the message back into its original form.

Authentication: Since this is a simple chat, the user just type in whatever username they want, and they will be forwarded to the room where everyone can see their name and chat with each other

# Demo
https://github.com/https://github.com/Duy221995/Security-and-Ethics-for-Data-Project/blob/main/Demo-DuyND.mov