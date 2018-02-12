from socket import socket, AF_INET, SOCK_STREAM

# Choose a mail server and call it mailserver
mailserver = ("esva.mail-relay.ubc.ca", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != "220":
    print("220 reply not received from server.")

# Send HELO command and print server response.
heloCommand = "HELO Kevin\r\n"
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print("250 reply not received from server.")
 
# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <i2y9a@ece.ubc.ca>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("MAIL FROM response: " + recv2)

# Send RCPT TO command and print server response.
mailFrom = "RCPT TO: <i2y9a@ece.ubc.ca>\r\n"
clientSocket.send(mailFrom.encode())
recv3 = clientSocket.recv(1024).decode()
print("RCPT TO response: " + recv3)

# Send DATA command and print server response.
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print("DATA response: " + recv4)

# Send message data.
subject = "Subject: [ELEC331] Kevin Qiu's Assignment 2 Email\r\n"
sender = "From: Kevin Qiu\r\n\r\n"
msg1 = "Name: Kevin Qiu \r\n"
msg2 = "Student #: 14188149 \r\n\r\n"
msg3 = "Hello ELEC 331 world!\r\n"
endmsg = ".\r\n"
clientSocket.send(subject.encode())
clientSocket.send(sender.encode())
clientSocket.send(msg1.encode())
clientSocket.send(msg2.encode())
clientSocket.send(msg3.encode())
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print("Message response: " + recv5)

# Send QUIT command and get server response.
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print("QUIT response: " + recv6)

clientSocket.close()