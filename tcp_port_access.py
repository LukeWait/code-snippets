# Script to retrieve information from an open TCP port (HTTP)
import socket

# Target host and port to retrieve information from
target_host = "10.0.0.138"
target_port = 80

# Create a socket object and connect to the target host and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

# Send a HTTP request
client.send(b"GET /0.1/gui/ HTTP/1.1\r\nHost: 10.0.0.138\r\n\r\n")

# Receive and print the response
response = client.recv(4096)
print(response.decode("utf-8"))

# Close the connection
client.close()