import drawlines_np as dnp
import drawlines_o as do
import time

N = 10000000

print(f"Starting measuring time for vanilla python.")
t1 = time.time()
do.tester(N)
t2 = time.time()
print(f"Finished, total time taken: {t2- t1} sec.")

print(f"Starting measuring time for numpy version.")
t1 = time.time()
dnp.tester(N)
t2 = time.time()
print(f"Finished, total time taken: {t2- t1} sec.")