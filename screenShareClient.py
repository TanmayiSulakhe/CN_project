from vidstream1 import ScreenShareClient
import threading
sender = ScreenShareClient('192.168.1.8',9999)
# sender.start_stream()
t = threading.Thread(target=sender.start_stream)
t.start()

# while input("") != 'STOP':
#     continue

# sender.stop_stream()

try:
    # Keep the main thread alive and wait for Ctrl+C to stop
    while True:
        pass  # Busy-waiting
except KeyboardInterrupt:
    print("Stopping the client...")
    sender.stop_stream()  # Implement this method to stop the stream properly