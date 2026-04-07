from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(print, "Zadanie 1")
    executor.submit(print, "Zadanie 2")

