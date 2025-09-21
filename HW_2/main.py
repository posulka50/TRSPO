import random
import math
import time
import threading
import multiprocessing as mp
import matplotlib.pyplot as plt


def count_pi(n):
    counter = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            counter += 1
    return counter


def threading_pi(n, number_of_threads):
    start = time.time()
    points_per_thread = n // number_of_threads
    results = [0] * number_of_threads
    threads = []

    def worker(idx):
        results[idx] = count_pi(points_per_thread)

    for i in range(number_of_threads):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total = sum(results)
    pi = 4 * total / n
    end = time.time()
    return {"pi": pi, "time": end - start}


def multiprocessing_pi(n, number_of_processes):
    start = time.time()
    points_per_process = n // number_of_processes

    with mp.Pool(number_of_processes) as pool:
        results = pool.map(count_pi, [points_per_process] * number_of_processes)

    total = sum(results)
    pi = 4 * total / n
    end = time.time()
    return {"pi": pi, "time": end - start}


def plot_results(x, y1, y2):
    plt.plot(x, y1, marker="o", label="Threading")
    plt.plot(x, y2, marker="o", label="Multiprocessing")
    plt.xlabel("Number of Threads/Processes")
    plt.ylabel("Time (seconds)")
    plt.title("Monte Carlo π Estimation")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    N = 10_000_000
    counts = (1, 2, 4, 8, 16, 32, 64)

    times_thread = []
    times_process = []

    print(f"Target value: {math.pi}\n")

    for c in counts:
        t_res = threading_pi(N, c)
        p_res = multiprocessing_pi(N, c if c <= mp.cpu_count() else mp.cpu_count())

        times_thread.append(t_res["time"])
        times_process.append(p_res["time"])

        print(f"Threads {c}: pi={t_res['pi']:.6f}, time={t_res['time']:.4f} sec")
        print(f"Processes {c}: pi={p_res['pi']:.6f}, time={p_res['time']:.4f} sec\n")

    plot_results(counts, times_thread, times_process)

# Висновок:
# Використання threading не пришвидшує обчислювальні задачі через Global Interpreter Lock (GIL),
# тому час виконання залишається приблизно однаковим або навіть зростає зі збільшенням потоків.
# Натомість multiprocessing дозволяє використати кілька ядер процесора, що дає реальне прискорення
# до кількості фізичних ядер. Таким чином, для CPU-bound задач ефективно застосовувати саме multiprocessing.

