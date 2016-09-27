#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    pass
    move_right(1)
    m=13
    n=1
    for i in range(m):
        if i%2==0:
         move_down(1)
         for o in range(n):
            fill_cell()
            move_right(1)
        else:
         move_down(1)
         move_right(1)
         for o in range(n):
            move_left(1)
            fill_cell()
        n=n+1
        o=0
    move_down(1)
    move_left(13)




if __name__ == '__main__':
    run_tasks()
