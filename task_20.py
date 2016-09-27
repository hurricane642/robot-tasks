#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    pass
    n=12
    m=27
    move_right(1)
    for i in range(n):
        if (i%2==0):
         for o in range(m):
             fill_cell()
             move_right(1)
        else:
         for o in range(m):
            move_left(1)
            fill_cell()
        move_down(1)
        o=0





if __name__ == '__main__':
    run_tasks()
