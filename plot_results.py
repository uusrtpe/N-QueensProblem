import csv
import matplotlib.pyplot as plt

# Read results from CSV
data = {}
with open("results/performance.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        algorithm = row["Algorithm"]
        n = int(row["N"])
        time = float(row["Time(s)"])

        if algorithm not in data:
            data[algorithm] = {"N": [], "Time": []}
        data[algorithm]["N"].append(n)
        data[algorithm]["Time"].append(time)

# Plotting
plt.figure(figsize=(10, 6))

for algo, values in data.items():
    plt.plot(values["N"], values["Time"], marker="o", label=algo)

plt.title("Execution Time vs. N (Number of Queens)")
plt.xlabel("N (Board Size)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("results/runtime_plot.png")
plt.show()
