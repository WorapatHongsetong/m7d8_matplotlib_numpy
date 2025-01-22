import matplotlib.pyplot as plt
import drawlines_np as dnp
import drawlines_o as do
import random

N = 5000

print(f"Creating sample data...")
sample_data = []
for _ in range(N):
    line = []
    for __ in range(4):
        line.append(random.uniform(0, 1000))
    line = list(line)
    sample_data.append(line)
print(f"Sample data created, total: {N} lines.")



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# Set global axis limits
plt.xlim(0, 1000)  # x-axis from 0 to 5
plt.ylim(0, 1000) # y-axis from 0 to 10


for line in sample_data:
    x1, y1, x2, y2 = line
    ax1.plot([x1, x2], [y1, y2], marker='o')

ax1.set_title("Graph 1: Unfiltered")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()


filtered_data = dnp.rectangular_filter(sample_data, x1=100, y1=100, x2=400, y2=400)

for line in filtered_data:
    x1, y1, x2, y2 = line
    ax2.plot([x1, x2], [y1, y2], marker='o')

ax2.set_title("Graph 2: Filtered")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.legend()


plt.tight_layout()
plt.show()