#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    pass
    while wall_is_above() and not(wall_is_on_the_left()) and wall_is_beneath():
        move_left(1)
    if not wall_is_above():
            move_up(1)
    elif not wall_is_beneath():
            move_down(1)
    else:
        while  wall_is_above() and not(wall_is_on_the_right())and wall_is_beneath():
            move_right(1)
        if not wall_is_above():
               move_up(1)
        elif not wall_is_beneath():
            move_down(1)
    while not wall_is_on_the_left():
                move_left(1)
    while not wall_is_above():
                move_up(1)




if __name__ == '__main__':
    run_tasks()
