import time  # Used to measure execution time

# Check if a queen can be safely placed at board[row][col]
def is_safe(board, row, col):
    for i in range(row):
        # Check same column and both diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Main DFS function to solve N-Queens
def dfs_nqueen(n):
    solutions = []  # List to store all valid board configurations
    board = [-1] * n  # Initialize board with -1 (no queen placed)

    # Recursive function to place queens row by row
    def solve(row):
        if row == n:
            solutions.append(board.copy())  # Found valid configuration
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place queen
                solve(row + 1)    # Move to next row
                board[row] = -1   # Backtrack

    start_time = time.time()
    solve(0)
    end_time = time.time()

    return {
        "solutions": solutions,
        "count": len(solutions),
        "time": end_time - start_time
    }

# Test the function
if __name__ == "__main__":
    result = dfs_nqueen(10)
    print("Number of solutions:", result["count"])
    print("Execution time:", result["time"], "seconds")
