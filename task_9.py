#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    pass
    while(wall_is_on_the_right()==False):
        if (wall_is_above()==False)or(wall_is_beneath()==False):
            fill_cell()
        move_right(1)
    if (wall_is_above()==False)or(wall_is_beneath()==False):
            fill_cell()
if __name__ == '__main__':
    run_tasks()
