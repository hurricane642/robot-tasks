#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    pass
    while(wall_is_beneath()==False):
        move_right(1)
    while(wall_is_beneath()==True):
        move_right(1)

if __name__ == '__main__':
    run_tasks()
