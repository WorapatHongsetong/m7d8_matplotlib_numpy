import drawlines_numpy as dnp
import drawlines_original as do
import time, random

N = 10000000

print(f"Creating sample data...")
sample_data = []
for _ in range(N):
    line = []
    for __ in range(4):
        line.append(random.uniform(0, 1000))
    line = list(line)
    sample_data.append(line)
print(f"Sample data created, total: {N} lines.")

print(f"Starting measuring time for vanilla python.")
t1 = time.time()
do.rectangular_filter(target=sample_data, x1=100, y1=100, x2=400, y2=400)
t2 = time.time()
print(f"Finished, total time taken: {t2- t1} sec.")

print(f"Starting measuring time for numpy version.")
t1 = time.time()
dnp.rectangular_filter(target=sample_data, x1=100, y1=100, x2=400, y2=400)
t2 = time.time()
print(f"Finished, total time taken: {t2- t1} sec.")

# print(f"Starting measuring time for vanilla python.")
# t1 = time.time()
# do.tester(N)
# t2 = time.time()
# print(f"Finished, total time taken: {t2- t1} sec.")

# print(f"Starting measuring time for numpy version.")
# t1 = time.time()
# dnp.tester(N)
# t2 = time.time()
# print(f"Finished, total time taken: {t2- t1} sec.")