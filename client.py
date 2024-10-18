#client side code

import socket
import threading
import sys

# Function to receive data from the server
def receive_data(client_socket):
    try:
        while True:
            # Receive the mouse position from the server
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(data.strip())
    except Exception as e:
        print(f"Error receiving data: {e}")

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Start a thread to receive data from the server
receive_thread = threading.Thread(target=receive_data, args=(client_socket,))
receive_thread.start()

# Main thread for user input
try:
    while True:
        # Check if Enter key is pressed to exit
        if input("Press Enter to quit...") == "":
            print("Client stopped.")
            break
except KeyboardInterrupt:
    print("Client stopped.")
finally:
    client_socket.close()
    receive_thread.join()
