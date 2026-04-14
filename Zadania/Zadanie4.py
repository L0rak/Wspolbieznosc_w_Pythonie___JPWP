import threading
import multiprocessing
import time

def zadanie_obliczeniowe(id_zadania):
    wynik = 0
    for i in range(10**7):
        wynik += 1
    return wynik

def zadanie_io(id_zadania):
    # symulacja czekania 1 sekundy na np. odpowiedź z serwera
    time.sleep(1) 

if __name__ == "__main__":
    liczba_zadan = 4
    
    # ---------------------------------------------------------
    # ZADANIE:
    # Masz do dyspozycji klasy 'threading.Thread' oraz 'multiprocessing.Process'.
    # Wykorzystaj je w pętlach poniżej, aby zrównoleglić zadania.
    # Użyj WĄTKÓW do jednego typu zadań, a PROCESÓW do drugiego.
    # Pamiętaj, żeby optymalnie dopasować narzędzie do zadania
    # ---------------------------------------------------------

    start_io = time.time()
    
    robotnicy_io = []
    for i in range(liczba_zadan):
        # Stwórz obiekt Wątku lub Procesu dla 'zadanie_io'
        # worker = ... 
        # robotnicy_io.append(worker)
        # worker.start()
        pass
        
    # Pamiętaj o pętli czekającej na zakończenie robotników (metoda join)


    koniec_io = time.time()
    print(f"Czas zadań I/O: {koniec_io - start_io:.2f} s")



    start_obliczeniowe = time.time()
    
    robotnicy_obliczeniowe = []
    for i in range(liczba_zadan):
        # Stwórz obiekt Wątku lub Procesu dla 'zadanie_obliczeniowe'
        # worker = ... 
        # robotnicy_obliczeniowe.append(worker)
        # worker.start()
        pass
        
    # Pamiętaj o pętli czekającej na zakończenie robotników (metoda join)


    koniec_obliczeniowe = time.time()
    print(f"Czas zadań CPU: {koniec_obliczeniowe - start_obliczeniowe:.2f} s")
