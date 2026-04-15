import time
from concurrent.futures import ProcessPoolExecutor

def zrob_pranie(numer_kosza):
    print(f"[Pralka] Pierze kosz nr {numer_kosza}")
    time.sleep(1) 
    return f"Czyste pranie z kosza {numer_kosza}"

if __name__ == '__main__':
    liczba_koszy = 10
    liczba_pralek = 10

    # ---------------------------------------------------------
    # SCENARIUSZ 1: PODEJŚCIE SZEREGOWE
    # ---------------------------------------------------------
    print("="*60)
    print("SCENARIUSZ 1: BŁĘDNE PODEJŚCIE (Czekanie przy pralce)")
    print("="*60)
    
    start_zly = time.time()
    wyniki_zle = []
    
    with ProcessPoolExecutor(max_workers=liczba_pralek) as executor:
        for i in range(liczba_koszy):
            przyszle_pranie = executor.submit(zrob_pranie, i)
            wyniki_zle.append(przyszle_pranie.result())
            
    koniec_zly = time.time()
    czas_zly = koniec_zly - start_zly
    print(f"\n=> CZAS CAŁKOWITY: {czas_zly:.2f} sekundy")


    # ---------------------------------------------------------
    # SCENARIUSZ 2: PODEJŚCIE RÓWNOLEGŁE
    # ---------------------------------------------------------
    print("="*60)
    print("SCENARIUSZ 2: POPRAWNE PODEJŚCIE (Dwie pętle)")
    print("="*60)
    
    start_dobry = time.time()
    wyniki_dobre = []
    
    with ProcessPoolExecutor(max_workers=liczba_pralek) as executor:
        paragony = []
        for i in range(liczba_koszy):
            przyszle_pranie = executor.submit(zrob_pranie, i)
            paragony.append(przyszle_pranie)
            
        for paragon in paragony:
            wyniki_dobre.append(paragon.result())
            
    koniec_dobry = time.time()
    czas_dobry = koniec_dobry - start_dobry
    print(f"\n=> CZAS CAŁKOWITY: {czas_dobry:.2f} sekundy")