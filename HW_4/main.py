import concurrent.futures
import time
import matplotlib.pyplot as plt

def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

def run_with_list(n: int, processes: int):
    numbers = range(1, n + 1)
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=processes) as executor:
        results = list(executor.map(collatz_steps, numbers, chunksize=10_000))
    return time.time() - start, sum(results) / len(results)

def run_streaming(n: int, processes: int):
    numbers = range(1, n + 1)
    start = time.time()
    total_steps, count = 0, 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=processes) as executor:
        for value in executor.map(collatz_steps, numbers, chunksize=10_000):
            total_steps += value
            count += 1
    return time.time() - start, total_steps / count

def main():
    n = 1_000_00
    process_counts = [1, 2, 4, 8]

    list_times = []
    stream_times = []

    for p in process_counts:
        elapsed_list, avg_list = run_with_list(n, p)
        elapsed_stream, avg_stream = run_streaming(n, p)
        list_times.append(elapsed_list)
        stream_times.append(elapsed_stream)
        print(f"\nПроцесів: {p}")
        print(f"  Список           : {elapsed_list:.2f} c (avg = {avg_list:.2f})")
        print(f"  Без синхронізації: {elapsed_stream:.2f} c (avg = {avg_stream:.2f})")

    plt.figure(figsize=(10, 6))
    plt.plot(process_counts, list_times, marker='o', label='Список')
    plt.plot(process_counts, stream_times, marker='o', label='Без синхронізації')
    plt.xlabel('Кількість процесів')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння швидкодії')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
