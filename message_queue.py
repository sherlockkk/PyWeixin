import queue


class MessageQueue():
    def __init__(self):
        self.mq = queue.Queue(-1)  # -1 表示无限长队列

    def put_message(self, message):
        self.mq.put_nowait(message)

    def get_message(self):
        message = self.mq.get_nowait()
        return message


if __name__ == '__main__':
    message_queue = MessageQueue()
    for i in range(10000):
        message_queue.put_message(i)
    for i in range(10000):
        message = message_queue.get_message()
        print(message)
