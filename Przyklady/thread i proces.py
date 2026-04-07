import threading
import multiprocessing
import time

def task(name):
    print(f"Zadanie {name} startuje")
    time.sleep(3)
    print(f"Zadanie {name} kończy")

if __name__ == "__main__":
    t1 = threading.Thread(target=task, args=("Wątek-1",))
    t2 = threading.Thread(target=task, args=("Wątek-2",))
    
    p1 = multiprocessing.Process(target=task, args=("Proces-1",))
    p2 = multiprocessing.Process(target=task, args=("Proces-2",))

    print("\nStart wątków")
    t1.start()
    t2.start()

    print("\nStart procesów")
    p1.start()
    p2.start()

    print("\nCzekanie")
    time.sleep(1)
    print("\nWyniki")
    t1.join()
    t2.join()
    p1.join()
    p2.join()


    