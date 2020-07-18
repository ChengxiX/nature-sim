from basic_genes import *

import matplotlib.pyplot as plt

if __name__ == '__main__':
    sun = suns(100)
    producers = []
    set_envir(the_sun=sun, the_producers_list=producers)
    tree(5, 12)
    tree(7, 15)
    for i in range(10):
        alga(0.05, 0.8)
        alga(0.08, 1)
    #print(sun.sunlight_queue)
    sums_of_trees = []
    sums_of_alags = []
    for t in range(10):
        sun.shine()
        sum_of_alags = 0
        sum_of_trees = 0
        for i in producers:
            if isinstance(i, alga):
                sum_of_alags += 1
            elif isinstance(i, tree):
                sum_of_trees += 1
        sums_of_alags.append(sum_of_alags)
        sums_of_trees.append(sum_of_trees)
    #while True:
        #sun.shine()
        #print('sum of producer', len(producers))
        #print(sun.sunlight_queue)
        #if input():
            #break
    plt.plot(sums_of_trees, marker='.')
    plt.plot(sums_of_alags, marker='.')
    plt.show()