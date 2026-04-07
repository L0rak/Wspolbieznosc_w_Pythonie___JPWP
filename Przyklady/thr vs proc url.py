import threading
import multiprocessing
import time

def io_task(name):
    time.sleep(1)

if __name__ == "__main__":
    count = 10
    print(f"{count} zadań typu I/O\n")

    start = time.time()
    for i in range(count):
        io_task(f"Zadanie-{i}")
    print(f"SEKWENCYJNIE: {time.time() - start:.3f}s")

    start = time.time()
    threads = []
    for i in range(count):
        t = threading.Thread(target=io_task, args=(f"Wątek-{i}",))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print(f"WĄTKI: {time.time() - start:.3f}s")

    start = time.time()
    processes = []
    for i in range(count):
        p = multiprocessing.Process(target=io_task, args=(f"Proces-{i}",))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    print(f"PROCESY: {time.time() - start:.3f}s")

    