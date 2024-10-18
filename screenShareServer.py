from vidstream1 import StreamingServer
import threading
reciever = StreamingServer('192.168.1.8',9999)
#use q to quit

t = threading.Thread(target=reciever.start_server)
t.start()

# while input("") != 'STOP':
#     continue

# reciever.stop_server()

try:
    # Keep the main thread alive and wait for Ctrl+C to stop
    while True:
        pass  # Busy-waiting
except KeyboardInterrupt:
    print("Stopping the server...")
    reciever.stop_server()  # Ensure you implement this to stop the server