# Współbieżność w Pythonie

Repozytorium zawiera zadania praktyczne z zakresu programowania współbieżnego i równoległego w języku Python.

## Struktura zadań

* **Zadanie 1:** Różnice w dostępie do pamięci współdzielonej (zmiennych globalnych) pomiędzy wątkami (`threading`) a procesami (`multiprocessing`).
* **Zadanie 2:** Omijanie blokady GIL (Global Interpreter Lock) w zadaniach obliczeniowych (CPU-bound) przy użyciu `ProcessPoolExecutor`.
* **Zadanie 3:** Zarządzanie blokadami (`threading.Lock`) i zapobieganie zakleszczeniom (deadlock) poprzez wymuszenie stałej kolejności blokowania zasobów.
* **Zadanie 4:** Optymalizacja wykonania poprzez dobór mechanizmu: wątki dla zadań I/O (I/O-bound) oraz procesy dla zadań obliczeniowych (CPU-bound).
* **Zadanie 5:** Implementacja wieloetapowego potoku danych. Wymaga połączenia operacji I/O, przetwarzania wieloprocesowego (CPU) oraz eliminacji wyścigów (Race Condition) przy aktualizacji współdzielonego licznika.

## Katalog `Przykłady`

Katalog `Przykłady` zawiera gotowe demonstracje i referencyjne fragmenty kodu, które wprowadzają w mechanizmy używane w zadaniach.
