#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    pass
    while not wall_is_above():
         move_up(1)
    if not wall_is_on_the_left():
        while not wall_is_on_the_left():
             move_left(1)
    else:
        while not wall_is_on_the_right():
             move_right(1)


if __name__ == '__main__':
    run_tasks()
