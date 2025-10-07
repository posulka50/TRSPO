import concurrent.futures
import time

# Функція для обчислення кількості кроків за гіпотезою
def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def run_with_processes(n: int, processes: int):
    numbers = range(1, n + 1)
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=processes) as executor:
        results = list(executor.map(collatz_steps, numbers, chunksize=10_000))

    avg_steps = sum(results) / len(results)
    elapsed = time.time() - start_time

    print(f"Процесів: {processes}")
    print(f"Кількість чисел: {n}")
    print(f"Середня кількість кроків: {avg_steps:.2f}")
    print(f"Час виконання: {elapsed:.2f} секунд")
    print("=" * 50)

def main():
    n = 1_000_000
    for processes in [1, 2, 4, 8, 12]:
        run_with_processes(n, processes)

if __name__ == "__main__":
    main()
