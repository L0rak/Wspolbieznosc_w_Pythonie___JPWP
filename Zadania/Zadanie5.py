import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ---------------------------------------------------------
# ZADANIE:
# Symulujemy pobieranie danych z masztu
# Po pobraniu danych chcemy zdeszyfrować
# Na końcu chcemy policzyć rozmiar danych, które pobraliśmy
# Wszystko chcemy zrobić optymalnym sposobem
# ---------------------------------------------------------

# Licznik przesyłania danych w MB
suma_transferu = 0
blokada_danych = threading.Lock()

# Symulacja pobierania danych z masztu
def pobierz_logi_z_masztu(id_masztu):
    print(f"[!] Łączenie z masztem nr {id_masztu}")
    time.sleep(1.2) 
    return f"ZASZYFROWANE_DANE_MASZT_{id_masztu}_ROZMIAR_50MB"

# Symulacja deszyfrowania - operacja CPU-bound
def deszyfruj_raport(surowe_dane):
    numer_masztu = surowe_dane.split("_")[3]
    print(f"[!] Deszyfrowanie raportu z masztu {numer_masztu}")
    
    licznik_kontrolny = 0
    for i in range(10**7):
        licznik_kontrolny += i
    
    # Zwracamy numer masztu i rozmiar danych (50 MB)
    return (numer_masztu, 50)

# Aktualizacja ilości przesłanych danych
def aktualizuj_billing(rozmiar_pakietu):
    global suma_transferu
    
    aktualny_stan = suma_transferu
    time.sleep(0.01)
    suma_transferu = aktualny_stan + rozmiar_pakietu

if __name__ == "__main__":
    liczba_masztow = 20
    start_systemu = time.time()

    print(f"\n=== POBIERANIE DANYCH Z {liczba_masztow} MASZTU ===")

    surowe_pakiety = []

    # użyj metody proces/wątek.result()

    with ...PoolExecutor(max_workers=10) ...:
        ...


    print(f"\n=== DESZYFROWANIE DANYCH Z {liczba_masztow} MASZTU ===")

    przetworzone_wyniki = []
    
    with ...PoolExecutor(max_workers=10) ...:
        ...

    print(f"\n=== AKTUALIZACJA ROZMIARU POBRANYCH DANYCH ===")
    with ...PoolExecutor(max_workers=10) ...:
        for ... in ...:
            executor.submit(..., ...[...])

    koniec_systemu = time.time()
    print("\n" + "="*40)
    print(f"RAPORT KOŃCOWY")
    print(f"Łączny przetworzony transfer: {suma_transferu} MB")
    print(f"Czas wykonania wszystkich operacji: {koniec_systemu - start_systemu:.2f} s")
    print("="*40)
    
    if suma_transferu == 1000:
        print("STATUS: Dane spójne.")
    else:
        print(f"BŁĄD: Licznik wynosi {suma_transferu} zamiast 1000.")
        print("STATUS: Wykryto Race Condition! Napraw blokadę.")