import threading
import multiprocessing
import time

wspolna_lista = []

#funkcja dodająca id do globalnej listy wspolna_lista
def dodaj_element(id_zadania):
    print(f"Zadanie {id_zadania} działa i dodaje dane...")
    wspolna_lista.append(f"Wynik-{id_zadania}")
    time.sleep(0.1)

if __name__ == "__main__":
    print("--- TEST 1: WĄTKI ---")
    watki = []

    # Kod używa wątków. Zobacz, co się stanie z globalną listą.
    for i in range(5):
        t = threading.Thread(target=dodaj_element, args=(i,))
        watki.append(t)
        t.start()

    for t in watki:
        t.join()

    print(f"Zawartość listy po wykonaniu wątków: {wspolna_lista}")
    
    # ---------------------------------------------------------
    # ZADANIE:
    # 1. Wyczyść poniżej 'wspolna_lista', aby znów była pusta.
    # 2. Skopiuj powyższą pętlę, ale zmień obiekt z wątku, na proces
    #    (podpowiedź - nieużywany import)
    # 3. Uruchom program. Zastanów się dlaczego w drugim przypadku lista jest pusta, 
    #    skoro funkcje wykonały się poprawnie?
    # ---------------------------------------------------------

    print("\n--- TEST 2: PROCESY ---")
    
    # UZUPEŁNIJ KOD TUTAJ:
    
    
    
    print(f"Zawartość listy po wykonaniu procesów: {wspolna_lista}")