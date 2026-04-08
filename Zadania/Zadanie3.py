import threading
import time

class Konto:
    def __init__(self, nazwa, saldo):
        self.nazwa = nazwa
        self.saldo = saldo
        self.blokada = threading.Lock()

def przelew(konto_z, konto_do, kwota):

    # 1. Ustal stałą kolejność wczytywania kont,
    # możesz użyć funkcji z lambdą:
    # konto_pierwsze, konto_drugie = sorted([z czego bierzesz], key=lambda x: x.nazwa)
        
    print(f"[{threading.current_thread().name}] Próba blokady 1: {konto_pierwsze.nazwa}")
    
    # 2. Uzupełnij poniższy kod
    # Załóż blokadę na 'konto_pierwsze', a wewnątrz niej załóż blokadę na 'konto_drugie'
    
    # with ... :
        print(f"[{threading.current_thread().name}] Zablokowano: {konto_pierwsze.nazwa}.")
        # symulacja opóźnienia
        time.sleep(0.1)
        
        print(f"[{threading.current_thread().name}] Próba blokady 2: {konto_drugie.nazwa}")
        # with ... :
            print(f"[{threading.current_thread().name}] Zablokowano: {konto_drugie.nazwa}. Zmiana salda.")
            
            # Właściwa operacja na saldach
            konto_z.saldo -= kwota
            konto_do.saldo += kwota
            print(f"[{threading.current_thread().name}] Przelew z {konto_z.nazwa} do {konto_do.nazwa} zakończony!")

konto_marcina = Konto("Marcin", 1000)
konto_adama = Konto("Adam", 1000)

t1 = threading.Thread(target=przelew, args=(konto_marcina, konto_adama, 100), name="Wątek 1")
t2 = threading.Thread(target=przelew, args=(konto_adama, konto_marcina, 200), name="Wątek 2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Wszystkie operacje zakończone pomyślnie!")
# Sprawdzenie, czy matematyka się zgadza (Marcin powinien mieć 1100, Adam 900)
print(f"Saldo końcowe Marcina: {konto_marcina.saldo}")
print(f"Saldo końcowe Adama: {konto_adama.saldo}")
