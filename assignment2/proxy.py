from socket import * 
import sys

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server') 
    sys.exit(2)
    
# Create a server socket, bind it to a port and start listening 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('',8888))
tcpSerSock.listen()
print('The server is ready to recieve')

while True:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr) 
    message = tcpCliSock.recv(1024).decode()
    print(message)
    
    # Extract the filename from the given message print(message.split()[1])
    filename = message.split()[1].partition("/")[2] 

    # Create a socket on the proxyserver
    c = socket(AF_INET,SOCK_STREAM) 
    host_resource = filename.replace("www.","",1).split('/',1)
    hostname = host_resource[0] if len(host_resource) >= 1 else ""
    resource = host_resource[1] if len(host_resource) > 1 else ""
    print("HOSTNAME: " + hostname)
    print("RESOURCE: " + resource)
    try:
        # Connect to the socket to port 80
        c.connect((hostname,80))
        print("Socket connected")
        # Create a temporary file on this socket and ask port 80 for the file requested by the client
        # fileobj = c.makefile('r', 0)
        # fileobj.write("GET "+"http://" + filename + "HTTP/1.0\n\n")
        request = "GET" + " /" + resource + "/ HTTP/1.0\r\n" + "Host: " + hostname + "\r\n\r\n"
        print(request)
        c.send(request.encode())
        print("Request Sent")

        # Read the response into buffer
        resp = c.recv(131072)
        print("Response recieved")
        print(resp.decode())
        c.close()

        # Create a new file in the cache for the requested file. 
        # Also send the response in the buffer to client socket and the corresponding file in the cache
        #tmpFile = open("./" + filename,"wb") # Fill in start. # Fill in end.

        tcpCliSock.send(resp)
    except: print("Illegal request") 


    
 # Close the client and the server sockets                 
tcpCliSock.close()
# Fill in start. 
# Fill in end.