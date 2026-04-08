import threading
import time
from concurrent.futures import ProcessPoolExecutor

def krotkie_zadanie():
    wynik = 0
    for i in range(10**6):
        wynik += 1
    return wynik

if __name__ == '__main__':

    liczba_zadan = 40

    start_czas_reczny = time.time()
    watki = []

# pętla tworzy 40 fizycznych wątków (jeśli dla komputerów B9 to za trudne, zmniejsz liczba_zadan do 5000 albo 1000)
    for i in range(liczba_zadan):
        t = threading.Thread(target=krotkie_zadanie)
        watki.append(t)
        t.start()

    for t in watki:
        t.join()

    koniec_czas_reczny = time.time()
    print(f"Czas wykonania (ręcznie): {koniec_czas_reczny - start_czas_reczny:.3f} s")

    # ---------------------------------------------------------
    # ZADANIE:
    # Wykonujemy zadanie obliczeniowe, więc aby ominąć blokadę GIL i zoptymalizować 
    # pracę programu, użyj klasy ProcessPoolExecutor z modułu concurrent.futures.
    # 
    # 1. Stwórz blok 'with ProcessPoolExecutor(max_workers=4) as executor:' 
    # 2. Wewnątrz bloku użyj pętli oraz metody executor.submit(), 
    #    aby przekazać funkcję 'krotkie_zadanie' do wykonania liczba_zadan razy.
    # ---------------------------------------------------------

    start_czas_pula = time.time()

    # UZUPEŁNIJ KOD TUTAJ:

    # with ...
    #     for i in range(...):
    #         ...


    koniec_czas_pula = time.time()
    print(f"Czas wykonania (Pula Procesów): {koniec_czas_pula - start_czas_pula:.3f} s")