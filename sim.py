from basic_genes import *

if __name__ == '__main__':
    sun = suns(100)
    producers = []
    set_envir(the_sun=sun, the_producers_list=producers)
    tree(5, 12)
    tree(7, 15)
    for i in range(10):
        alga(0.05, 0.8)
        alga(0.08, 1)
    print(sun.sunlight_queue)
    while True:
        sun.shine()
        print('sum of producer', len(producers))
        print(sun.sunlight_queue)
        if input():
            break