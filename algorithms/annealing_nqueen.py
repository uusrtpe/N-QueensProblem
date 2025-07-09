import random
import math
import time

# Calculate number of attacking queen pairs
def calculate_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or \
               abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Generate a random board
def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# Simulated Annealing algorithm
def simulated_annealing(n, initial_temp=1000, cooling_rate=0.995, min_temp=0.001):
    board = random_board(n)
    current_conflicts = calculate_conflicts(board)
    temp = initial_temp
    start_time = time.time()

    while temp > min_temp:
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        while col == board[row]:
            col = random.randint(0, n - 1)

        new_board = board.copy()
        new_board[row] = col
        new_conflicts = calculate_conflicts(new_board)

        delta = new_conflicts - current_conflicts

        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temp):
            board = new_board
            current_conflicts = new_conflicts

        if current_conflicts == 0:
            end_time = time.time()
            return {
                "solution": board,
                "time": end_time - start_time,
                "success": True
            }

        temp *= cooling_rate

    end_time = time.time()
    return {
        "solution": None,
        "time": end_time - start_time,
        "success": False
    }

# Test
if __name__ == "__main__":
    result = simulated_annealing(10)
    if result["success"]:
        print("Solution found:", result["solution"])
    else:
        print("No solution found.")
    print("Execution time:", result["time"], "seconds")
