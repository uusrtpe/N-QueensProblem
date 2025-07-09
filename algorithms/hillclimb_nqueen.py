import random
import time

# Calculate the number of attacking queen pairs
def calculate_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Generate a random board
def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# Hill Climbing algorithm with timeout
def hill_climbing(n, max_restarts=10, timeout=10):
    start_time = time.time()

    for restart in range(max_restarts):
        if time.time() - start_time > timeout:
            break  # Time limit reached

        board = random_board(n)
        current_conflicts = calculate_conflicts(board)

        while True:
            if time.time() - start_time > timeout:
                break  # Time limit reached

            neighbors = []
            for row in range(n):
                for col in range(n):
                    if board[row] != col:
                        new_board = board.copy()
                        new_board[row] = col
                        conflicts = calculate_conflicts(new_board)
                        neighbors.append((conflicts, new_board))

            neighbors.sort(key=lambda x: x[0])
            best_conflicts, best_board = neighbors[0]

            if best_conflicts >= current_conflicts:
                break  # Local minimum

            board = best_board
            current_conflicts = best_conflicts

            if current_conflicts == 0:
                end_time = time.time()
                return {
                    "solution": board,
                    "time": end_time - start_time,
                    "restarts": restart,
                    "success": True
                }

    end_time = time.time()
    return {
        "solution": None,
        "time": end_time - start_time,
        "restarts": max_restarts,
        "success": False
    }

# For manual testing
if __name__ == "__main__":
    result = hill_climbing(10)
    if result["success"]:
        print("Solution found:", result["solution"])
    else:
        print("No solution found.")
    print("Execution time:", result["time"], "seconds")
    print("Restarts:", result["restarts"])
