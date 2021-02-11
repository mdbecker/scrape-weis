from time import time, sleep
import sys

times = [0, 15, 30, 45]
x = int(sys.argv[1])
start = time()
next_t = min((abs(a-x), a) for a in times)
if next_t[0] < 3:
    exit(0)
sleep_t = min((abs(a-x), a) for a in times if a-x >=0)[1]
sleep_to = start + (60.0*(sleep_t-x))
while time() < sleep_to:
    sleep_for = (sleep_to - time())/2.0
    print(sleep_for)
    sleep(max(sleep_for, 1))
