from celery import Celery, group
from time import time

app = Celery('tasks', broker='redis:///0', backend='redis:///1', task_ignore_result=False)

@app.task
def test_task(i):
    print('hi')
    return i

def main():
    x = test_task.delay(3)
    print(x.get())

if __name__ == '__main__':
    main()