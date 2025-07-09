import random
import time

# Count attacking pairs
def calculate_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or \
               abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Create initial population
def initialize_population(n, size):
    return [random.sample(range(n), n) for _ in range(size)]

# Select top-k fittest individuals
def select_parents(population, k):
    scored = sorted(population, key=calculate_conflicts)
    return scored[:k]

# Crossover two parents
def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(0, n - 1)
    child = parent1[:point]
    for gene in parent2:
        if gene not in child:
            child.append(gene)
    return child

# Mutate by swapping two positions
def mutate(board, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(board)), 2)
        board[i], board[j] = board[j], board[i]
    return board

# Genetic Algorithm
def genetic_algorithm(n, population_size=100, generations=1000, mutation_rate=0.05):
    population = initialize_population(n, population_size)
    start_time = time.time()

    for gen in range(generations):
        population = select_parents(population, population_size // 2)
        next_gen = []

        while len(next_gen) < population_size:
            p1, p2 = random.sample(population, 2)
            child = crossover(p1, p2)
            child = mutate(child, mutation_rate)
            next_gen.append(child)

        population = next_gen

        best = min(population, key=calculate_conflicts)
        if calculate_conflicts(best) == 0:
            end_time = time.time()
            return {
                "solution": best,
                "time": end_time - start_time,
                "generations": gen,
                "success": True
            }

    end_time = time.time()
    return {
        "solution": None,
        "time": end_time - start_time,
        "generations": generations,
        "success": False
    }

# Test
if __name__ == "__main__":
    result = genetic_algorithm(10)
    if result["success"]:
        print("Solution found:", result["solution"])
    else:
        print("No solution found.")
    print("Execution time:", result["time"], "seconds")
    print("Generations:", result["generations"])
