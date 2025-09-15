import random
import math
import time
import threading
import matplotlib.pyplot as plt

def count_pi(n, results, index):
    counter = 0

    for _ in range(n):
        x = random.uniform(a=-1, b=1)
        y = random.uniform(a=-1, b=1)
        if x**2 + y**2 <= 1:
            counter += 1
    results[index] = counter

def tread_function(n, number_of_threads):
    time_start = time.time()
    point_for_thread = n // number_of_threads
    threads = []
    results = [0] * number_of_threads

    for _ in range(number_of_threads):
        thread = threading.Thread(target=count_pi, args=(point_for_thread, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total = sum(results)
    pi = 4 * total / n

    time_end = time.time()

    time_result = time_end - time_start

    return {'pi': pi, 'time': time_result}

def plotting(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Number of Threads')
    plt.ylabel('Time (seconds)')
    plt.xticks(x)
    plt.yticks(y)
    plt.title('Time vs Number of Threads for Pi Calculation')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    treads = (2, 4, 8, 16, 32, 64)
    times = []

    print(f'Target value: {math.pi}\n')

    for i in treads:
        result = tread_function(1_000_000_0, i)
        times.append(result['time'])
        print(f'Number of threads: {i} -> {result["pi"]} Time: {result["time"]} sec')

    plotting(treads, times)

