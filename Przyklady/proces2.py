import multiprocessing

liczba = 10

def zmien_liczbe():
    global liczba
    liczba = 50
    print(f"Nowy proces = {liczba}")

if __name__ == "__main__":
    p = multiprocessing.Process(target=zmien_liczbe)
    p.start()
    p.join()
    
    print(f"Main Proces = {liczba}")

    