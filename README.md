 ## 📑 Project Report

Solving the N-Queens Problem: Exhaustive Search vs. Genetic Algorithm* (Ummuhan Saritepe; Univ. of Europe for Applied Sciences)

This report compares a classic exact method—**Depth-First Search (DFS)**—with a heuristic **Genetic Algorithm (GA)** for the N-Queens problem under the same conditions.  
- **Methods**
  - **DFS (backtracking):** exact and complete; explores the state space with pruning (row/column/diagonal conflicts), performs well for small boards but scales poorly as N grows.
  - **GA (heuristic):** permutation encoding (index = row, value = column) to ensure one queen per row/column; fitness penalizes diagonal conflicts; standard **selection–crossover–mutation** with **elitism**. Tuned parameters used in the study: **population = 100**, **generations = 1000**, **elitism ≈ 20%**, **mutation rate ≈ 1%**.
- **Experimental setup:** Python implementations of both approaches; side-by-side tests across increasing board sizes *N*.
- **Results**
  - **DFS:** fast for small *N*, but runtime grows **exponentially**; becomes **impractical beyond ~N = 20**.
  - **GA:** **scales more smoothly**; consistently found valid solutions **up to N = 100** within the allowed generations and typically **within seconds** (stochastic, so runs can vary).
- **Takeaways**
  - **Trade-off:** DFS guarantees completeness; GA offers scalability and speed on large boards but doesn’t enumerate all solutions.
  - **Sensitivity:** GA convergence depends on mutation rate and elite size—too low risks stagnation; too high hurts convergence.
- **Future directions:** Hybrid GA + local search, **simulated annealing**, and improved mutation/selection strategies to boost convergence and avoid local optima.



