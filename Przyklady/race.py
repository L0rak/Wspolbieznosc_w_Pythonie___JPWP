import threading
import time

x = 10

def increment_bad():
    global x
    current = x
    print(f"Wątek odczytał: {current}")
    time.sleep(0.1)
    x = current + 1
    print(f"Wątek zapisał: {x}")

t1 = threading.Thread(target=increment_bad)
t2 = threading.Thread(target=increment_bad)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Końcowy wynik: {x}")

