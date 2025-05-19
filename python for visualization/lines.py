import matplotlib.pyplot as plt
import numpy as np

queries = [1, 10, 100, 1000, 10000, 100000]

crack_times = [0.020144, 0.05055, 0.092923, 0.136243, 0.187149, 0.439207]
ddc_times = [0.050916, 0.074435, 0.123012, 0.145247, 0.172268, 0.410842]
ddr_times = [0.033751, 0.062615, 0.113297, 0.14945, 0.201347, 0.444358]
dd1c_times = [0.049369, 0.079442, 0.127167, 0.130444, 0.171242, 0.42287]
dd1r_times = [0.030497, 0.059816, 0.100053, 0.133622, 0.180542, 0.418826]
mdd1r_times = [0.039526, 0.061116, 0.120765, 0.190531, 0.226752, 0.471741]

crack_times = np.array(crack_times, dtype=np.float64)
ddc_times = np.array(ddc_times, dtype=np.float64)
ddr_times = np.array(ddr_times, dtype=np.float64)
dd1c_times = np.array(dd1c_times, dtype=np.float64)
dd1r_times = np.array(dd1r_times, dtype=np.float64)
mdd1r_times = np.array(mdd1r_times, dtype=np.float64)

plt.figure(figsize=(10, 6))

plt.plot(queries, crack_times, marker='.', linestyle='-', color='navy', label="Crack")
plt.plot(queries, ddc_times, marker='+', linestyle='-', color='indianred', label="DDC")
plt.plot(queries, ddr_times, marker='^', linestyle='-', color='seagreen', label="DDR")
plt.plot(queries, dd1c_times, marker='x', linestyle='-', color='tomato', label="DD1C")
plt.plot(queries, dd1r_times, marker='v', linestyle='-', color='limegreen', label="DD1R")
plt.plot(queries, mdd1r_times, marker='*', linestyle='-', color='magenta', label="MDD1R")

plt.xscale("log")
plt.xticks(queries, labels=[f"{q:,}" for q in queries])  

plt.yscale("log")
plt.ylabel("Execution Time (ms)")
plt.xlabel("Number of Queries")

plt.title("Comparison of Crack, DDC, DDR, DD1C, DD1R, MDD1R")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.show()
