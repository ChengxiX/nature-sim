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

class consumer(hetero):
    '消费者'
    pass

class decomposer(hetero):
    '分解者'
    pass

class environment():
    '环境'
    pass

class sun(environment):
    '太阳'
    pass

class land(environment):
    '土地（空间）'
    pass

class water(environment):
    '水'
    pass