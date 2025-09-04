
---

# Multithreaded TCP Chat

##  Project Overview

This project is a multithreaded chat system implemented in Python using TCP sockets.
It supports communication between a server and multiple clients, allowing both **public (broadcast) messages** and **private messages** between users.

---

##  Features

###  Server

* **Multithreading** – Handles multiple clients simultaneously.
* **Broadcast Messaging** – Sends messages to all connected clients except the sender.
* **Private Messaging** – Clients can send private messages using:

  ```bash
  /pm <username> <message>
  ```
* **Connection Management** – Keeps track of connected users, removes disconnected clients, and notifies others.
* **Graceful Shutdown** – Optionally, the server can notify all clients when shutting down.

###  Client

* **Username Login** – Prompts the user for a username when connecting.
* **Public Messaging** – Sends messages to all connected users.
* **Private Messaging** – Supports sending private messages with `/pm`.
* **Real-Time Communication** – Continuously listens for incoming messages.
* **Disconnect Command** – Type `quit` to disconnect from the server.
* **User Instructions** – Clear prompts for sending messages.

---

##  Installation & Usage

### Prerequisites

* Python 3 or higher installed.

### Setup

1. Clone or download the repository.
2. Place `server.py` and `client.py` in the same folder.

### Running the Server

```bash
python server.py
```

The server will start and listen for incoming connections.

### Running a Client

```bash
python client.py
```

You will be prompted to enter a username.

---

##  Example Run

### 1. Multiple Clients Connect

* **Sam** sends a public message:

```
Sam: Hello everyone!
```

* **On the server terminal:**

```
Message from Sam: Hello everyone!
```

### 2. Private Message (Eliya → Sam)

```
/pm Sam Hi Sam, how are you?
```

* **Displayed on Sam’s client:**

```
[Private from Eliya]: Hi Sam, how are you?
```

* **Displayed on Eliya’s client:**

```
[Private to Sam]: Hi Sam, how are you?
```

### 3. Disconnect

* **Sam** types:

```
quit
```

* Server terminal:

```
Sam has disconnected.
```

---

##  Project Files

* **server.py** – Handles client connections, broadcasting, private messaging, and connection management.
* **client.py** – Connects to the server, sends/receives messages, supports private and public chat.
* **Documentation** – Detailed explanation of system architecture, installation, and usage.

---

##  Future Improvements

* GUI interface for easier interaction.
* Encrypted messaging.
* User authentication system.

---

