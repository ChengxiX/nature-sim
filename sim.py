from basic_genes import *

import matplotlib.pyplot as plt

if __name__ == '__main__':
    mainen = container()
    tree(5, 12, mainen)
    tree(7, 15, mainen)
    for i in range(10):
        alga(0.05, 0.8, mainen)
        alga(0.08, 1, mainen)
    sums_of_trees = []
    sums_of_alags = []
    for t in range(100):
        sum_of_alags = 0
        sum_of_trees = 0
        #print(mainen.producer_list)
        for i in mainen.producer_list:
            mainen.sun.shine()
            if isinstance(i, alga):
                sum_of_alags += 1
            elif isinstance(i, tree):
                sum_of_trees += 1
        sums_of_alags.append(sum_of_alags)
        sums_of_trees.append(sum_of_trees)
        print('=')
    plt.plot(sums_of_trees, marker='.', color='b')
    plt.plot(sums_of_alags, marker='.', color='r')
    plt.show()