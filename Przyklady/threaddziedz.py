from threading import Thread

class MyWorker(Thread):
    def __init__(self, i):
        super().__init__()
        self.i = i

    def run(self):
        print(f"Pracuje obiekt: {self.i}")

worker = MyWorker(10)
worker.start()
worker.join()

