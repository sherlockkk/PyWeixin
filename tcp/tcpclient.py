import socket
import tcp.config as config


class TcpClient():
    '''TCP客户端'''

    def __init__(self):
        '''构造函数，初始化的时候构造tcp连接，返回该次连接的socket对象'''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((config.IP_ADRESS, config.PORT))
        self.soc = s

    def connect(self):
        '''重连tcp'''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((config.IP_ADRESS, config.PORT))
        return s

    def send_data(self, data):
        '''发送消息，data为str类型'''
        try:
            data = data + '<END>\r\n'
            self.soc.send(data.encode())  # 发送的数据的类型是byte数组，所以这里要用encode()，str -> bytes
        except Exception as e:
            print(e)
            self.soc.close()

    def receive_data(self):
        '''接收反馈消息，返回str类型的反馈消息'''
        while True:
            try:
                soc_recv = self.soc.recv(8192)
                return soc_recv.decode()  # 收到的是byte数组，decode() ==>>> bytes -> str
            except Exception as e:
                print(e)
                self.soc.close()

    def close_(self):
        '''关闭socket'''
        self.soc.close()
