# -*- coding:utf-8 -*-

from socketserver import TCPServer, BaseRequestHandler
import traceback
import json
import message


class MyBaseRequestHandlerr(BaseRequestHandler):
    '''TCP服务端，不以TCPServer命名是因为Python有个名为tcpserver的模块，防止冲突'''

    def handle(self):
        # 循环监听（读取）来自客户端的数据
        data_str = ''
        while True:
            # 当客户端主动断开连接时，self.recv(1024)会抛出异常
            try:
                # 一次读取1024字节
                data = self.request.recv(1024)
                data_str += data.decode()
                # self.client_address是客户端的连接(host, port)的元组
                print("receive from (%r):%r" % (self.client_address, data_str))
                if '<END>' in data_str:
                    self.validate_str(data_str)
                    self.request.sendall('0 "OK"<END>\r\n'.encode())
                    break
            except:
                traceback.print_exc()
                break

    def validate_str(self, data_str):
        '''验证收到的消息所包含的信息'''
        print(data_str[:2])
        if data_str[:2] == '21':
            str_json = data_str[3:len(data_str) - 7]
            dump = json.loads(str_json)
            if dump['SendMsgType'] == 0:
                nick_name = dump['IMNickName']
                content = dump['Content']
                m = message.Message()
                m.send_message(content, nick_name)
            elif dump['SendMsgType'] == 1:
                group_name = dump['GroupName']
                content = dump['Content']
                m = message.Message()
                m.send_chatroom_mseeage(content, group_name)

        elif data_str[:2] == '22':
            str_json = data_str[3:len(data_str) - 7]
            dump = json.loads(str_json)
            gname = dump['GroupName']
            m = message.Message()
            m.obtain_chatroom_member(gname)
