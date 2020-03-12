#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    # for i in range(3):
    #     move_down()
    #     move_right()
    #     if i == 2:
    #         fill_cell()
    #
    # move_right()

    # move_right(n=2)
    # move_down(n=2)
    # fill_cell()
    # move_right(n=2)
    # move_down(n=1)
if __name__ == '__main__':
    run_tasks()
