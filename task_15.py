#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    pass
    if wall_is_above():
        if wall_is_on_the_left():
            while not wall_is_on_the_right():
                move_down(1)
                move_right(1)
        else:
            while not wall_is_on_the_left():
                move_down(1)
                move_left(1)
    elif wall_is_on_the_left():
        while not wall_is_on_the_right():
                move_up(1)
                move_right(1)
    else:
        while not wall_is_on_the_left():
                move_up(1)
                move_left(1)


if __name__ == '__main__':
    run_tasks()
