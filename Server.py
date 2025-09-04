
import socket
import threading

class ChatServer:
    def __init__(self, host='127.0.0.1', port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        print("Server is now listening for incoming connections...")
        print(f"Server started on {host}:{port}")
        self.clients = {}

    def broadcast(self, sender, message):
        for client, username in self.clients.items():
            if client != sender:
                try:
                    client.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"Error broadcasting to {username}: {e}")
                    self.disconnect(client)

    def send_private_message(self, sender, recipient_username, message):
        recipient_client = None
        for client, username in self.clients.items():
            if username == recipient_username:
                recipient_client = client
                break

        if recipient_client:
            try:
                recipient_client.send(f"[Private from {self.clients[sender]}]: {message}".encode('utf-8'))
                sender.send(f"[Private to {recipient_username}]: {message}".encode('utf-8'))
            except Exception as e:
                print(f"Error sending private message to {recipient_username}: {e}")
                self.disconnect(recipient_client)
        else:
            sender.send(f"User {recipient_username} not found.".encode('utf-8'))

    def handle_client(self, client):
        try:
            username = client.recv(1024).decode('utf-8')
            self.clients[client] = username
            print(f"{username} connected.")

            while True:
                try:
                    message = client.recv(1024).decode('utf-8')
                    if not message:
                        print(f"Client {username} disconnected unexpectedly.")
                        break

                    print(f"Message from {username}: {message}")  # Debug log for received message

                    if message.startswith("/pm"):
                        parts = message.split(" ", 2)
                        if len(parts) >= 3:
                            recipient_username = parts[1]
                            private_message = parts[2]
                            self.send_private_message(client, recipient_username, private_message)
                        else:
                            client.send("Invalid private message format. Use: /pm <username> <message>".encode('utf-8'))
                    else:
                        print(f"{username}: {message}")
                        self.broadcast(client, f"{username}: {message}")
                except Exception as e:
                    print(f"Error handling message from {username}: {e}")
                    break
        except Exception as e:
            print(f"Error during client initialization: {e}")
        finally:
            self.disconnect(client)

    def disconnect(self, client):
        username = self.clients.pop(client, None)
        if username:
            print(f"{username} disconnected.")
            self.broadcast(client, f"{username} has left the chat.")
        try:
            client.close()
        except Exception as e:
            print(f"Error closing client connection: {e}")

    def run(self):
        while True:
            try:
                client, address = self.server.accept()
                print(f"New connection from {address}")
                threading.Thread(target=self.handle_client, args=(client,)).start()
            except Exception as e:
                print(f"Error accepting new connection: {e}")

if __name__ == "__main__":
    server = ChatServer()
    server.run()

