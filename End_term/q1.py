import socket
import threading

# Client configuration
SERVER_IP = 'YOUR_SERVER_IP'  # Replace with the server's IP
SERVER_PORT = 5000

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_messages():
    while True:
        data, _ = client_socket.recvfrom(1024)
        print(f"Received from server: {data.decode()}")

# Start a separate thread for receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop for sending messages
while True:
    message = input("Enter message (type 'exit' to quit): ")
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    if message.lower() == 'exit':
        break