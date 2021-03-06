import random
import zmq

import matplotlib.pyplot as plt

import abc

class creature():
    '生物'

    @abc.abstractmethod
    def reproduce(self):
        '''抽象方法'''
        pass

    @abc.abstractmethod
    def die(self):
        '''抽象方法'''
        pass
    pass

class auto(creature):
    '自养生物'
    pass

class hetero(creature):
    '异养生物'
    pass

class producer(auto):
    '生产者'
    def __init__(self, cost, height, vary_magnifi, efficiency_magnifi, max_height, container):
        self.container = container
        self.container.producer_list.append(self)
        self.cost = cost
        self.height = height
        self.container.sunlight_queue.append({'height': self.height, 'cost': self.cost, 'self': self})
        self.vary_magnifi = vary_magnifi
        if efficiency_magnifi * self.cost < self.height:
            self.die()
        if height > max_height:
            self.die()

    def die(self):
        # 此处可以有被分解
        try:
            self.container.producer_list.remove(self)
        except ValueError:
            pass
        try:
            self.container.sunlight_queue.remove({'height': self.height, 'cost': self.cost, 'self': self})
        except ValueError:
            pass
        del self

    def ingestion(self, res):
        '摄食，被动过程，被太阳调用'
        if not res:
            self.die()
        else:
            self.reproduce()



class tree(producer):
    '''Perennial Plant 多年生植物'''
    def __init__(self, cost, height, container,vary_magnifi=1, efficiency_magnifi=10, max_height=20):
        super(tree, self).__init__(cost, height, vary_magnifi, efficiency_magnifi, max_height, container)

    def reproduce(self):
        posi = random.randrange(2)
        if posi == 0:
            height_changes = random.random() * self.vary_magnifi
        else:
            height_changes = - random.random() * self.vary_magnifi
        posi = random.randrange(2)
        if posi == 0:
            cost_changes = random.random() * self.vary_magnifi
        else:
            cost_changes = - random.random() * self.vary_magnifi
        tree(self.cost + height_changes, self.height + cost_changes, self.container)

class alga(producer):
    '''Annual Plant 一年生植物'''

    def __init__(self, cost, height, container, repro_times=4, vary_magnifi=0.01, efficiency_magnifi=50, max_height=2):
        self.repro_times = repro_times
        super(alga, self).__init__(cost, height, vary_magnifi, efficiency_magnifi, max_height, container)

    def reproduce(self):
        for i in range(self.repro_times):
            posi = random.randrange(2)
            if posi == 0:
                height_changes = random.random() * self.vary_magnifi
            else:
                height_changes = - random.random() * self.vary_magnifi
            posi = random.randrange(2)
            if posi == 0:
                cost_changes = random.random() * self.vary_magnifi
            else:
                cost_changes = - random.random() * self.vary_magnifi
            if random.randint(0, 1//self.vary_magnifi):
                repro_times_changes = random.choice([1, -1])
            else:
                repro_times_changes = 0
            alga(self.cost + height_changes, self.height + cost_changes, self.container, repro_times=self.repro_times + repro_times_changes)

        self.die()

class consumer(hetero):
    '消费者'
    pass

class animal(consumer):
    '动物'
    def ingestion(self):
        pass
    def die(self):
        pass

class decomposer(hetero):
    '分解者'
    pass


class container():
    def __init__(self, topicfilter='1'):
        self.producer_list = []
        self.sun = suns(self)
        self.sunlight_queue = []

        # 初始化zmq
        self.port = "5556"

        # Socket to talk to server
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("tcp://localhost:%s" % self.port)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

    def listen(self):
        sums_of_trees = []
        sums_of_alags = []
        while True:
            #print('listening')
            string = self.socket.recv()
            topic, num, name = string.split()
            num = int(num)
            #print(num)
            if num > 0:
                sum_of_alags = 0
                sum_of_trees = 0
                self.sun.shine(num)
                for i in self.producer_list:
                    if isinstance(i, alga):
                        sum_of_alags += 1
                    elif isinstance(i, tree):
                        sum_of_trees += 1
                sums_of_alags.append(sum_of_alags)
                sums_of_trees.append(sum_of_trees)
            elif num == -1:
                break
        plt.plot(sums_of_trees, marker='.', color='b')
        plt.plot(sums_of_alags, marker='.', color='r')
        plt.show()



class environment():
    '环境'
    def __init__(self, container):
        self.container = container

class suns(environment):
    '太阳'
    def __init__(self, container):
        super(suns, self).__init__(container)

    def shine(self, sunlight):
        self.sunlight_avail = sunlight
        self.sunlight_queue = sorted(self.container.sunlight_queue, key=lambda x: x['height'], reverse=True)
        for i in self.sunlight_queue:
            if self.sunlight_avail - i['cost'] > 0:
                i['self'].ingestion(res=True)
                self.sunlight_avail -= i['cost']
            else:
                i['self'].ingestion(res=False)

class land(environment):
    '土地（空间）'
    pass

class water(environment):
    '水'
    pass