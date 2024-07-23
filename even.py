import random
import time


def randomGen(size):
    return [random.randint(0, 100) for _ in range(size)]


def even_sum(arr):
    sum_num = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            sum_num += arr[i]
    return sum_num


arr_n = [25000, 50000, 75000, 100000]
for size in arr_n:
    initial_time = time.time()
    arr = randomGen(size)
    final_time = time.time()
    Tr = final_time - initial_time
    sum_even = even_sum(arr)
    print(sum_even)
    print(Tr)
