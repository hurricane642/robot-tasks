#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    pass
    while(wall_is_on_the_right()==False):
        if not wall_is_above():
            move_up(1)
            fill_cell()
            move_down(1)
        if not wall_is_beneath():
            move_down(1)
            fill_cell()
            move_up(1)
        move_right(1)
    if not  wall_is_above():
            move_up(1)
            fill_cell()
            move_down(1)
    if  not wall_is_beneath():
            move_down(1)
            fill_cell()
            move_up(1)

if __name__ == '__main__':
    run_tasks()
