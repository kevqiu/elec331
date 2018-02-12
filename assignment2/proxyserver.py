from socket import *
import sys
if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)
serverIp = sys.argv[1]

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(("", 8888))
tcpSerSock.listen()

while True:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()
    print(message)

    # Extract the filename from the given message
    filename = message.split()[1].partition("/")[2]
    print("Filename: " + filename)

    # Create a socket on the proxyserver
    c = socket(AF_INET, SOCK_STREAM)
    hostn = filename.replace("www.","",1)
    print("Hostname: " + hostn)
    url = hostn.split("/", 1)
    host = url[0] if len(url) >= 1 else ""
    resource = url[1] if len(url) > 1 else ""
    try:
        # Connect to the socket to port 80
        c.connect((host, 80))
        req = "GET /" + resource + "/ HTTP/1.0\r\nHost: " + host + "\r\n\r\n"
        print("Request: " + req)
        c.send(req.encode())

        buffer = c.recv(1000000)
        print("Buffer: " + buffer.decode())
        c.close()

        tcpCliSock.send(buffer)
    except Exception as e:
        print("Illegal request. Error: " + e)
# Close the client and the server sockets
tcpCliSock.close()