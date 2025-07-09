import time
import tracemalloc
import random

#################### DFS ####################
def dfs_solve(n):
    board = [-1] * n
    solutions = []
    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    def solve(row):
        if row == n:
            solutions.append(board.copy())
            return True
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if solve(row + 1):
                    return True
                board[row] = -1
        return False
    return solve(0)

def run_dfs(n):
    try:
        tracemalloc.start()
        start = time.time()
        found = dfs_solve(n) if n <= 12 else False
        t = time.time() - start
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return found, t, peak / 1024
    except Exception as e:
        return False, -1, -1

#################### Hill Climbing ####################
def hill_climbing_solve(n, max_restarts=10, timeout=10):
    def calculate_conflicts(board):
        conflicts = 0
        for i in range(n):
            for j in range(i+1, n):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    start_time = time.time()
    for restart in range(max_restarts):
        if time.time() - start_time > timeout:
            break
        board = [random.randint(0, n-1) for _ in range(n)]
        current_conflicts = calculate_conflicts(board)
        improved = True
        while improved:
            if time.time() - start_time > timeout:
                break
            improved = False
            best_move = board[:]
            best_conflicts = current_conflicts
            for row in range(n):
                original_col = board[row]
                for col in range(n):
                    if col == original_col:
                        continue
                    board[row] = col
                    conflicts = calculate_conflicts(board)
                    if conflicts < best_conflicts:
                        best_conflicts = conflicts
                        best_move = board[:]
                        improved = True
                board[row] = original_col
            board = best_move
            current_conflicts = best_conflicts
            if current_conflicts == 0:
                return True
    return False

def run_hill_climbing(n):
    try:
        tracemalloc.start()
        start = time.time()
        found = hill_climbing_solve(n)
        t = time.time() - start
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return found, t, peak / 1024
    except Exception as e:
        return False, -1, -1

#################### Simulated Annealing ####################
def simulated_annealing_solve(n, initial_temp=1000, cooling_rate=0.995, min_temp=0.01, timeout=10):
    def calculate_conflicts(board):
        conflicts = 0
        for i in range(n):
            for j in range(i+1, n):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    board = [random.randint(0, n-1) for _ in range(n)]
    current_conflicts = calculate_conflicts(board)
    temp = initial_temp
    start_time = time.time()
    while temp > min_temp and (time.time() - start_time < timeout):
        row = random.randint(0, n-1)
        col = random.randint(0, n-1)
        while col == board[row]:
            col = random.randint(0, n-1)
        new_board = board[:]
        new_board[row] = col
        new_conflicts = calculate_conflicts(new_board)
        delta = new_conflicts - current_conflicts
        if delta < 0 or random.uniform(0, 1) < pow(2.71828, -delta/temp):
            board = new_board
            current_conflicts = new_conflicts
        if current_conflicts == 0:
            return True
        temp *= cooling_rate
    return False

def run_simulated_annealing(n):
    try:
        tracemalloc.start()
        start = time.time()
        found = simulated_annealing_solve(n)
        t = time.time() - start
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return found, t, peak / 1024
    except Exception as e:
        return False, -1, -1

#################### Genetic Algorithm ####################
def genetic_algorithm_solve(n, population_size=50, generations=2000, mutation_rate=0.05, timeout=10):
    def calculate_conflicts(board):
        conflicts = 0
        for i in range(n):
            for j in range(i+1, n):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    def crossover(p1, p2):
        n = len(p1)
        point = random.randint(0, n-1)
        child = p1[:point]
        for x in p2:
            if x not in child:
                child.append(x)
        while len(child) < n:
            child.append(random.randint(0, n-1))
        return child
    def mutate(board):
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(board)), 2)
            board[i], board[j] = board[j], board[i]
        return board
    population = [[random.randint(0, n-1) for _ in range(n)] for _ in range(population_size)]
    start_time = time.time()
    for gen in range(generations):
        if time.time() - start_time > timeout:
            break
        population.sort(key=calculate_conflicts)
        if calculate_conflicts(population[0]) == 0:
            return True
        next_gen = population[:population_size//2]
        while len(next_gen) < population_size:
            p1, p2 = random.sample(population[:10], 2)
            child = crossover(p1, p2)
            child = mutate(child)
            next_gen.append(child)
        population = next_gen
    return False

def run_genetic_algorithm(n):
    try:
        tracemalloc.start()
        start = time.time()
        found = genetic_algorithm_solve(n)
        t = time.time() - start
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return found, t, peak / 1024
    except Exception as e:
        return False, -1, -1

#################### Karşılaştırma Tablosu ####################
def main():
    ns = [10, 30, 50, 100, 200]
    print("\n============== N-Queens Comparison ==============\n")
    header = f"{'N':>6} | {'DFS':^20} | {'HillClimb':^20} | {'SimAnneal':^20} | {'GeneticAlg':^20}"
    print(header)
    print("-" * len(header))
    for n in ns:
        row = [f"{n:>6}"]
        # --- DFS ---
        if n > 12:
            row.append(f"{'SKIP':^20}")
        else:
            found, t, mem = run_dfs(n)
            row.append(f"{'Y' if found else 'N'} | {t:.2f}s | {mem:.0f}KB")
        # --- Hill Climbing ---
        found, t, mem = run_hill_climbing(n)
        row.append(f"{'Y' if found else 'N'} | {t:.2f}s | {mem:.0f}KB")
        # --- Simulated Annealing ---
        found, t, mem = run_simulated_annealing(n)
        row.append(f"{'Y' if found else 'N'} | {t:.2f}s | {mem:.0f}KB")
        # --- Genetic Algorithm ---
        found, t, mem = run_genetic_algorithm(n)
        row.append(f"{'Y' if found else 'N'} | {t:.2f}s | {mem:.0f}KB")
        print(" | ".join(row))
    print("\nLegend: Y = Solution Found, N = Not Found, s = seconds, KB = kilobytes\n")
    print("Note: DFS is skipped for N > 12 due to impractical runtime/memory.")

if __name__ == "__main__":
    main()
