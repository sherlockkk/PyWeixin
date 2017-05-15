import itchat
import itchat.content as content
import re
from tcp import tcpclient
import json
import datetime
import tcp.MyBaseTCPServer as tcpserver
import threading
import message_queue
from socketserver import TCPServer, BaseRequestHandler
import message

global msg_queue


def get_timestamp():
    isoformat = datetime.datetime.now().isoformat()
    return isoformat


'''
监听收到的消息
'''


@itchat.msg_register([content.TEXT, content.PICTURE], isFriendChat=True, isGroupChat=True, isMpChat=False)
def text_reply(msg):
    print(msg)
    print('******************************')

    '''
    msg为收到的消息的列表，如果列表中存在‘ActualNickName’的键，即为群消息，否则为私聊消息
    '''
    if 'ActualNickName' not in msg:
        if msg.type is content.TEXT:
            msg_content = {'Content': msg['Content'], 'Time': get_timestamp(),
                           'GroupName': '',
                           'Source': msg['User']['NickName']}

            json_str = struct_json(msg_content)
            print(json_str)
            # msg_queue.put_message('10 ' + json_str)
            # return send_tcp(msg_queue.get_message())
            return send_tcp('10 ' + json_str)

        elif msg.type is content.PICTURE:
            text = msg['Content']
            re_match = re.findall('[a-zA-z]+://[^\s]*', text)
            cdnurl = re_match[0][0:len(re_match[0]) - 1]
            url_content = {'Content': cdnurl, 'Time': get_timestamp(),
                           'GroupName': '',
                           'Source': msg['User']['NickName']}
            json_url = struct_json(url_content)
            print(json_url)
            # msg_queue.put_message('11 ' + json_url)
            # return send_tcp(msg_queue.get_message())
            return send_tcp('11 ' + json_url)
    else:
        if msg.type is content.TEXT:
            msg_content = {'Content': msg['Content'], 'Time': get_timestamp(),
                           'GroupName': msg['User']['NickName'],
                           'Source': msg['ActualNickName']}
            json_str = struct_json(msg_content)
            # msg_queue.put_message('10 ' + json_str)
            print(json_str)
            # return send_tcp(msg_queue.get_message())
            return send_tcp('10 ' + json_str)
        elif msg.type is content.PICTURE:
            text = msg['Content']
            re_match = re.findall('[a-zA-z]+://[^\s]*', text)
            if re_match is None:
                return
            cdnurl = re_match[0][0:len(re_match[0]) - 1]
            url_content = {'Content': cdnurl, 'Time': get_timestamp(),
                           'GroupName': msg['User']['NickName'],
                           'Source': msg['ActualNickName']}
            json_url = struct_json(url_content)
            # msg_queue.put_message('11 ' + json_url)
            print(json_url)
            # return send_tcp(msg_queue.get_message())
            return send_tcp('11 ' + json_url)


def parser_json(json):
    '''
    解析json对象
    :param json: 
    :return: 
    '''
    content = json.loads(json)
    return content


def struct_json(dict):
    '''
    构造json对象
    :param dict: 
    :return: 
    '''
    json_load = json.dumps(dict, ensure_ascii=False)
    return json_load


def send_tcp(content):
    tcp = tcpclient.TcpClient()
    tcp.send_data(content)
    print('***************')


def tcp_server():
    host = ""  # 主机名，可以是ip,像localhost的主机名,或""
    port = 9997  # 端口
    addr = (host, port)
    # 购置TCPServer对象，
    server = TCPServer(addr, tcpserver.MyBaseRequestHandlerr)
    # 启动服务监听
    server.serve_forever()


def itchat_run():
    itchat.auto_login()
    itchat.run()


def hand():
    tcp = tcpclient.TcpClient()
    tcp.send_data('1 "Web"<END>\r\n')
    data = tcp.receive_data()
    if ('<END>' in data and data[3:5] == 'OK'):
        pass
    else:
        print("跟服务器握手失败，请重试")


if __name__ == '__main__':
    threading.Thread(target=tcp_server).start()  # 开启服务端线程
    threading.Thread(target=itchat_run).start()  # 开启微信登录线程
    hand()
