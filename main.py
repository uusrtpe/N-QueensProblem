import csv
import time
import os

from algorithms.dfs_nqueen import dfs_nqueen
from algorithms.hillclimb_nqueen import hill_climbing
from algorithms.annealing_nqueen import simulated_annealing
from algorithms.genetic_nqueen import genetic_algorithm

# Dictionary of all algorithms to test
algorithms = {
    "DFS": dfs_nqueen,
    "HillClimb": hill_climbing,
    "Annealing": simulated_annealing,
    "Genetic": genetic_algorithm
}

# Values of N to test
n_values = [10, 30, 50, 100, 200]

results = []

# Run each algorithm for each N
for n in n_values:
    print(f"\nTesting N = {n}...")
    for name, func in algorithms.items():
        print(f"  Running {name}...")

        try:
            # Skip DFS for large N due to performance limits
            if name == "DFS" and n > 12:
                print("    Skipped (DFS is too slow for N > 30)")
                continue

            result = func(n)

            if result.get("success", True) or name == "DFS":
                duration = result["time"]
            else:
                duration = -1  # failed

            results.append([name, n, duration])

        except Exception as e:
            print(f"    Error: {e}")
            results.append([name, n, -1])

# Save results to CSV
os.makedirs("results", exist_ok=True)
with open("results/performance.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Algorithm", "N", "Time(s)"])
    writer.writerows(results)

print("\n✅ All tests completed. Results saved to 'results/performance.csv'.")
