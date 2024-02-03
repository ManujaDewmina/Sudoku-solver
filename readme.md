# Sudoku Solver

This project is based on development of an efficient algorithm capable of tackling Sudoku puzzles with best time complexity and accuracy. The algorithm prioritizes minimizing processing time while maintaining the accuracy of the solution.

Additionally, the algorithm's capabilities will be extended to handle Hexadoku, a variant of the puzzle that uses a 16x16 grid and digits from 1 to 16.

## Implementation

Sudoku solving can consider as an exact cover problem. The exact cover problem is known to be NP-complete problem because there is no known efficient algorithm that can solve it for all possible input sizes. However, there are several efficient algorithms that can solve the problem for many practical applications, including Sudoku solving. 

One such algorithm is Donald Knuth's Algorithm X, which is based on the concept of dancing links. Algorithm X is a backtracking algorithm that systematically explores the search space of possible Sudoku solutions. It maintains a data structure called a "dancing links" matrix, which represents the partial Sudoku solution and the constraints that it must satisfy. The algorithm iteratively fills in the empty cells of the Sudoku grid, making sure that each new digit does not violate any of the constraints. If a contradiction is encountered, the algorithm backtracks and tries another possibility. Algorithm X is known to be efficient for Sudoku solving because it can prune the search space effectively. This means that it can quickly eliminate many invalid solutions and focus on the promising ones. 

## Example

| Input Puzzle         | Solved Puzzle          | Time                   |
| ---------------------- | ---------------------- | ---------------------- |
| ![Input](https://github.com/ManujaDewmina/Sudoku-solver/assets/92631934/61bba46a-06d7-4ed1-9f66-c4f17ababeda) | ![Solved](https://github.com/ManujaDewmina/Sudoku-solver/assets/92631934/5db7e7dc-e87e-4d81-a606-b6031f08816c) | 0.004 seconds     |
## How to run

1. Clone the Github repository : https://github.com/ManujaDewmina/Sudoku-solver

2. Compile three source files using cmd : `g++ sudoku_solver_main.cpp sudoku_solver_16.cpp sudoku_solver_9.cpp -o dancingLinks`

3. Run the executable : `./dancingLinks 'Sample Inputs/input1.txt'`

## Test examples

After run exaple inputs check them using : `python check_output.py` 
