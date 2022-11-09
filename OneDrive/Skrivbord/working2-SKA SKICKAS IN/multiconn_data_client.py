# import socket
from serverhall import *


def send_all_data_to_server():
    conf = computerConfig()
    return conf.all_values()


# Send data from "serverhall.py"(data sent to klient) to "multiconn_server.py"(server) (*)
def send_client_1_data(dataclient):
    data = dataclient.socket.sendall(bytes(f's{send_all_data_to_server()}', 'utf-8'))
    return data


def main():
    # Create an IP, PORT and and save them into a tuple called "ADDR"
    dataclient = connection()
    dataclient.client_connector(dataclient)  # <--- Serverhall.py (info)

    # While this runs, the menu will loop until "connected" become false.
    connected = True
    while connected:

        print(""" ## MENU ## 
        1. Send all DATA to server

        !DISCONNECT to exit""")

        msg = input("> ")

        if msg == dataclient.disconnect():
            connected = False

        #  IF Client input is "1", it will send the data from "serverhall.py" with an "s" infront to excecute a specific command in the server.
        elif msg == "1":
            send_client_1_data(dataclient)  # <---- (*)


if __name__ == "__main__":
    main()
