import threading
import time
def print_hello():
    for _ in range(5):
        print("Hello")
        time.sleep(0.5)
def print_hi():
    for _ in range(5):
        print("Hi")
        time.sleep(0.5)
thread_hello = threading.Thread(target=print_hello)
thread_hi = threading.Thread(target=print_hi)
thread_hello.start()
thread_hi.start()
thread_hello.join()
thread_hi.join()
