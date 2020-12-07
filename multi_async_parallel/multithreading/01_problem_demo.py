from multi_async_parallel.multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    # print(add_ints('../data/1Kints.txt'))

    print('started main')
    ints = read_ints('../data/1Kints.txt')
    count_three_sum(ints)

    print('What are we waiting for?')
    print('Ended main')
