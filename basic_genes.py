import random

def set_envir(the_sun, the_producers_list):
    global sun, producers_list
    sun = the_sun
    producers_list = the_producers_list

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
    pass

class tree(producer):
    def __init__(self, cost, height, vary_magnifi=1, efficiency_magnifi=10, max_height=20):
        self.cost = cost
        self.height = height
        sun.sunlight_queue.append({'height': self.height, 'cost': self.cost, 'self': self})
        self.vary_magnifi = vary_magnifi
        producers_list.append(self)
        if efficiency_magnifi * self.cost < self.height:
            self.die()
        if height > max_height:
            self.die()
    def ingestion(self, res):
        '摄食，被动过程，被太阳调用'
        if not res:
            self.die()
        else:
            self.reproduce()
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
        tree(self.cost + height_changes, self.height + cost_changes)
    def die(self):
        #此处可以有被分解
        try:
            producers_list.remove(self)
        except ValueError:
            pass
        try:
            sun.sunlight_queue.remove({'height': self.height, 'cost': self.cost, 'self': self})
        except ValueError:
            pass
        del self

class alga(producer):
    def __init__(self, cost, height, repro_times=4, vary_magnifi=0.01, efficiency_magnifi=50, max_height=2):
        self.repro_times = repro_times
        self.cost = cost
        self.height = height
        sun.sunlight_queue.append({'height': self.height, 'cost': self.cost, 'self': self})
        self.vary_magnifi = vary_magnifi
        producers_list.append(self)
        if efficiency_magnifi * self.cost < self.height:
            self.die()
        if height > max_height:
            self.die()
    def ingestion(self, res):
        '摄食，被动过程，被太阳调用'
        if not res:
            self.die()
        else:
            self.reproduce()
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
            alga(self.cost + height_changes, self.height + cost_changes, self.repro_times + repro_times_changes)

        self.die()
    def die(self):
        #此处可以有被分解
        try:
            producers_list.remove(self)
        except ValueError:
            pass
        try:
            sun.sunlight_queue.remove({'height': self.height, 'cost': self.cost, 'self': self})
        except ValueError:
            pass
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
        self.sunlight_avail = self.sunlight
        self.sunlight_queue = sorted(self.sunlight_queue, key=lambda x: x['height'], reverse=True)
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