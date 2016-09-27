#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    pass
    move_right(1)
    m=13
    n=1
    for i in range(m):
        move_down(1)
        if i%2==0:
         for o in range(n):
            fill_cell()
            move_right(1)
         



if __name__ == '__main__':
    run_tasks()
