import threading

from multi_async_parallel.multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    # print(add_ints('../data/1Kints.txt'))

    # print('started main')
    #
    # ints = read_ints('../data/1Kints.txt')
    #
    # t1 = threading.Thread(target=count_three_sum, args=(ints,))
    # t1.start()
    #
    # print('What are we waiting for?')
    # print('Ended main')

    print('started main')

    ints = read_ints('../data/1Kints.txt')

    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
    t1.start()

    print(input("Whats your name?"))

    print('What are we waiting for?')
    print('Ended main')
