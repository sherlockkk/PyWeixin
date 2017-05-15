import socket
from tcp import tcpclient
import json
import threading


class TCPServer():
    def __init__(self):
        HOST = ''
        POST = 9997
        self.BUFSIZ = 8192
        ADDR = (HOST, POST)

        self.tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpServerSocket.bind(ADDR)
        self.tcpServerSocket.listen(5)
        self.tcpClientSocket, self.clientaddr = self.tcpServerSocket.accept()

    def read(self):
        try:
            data_str = ""
            while True:
                data_str += self.tcpClientSocket.recv(self.BUFSIZ).decode()
                if '<END>' in data_str:
                    self.tcpClientSocket.send('0 "OK"<END>\r\n'.encode())
                    print(data_str)
                    self.validate_str(data_str)
                print(data_str)
                data_str = ''
        except Exception as e:
            # self.tcpServerSocket.close()
            print(e)
            # finally:
            # self.tcpServerSocket.close()

    def validate_str(self, data_str):
        if data_str[:2] is '21':
            print(data_str[3:len(data_str) - 7])


if __name__ == '__main__':
    tcp_server = TCPServer()
    tcp_server.read()
    
