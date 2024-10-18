import socket
import pyautogui
import time

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Bind to localhost and a port
server_socket.listen(1)

print("Server is listening for connections...")
client_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")

try:
    while True:
        try:
            # Get the current mouse position
            mouse_position = pyautogui.position()
            # Send the mouse position to the client
            client_socket.sendall(f"Mouse position: {mouse_position}\n".encode())
            time.sleep(1)  # Send every second
        except (ConnectionResetError, BrokenPipeError):
            print("Client disconnected. Stopping server.")
            break
except KeyboardInterrupt:
    print("Server stopped.")
finally:
    client_socket.close()
    server_socket.close()
