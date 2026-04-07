import threading
import multiprocessing
import time

def cpu_task():
    count = 0
    for i in range(10**7):
        count += i
    return count

if __name__ == "__main__":
    print("Uruchamiam 2 wątki.")
    t1 = threading.Thread(target=cpu_task)
    t2 = threading.Thread(target=cpu_task)
    
    start_threads = time.time()
    t1.start(); t2.start()
    t1.join(); t2.join()
    end_threads = time.time()
    
    print("Uruchamiam 2 procesy.")
    p1 = multiprocessing.Process(target=cpu_task)
    p2 = multiprocessing.Process(target=cpu_task)
    
    start_procs = time.time()
    p1.start(); p2.start()
    p1.join(); p2.join()
    end_procs = time.time()

    print(f"\nCzas wykonania (Wątki):  {end_threads - start_threads:.2f}s")
    print(f"Czas wykonania (Procesy): {end_procs - start_procs:.2f}s")

    