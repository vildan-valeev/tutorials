import random


def add_ints(path):
    with open(path, 'w') as f:
        counter = 0
        while counter <= 1000:
            f.write(str(random.randint(-999999, -99999)) + '\n')
            f.write(str(random.randint(99999, 999999)) + '\n')
            counter += 1
    return 'ok'


def read_ints(path):
    lst = []
    with open(path, 'r') as f:
        while line := f.readline():
            lst.append(int(line))
    return lst


def count_three_sum(ints, thread_name='t'):
    print(f'Started count_three_sum in {thread_name}')
    n = len(ints)
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in {thread_name}: {ints[i]}, {ints[j]}, {ints[k]}', end='\n')
    print(f'Ended count_three_sum in {thread_name}, Triplets {counter=}')