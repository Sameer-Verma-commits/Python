# ram_stress.py
a = []
try:
    while True:
        a.append("X" * 10_000_000)   # ~10MB each loop
except KeyboardInterrupt:
    pass
