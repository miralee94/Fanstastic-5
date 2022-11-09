from pytest import *
from serverhall import *
from multiconn_server import *
from multiconn_user_client import *
from multiconn_data_client import *

conf = computerConfig()
conn = connection()


def test_all_strings():
    assert conf.all_values(
    ) == f"\nCPU VALUES: [{conf.cpu}]\nPROCCESER: [{conf.proccess}]\nGRAPHICS: [{conf.graphics}]\nMOTHERBOARD: [{conf.motherboard}]\n"


def test_close_connection():
    assert conn.disconnect() == "!DISCONNECT"


def test_buf_size():
    assert conn.buf_size() == 4096


def test_sending_all_data():
    assert send_all_data_to_server(
    ) != f"\nCPU VALUES: [{conf.cpu}]\nPROCCESER: [{conf.proccess}]\nGRAPHICS: [{conf.graphics}]\nMOTHERBOARD: [{conf.motherboard}]\n"
