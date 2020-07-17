import random

class creature():
    '生物'
    pass

class auto(creature):
    '自养生物'
    pass

class hetero(creature):
    '异养生物'
    pass

class producer(auto):
    '生产者'
    def __init__(self, sun, plants_list, cost, height, vary_magnifi=1, efficiency_magnifi=10):
        self.plants_list = plants_list
        self.cost = cost
        self.height = height
        self.sun = sun
        self.sun.sunlight_queue.append({'height': self.height, 'cost': self.cost, 'self': self})
        self.vary_magnifi = vary_magnifi
        self.plants_list.append(self)
        if efficiency_magnifi * cost < height:
            self.die()
    def ingestion(self, res):
        '摄食，被动过程，被太阳调用'
        if not res:
            self.die()
        else:
            self.reproduce()
    def copy(self, cost, height):
        producer(self.sun, self.plants_list, cost, height)
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
        self.copy(self.cost + height_changes, self.height + cost_changes)
    def die(self):
        #此处可以有被分解
        self.plants_list.remove(self)
        self.sun.sunlight_queue.remove({'height': self.height, 'cost': self.cost, 'self': self})
        del self

class consumer(hetero):
    '消费者'
    pass

class decomposer(hetero):
    '分解者'
    pass



class environment():
    '环境'
    pass

class suns(environment):
    '太阳'
    def __init__(self, sunlight):
        self.sunlight = sunlight
        self.sunlight_queue = []
    def shine(self):
        sunlight_avail = self.sunlight
        self.sunlight_queue = sorted(self.sunlight_queue, key=lambda x: x['height'], reverse=True)
        for i in self.sunlight_queue:
            if sunlight_avail > 0:
                i['self'].ingestion(res=True)
                sunlight_avail -= i['cost']
            else:
                i['self'].ingestion(res=False)

    pass

class land(environment):
    '土地（空间）'
    pass

class water(environment):
    '水'
    pass