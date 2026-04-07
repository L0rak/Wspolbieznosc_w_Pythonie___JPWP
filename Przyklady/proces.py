import os
import multiprocessing
import time

def demo_process():
    print(f"Proces PID: {os.getpid()}")
    time.sleep(2)

if __name__ == "__main__":
    print(f"Main Process PID: {os.getpid()}")
    
    p = multiprocessing.Process(target=demo_process)
    p.start()
    p.join()

