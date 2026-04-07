from threading import Thread

def task(i):
    print(f"Liczba: {i}")

threads = []
for i in range(5):
    t = Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

    