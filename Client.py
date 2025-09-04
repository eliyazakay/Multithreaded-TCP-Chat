# Client Code (client.py)
import socket
import threading

class ChatClient:
    def __init__(self, host='127.0.0.1', port=12345):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((host, port))
            self.username = input("Enter your username: ")
            self.client.send(self.username.encode('utf-8'))  
            print("Successfully connected to the server.")  # Debug log for connection success
            print("To send a private message, use the format: /pm <username> <message>")
        except Exception as e:
            print(f"Error connecting to server: {e}")
            raise

    def send_message(self, message):
        try:
            self.client.send(message.encode('utf-8'))
            print(f"Message sent: {message}")  # Debug log for sent message
        except Exception as e:
            print(f"Error sending message: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message:
                    print(f"Received message: {message}")  # Debug log for received message
                else:
                    print("Server has closed the connection.")  # Debug log for connection close
                    break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def start(self):
        threading.Thread(target=self.receive_messages, daemon=True).start()
        print(f"Welcome to the chat, {self.username}!")
        while True:
            try:
                message = input()
                if message.lower() == 'quit':
                    self.client.close()
                    print("Disconnected from the server.")  # Debug log for disconnection
                    break
                self.send_message(message)
            except Exception as e:
                print(f"Error in input loop: {e}")

if __name__ == "__main__":
    import sys

    try:
        client = ChatClient()
        client.start()
    except Exception as e:
        print(f"Failed to start client: {e}")