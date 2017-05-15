import itchat
import tcp.tcpclient as tcp
import json


class Message():
    '''负责发送消息的类，类中的itchat模块只有在微信已经
    成功登录的状态下才能执行，否则会报出异常'''

    def send_message(self, message, nickname):
        auth = itchat.search_friends(nickName=nickname)[0]
        auth.send(message)

    def send_chatroom_mseeage(self, message, name):
        auth = itchat.search_chatrooms(name=name)[0]
        auth.send(message)

    def obtain_chatroom_member(self, name):
        auth = itchat.search_chatrooms(name=name)[0]
        memberlist = auth['MemberList']
        if len(memberlist) == 0:
            print('暂无数据')
            return
        else:
            mList = []
            for i in range(len(memberlist)):
                nick_name = memberlist[i]['NickName']
                member = {'IMNickName': nick_name}
                mList.append(member)
            listDict = {'IMNickNameList': mList, 'GroupName': name}
            json_dumps = json.dumps(listDict, ensure_ascii=False)
            print(json_dumps)
            tcp_client = tcp.TcpClient()
            tcp_client.send_data('22 ' + json_dumps)
