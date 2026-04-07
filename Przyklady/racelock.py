import threading
import time

x = 10
lock = threading.Lock()

def increment_good():
    global x
    with lock:
        current = x
        print(f"Wątek z Lockiem odczytał: {current}")
        time.sleep(0.1)
        x = current + 1
        print(f"Wątek z Lockiem zapisał: {x}")

t1 = threading.Thread(target=increment_good)
t2 = threading.Thread(target=increment_good)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Końcowy wynik: {x}")
