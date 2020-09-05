from basic_genes import *

import zmq
import threading


def message(socket, data):
    topic = 1
    messagedata = data
    print('topic:%s messagedata:%s' % (topic, messagedata))
    socket.send_string('%d %d %s' % (topic, messagedata, pub_server_name))

def new_container():
    mainen = container()
    tree(5, 12, mainen)
    tree(7, 15, mainen)
    for i in range(10):
        alga(0.05, 0.8, mainen)
        alga(0.08, 1, mainen)
    mainen.listen()


if __name__ == '__main__':

    #初始化zmq
    port = '55566'
    pub_server_name = 'pub-sim_main'
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:%s' % port)

    #container多线程
    newcontainer = threading.Thread(target=new_container)
    newcontainer.start()

    #开始模拟
    for t in range(1):
        message(socket, 100)
    message(socket, -1)