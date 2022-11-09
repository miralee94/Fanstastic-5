import socket
import threading
from serverhall import connection


# Conn list = all connections to server. Appended once in main*(line 62*)
# Observ list = Data sent from Client-1(Data-client) saved into a list.
connections = []
observation = []


# Client handler - Takes a letter sent from undependent clients, and executes it. (Socket-based)-(No tests)
def handle_client(conn, addr):
    serverconn = connection()
    try:
        print(f"[NEW CONNECTION] {addr} Connected")
        connected = True
        while connected:
            # Data received from klients.
            msg = conn.recv(4096).decode()

            # First letter in that Data (Pre-decided, to execute certain commands)
            commando = msg[0]

            # IF the message from Clients are !DISCONNECT then it will print something, and close the connection.
            if msg == serverconn.disconnect():
                print("DISCONNECTED")
                conn.close()
                connected = False  # Not sure if this is ever used.

            # IF server gets an "s" from client, append the Data sent(Removing the s with [1:]) from klient and execute code below. print from who and msg
            elif commando == "s":
                observation.append(msg[1:])
                print(f"Data recieved from Client[{addr[1]}]{msg[1:]}")

            # IF server gets an "f" from clients, append the Data sent from DataClient-1 to server(Removing the f with [1:]) and send data back to the UserClient-2.
            elif commando == "f":
                observation.append(msg[1:])
                response = "\n"
                for i in observation:
                    response += i
                conn.sendall(response[1:].encode())
                observation.clear()

    # Expect all error, so the server doesnt print unneccesary information. Clarity.
    except Exception as e:
        print(f"Error: {e}")
    conn.close()
    print(f"CLIENT: [{addr[1]}] Has Disconnected.")


# Threaded to handle multiple connections. (*)
def threaded_server(conn, addr):
    thread = threading.Thread(
        target=handle_client, args=(conn, addr), daemon=True)
    thread.start()
    connections.append(conn)  # *
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}\n")


def main():
    try:
        # Create an IP, PORT and "ADDR"(Combined in a tuple to be executed easier using "server.bind()" function. easy to forget to have tuple (()).
        serverconn = connection()
        # IP = server.ip
        # PORT = server.port
        ADDR = (serverconn.ip, serverconn.port)
        print("[STARTING] server is starting...")

        # Create a Server-socket, "bind" the information and "listen" for connection.
        serverconn.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverconn.socket.bind(ADDR)
        serverconn.socket.listen(5)
        print(f"[LISTENING] server is listening...")

        # While this is running, server will accept connections from clients.
        # Threaded to handle multiple connections.
        while True:
            conn, addr = serverconn.socket.accept()
            threaded_server(conn, addr)  # <--- (*)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
