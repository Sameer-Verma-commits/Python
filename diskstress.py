# disk_stress.py
with open("bigfile.tmp", "wb") as f:
    for _ in range(2000):
        f.write(b"0" * 5_000_000)   # ~5MB each loop
