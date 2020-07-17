import random
from basic_genes import *

if __name__ == '__main__':
    sun = suns(100)
    producers = []
    producer(sun, producers, 20, 10)
    for x in range(3000):
        sun.shine()
