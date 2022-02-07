print('счетчик')
import time
elapsed = 0
while elapsed < 10:
    time.sleep(1)
    elapsed +=1
    print(f'\r{elapsed}', end='')