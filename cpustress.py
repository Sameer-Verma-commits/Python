# cpu_stress.py
import multiprocessing
import time

def burn():
    while True:
        # ram_stress.py
        a = []
        try:
            a.append("X" * 10_000_000)   # ~10MB each loop
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    for _ in range(multiprocessing.cpu_count()):
        multiprocessing.Process(target=burn).start()
