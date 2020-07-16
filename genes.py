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
    def __init__(self, cost, height):
        self.cost = cost
        self.height = height
        sun.sunlight_queue.append({'height': self.height, 'cost': self.cost, 'self': self})
    def ingestion(self, res):
        '摄食'
        if not res:
            self.die()
    def reproduce(self):
        #未实现创建一个名为变量的对象
        pass
    def die(self):
        #此处可以有被分解
        del self
    pass

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
    def __init__(self, sunlight=100):
        self.sunlight = sunlight
        self.sunlight_queue = []
    def shine(self):
        sunlight_avail = self.sunlight
        self.sunlight_queue = sorted(self.sunlight_queue, key=lambda x: x['height'])
        for i in self.sunlight_queue:
            i['self'].ingestion(res=True)
            sunlight_avail -= i['cost']
            if sunlight_avail <= 0:
                break
    pass

class land(environment):
    '土地（空间）'
    pass

class water(environment):
    '水'
    pass

if __name__ == '__main__':
    plants = []
    sun = suns()
