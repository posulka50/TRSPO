import threading

def thread_function_1():
    for i in range(500):
        print(f"Thread_1: {i}\n")

def thread_function_2():
    for i in range(500):
        print(f"Thread_2: {i}\n")

if __name__ == "__main__":
    thread1 = threading.Thread(target=thread_function_1)
    thread2 = threading.Thread(target=thread_function_2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Both threads have finished execution.")

    