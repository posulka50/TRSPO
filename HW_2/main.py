import random
import math
import time
import multiprocessing as mp
import matplotlib.pyplot as plt


def count_pi(n):
    counter = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            counter += 1
    return counter


def process_function(n, number_of_processes):
    time_start = time.time()
    points_per_process = n // number_of_processes

    with mp.Pool(number_of_processes) as pool:
        results = pool.map(count_pi, [points_per_process] * number_of_processes)

    total = sum(results)
    pi = 4 * total / n
    time_end = time.time()

    return {'pi': pi, 'time': time_end - time_start}


def plotting(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Number of Processes')
    plt.ylabel('Time (seconds)')
    plt.xticks(x)
    plt.title('Time vs Number of Processes for Pi Calculation')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    processes = (2, 4, 8, 16, 32)
    times = []

    print(f'Target value: {math.pi}\n')

    for p in processes:
        result = process_function(10_000_000, p)
        times.append(result['time'])
        print(f'Number of processes: {p} -> {result["pi"]} Time: {result["time"]:.4f} sec')

    plotting(processes, times)

#Multiprocessing у Python справді пришвидшує обчислювальні задачі (на відміну від threading),
# але ефективність росте лише до кількості, близької до числа фізичних ядер CPU.
# Подальше збільшення кількості процесів не тільки не дає виграшу, а й може погіршити час через витрати на управління процесами.
