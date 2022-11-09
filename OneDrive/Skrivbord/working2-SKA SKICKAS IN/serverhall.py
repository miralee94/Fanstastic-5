from random import randint
import socket


class computerConfig:

    def __init__(self):
        self.cpu = randint(1, 10)
        self.proccess = randint(1, 10)
        self.graphics = randint(1, 10)
        self.motherboard = randint(1, 10)

    def all_values(self) -> str:
        return f"\nCPU VALUES: [{self.cpu}]\nPROCCESER: [{self.proccess}]\nGRAPHICS: [{self.graphics}]\nMOTHERBOARD: [{self.motherboard}]\n"


class connection:

    def __init__(self):
        self.socket = socket.socket()
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 50007
        self.addr = (self.ip, self.port)

        # Self-explanatory
    def disconnect(self):
        self.DISCONNECT_MSG = "!DISCONNECT"
        return self.DISCONNECT_MSG

    def buf_size(self):
        return 4096

    def client_connector(self, dataclient):  # (Used in both clients.) (socked-based)
        # Create an IP, PORT and and save them into a tuple called "ADDR"
        IP = dataclient.ip
        PORT = dataclient.port
        ADDR = dataclient.addr

        # Create a Client-socket and connect to the IP and PORT using (socketname).connect(ADDR)
        dataclient.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dataclient.socket.connect(ADDR)
        print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

        # Sends and recv data from/to server. (Used in "multiconn_user_client.py") (socket-based)
    def send_and_recv_client_2(self, clientconn):
        clientconn.socket.sendall(bytes(f'f', 'utf-8'))
        data1 = clientconn.socket.recv(clientconn.buf_size()).decode()
        if not data1:
            clientconn.close()
        print(f"fetched data from server:\n {data1[0:]}")
