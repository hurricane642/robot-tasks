#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    pass
    while not cell_is_filled():
         move_up(1)
    move_right(1)
    if not cell_is_filled():
        move_left(2)


if __name__ == '__main__':
    run_tasks()
