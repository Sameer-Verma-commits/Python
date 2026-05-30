import time
t = int(input("Enter Time in Seconds: "))
# Countdown loop
while t > 0:
    h = t // 3600
    m = (t % 3600) // 60
    sec = t % 60
    countdown=f"{h:02d}:{m:02d}:{sec:02d}"
    print(countdown)
    t-=1
    time.sleep(1)
print("\nTIME OVER")
