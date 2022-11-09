# import socket
from serverhall import connection


def main():
    try:
        # Create an IP, PORT and and save them into a tuple called "ADDR"
        clientconn = connection()
        clientconn.client_connector(clientconn)  # <--- Serverhall.py(info)

        connected = True
        while connected:
            print(""" ## MENU ##
            1. fetch all DATA from server

            !DISCONNECT to exit""")

            msg = input("> ")

            if msg == clientconn.disconnect():  # <--- serverhall.py(info)
                connected = False

            elif msg == "1":
                clientconn.send_and_recv_client_2(clientconn)  # <--- serverhall.py(info)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
