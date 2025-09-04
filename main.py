# Дмитренко В.О (КІ-33)

import threading

def thread_function_1():
    thread_sum = 0
    for i in range(500):
        thread_sum += i
        print(f'[Thread_1] Iter: {i} Sum: {thread_sum}\n')

def thread_function_2():
    thread_sum = 0
    for i in range(500):
        thread_sum += i
        print(f'[Thread_2] Iter: {i} Sum: {thread_sum}\n')

if __name__ == '__main__':
    thread1 = threading.Thread(target=thread_function_1)
    thread2 = threading.Thread(target=thread_function_2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Both threads have finished execution.")

