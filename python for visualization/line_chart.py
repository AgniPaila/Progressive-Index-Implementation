import matplotlib.pyplot as plt
import numpy as np

queries = [10000, 100000, 1000000, 10000000, 50000000]
crack_times = [4.52, 5.31, 8.61, 29.51, 41.01]  
sort_times = [12.82, 13.19, 15.03, 34.04, 42.82]
scan_times = [15.41, 30.09, 58.18, 113.17, 240.97]

crack_times = np.array(crack_times, dtype=np.float64)
sort_times = np.array(sort_times, dtype=np.float64)
scan_times = np.array(scan_times, dtype=np.float64)

plt.figure(figsize=(10, 6))

plt.plot(queries, crack_times, marker='o', linestyle='-', color='navy', label="Crack")
plt.plot(queries, sort_times, marker='s', linestyle='-', color='cornflowerblue', label="Sort")
plt.plot(queries, scan_times, marker='p', linestyle='-', color='lightsteelblue', label="Scan")

plt.xscale("log")
plt.xticks(queries, labels=[f"{q:,}" for q in queries])  

plt.yscale("log")  
plt.ylabel("Execution Time (ms)")
plt.xlabel("Number of Queries")

plt.title("Crack vs Sort vs Scan")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.show()

