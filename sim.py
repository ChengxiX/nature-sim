import random
from basic_genes import *

if __name__ == '__main__':
    sun = suns(100)
    plants = []
    plants.append(producer(sun, plants, 20, 10))
    for x in range(1000):
        sun.shine()
    print(sun.sunlight_queue)