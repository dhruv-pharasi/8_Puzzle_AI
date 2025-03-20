# 8-Puzzle Solver

## Overview
This project implements **Depth-First Search (DFS), Breadth-First Search (BFS), and Best-First Search** algorithms to solve the **8-puzzle game**. The program takes an initial puzzle state as input and finds a sequence of moves to reach the goal state.

## What is the 8-Puzzle Game?
The 8-puzzle is a sliding tile puzzle consisting of a **3x3 grid** with **eight numbered tiles** and one **empty space**. The goal is to move tiles into the correct order by sliding them into the empty space.

**Example**:  

Initial State:  
4  3  2
5  6  1
7  8  _

Goal State:  
1  2  3
4  5  6
7  8  _

## Search Algorithms Implemented
1. **Depth-First Search (DFS)**: Explores as deep as possible before backtracking.  
2. **Breadth-First Search (BFS)**: Explores nodes level by level for optimal solutions.  
3. **Best-First Search**: Uses heuristic functions to guide the search.  

## How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/dhruv-pharasi/8_Puzzle_AI.git
   ```
2. Install dependencies (if needed):  
   `pip install numpy`
3. Run the script:  
   `python 8_puzzle.py`

## Results
- **DFS**: May not find the optimal solution and can get stuck in deep search branches.  
- **BFS**: Guarantees the shortest path solution but is memory-intensive.  
- **Best-First Search**: Uses heuristics for efficient searching but may not always be optimal.

## Future Improvements
- Implement **A\*** search for optimal and efficient solving.  
- Allow **custom heuristics** for better performance.  
- Add **GUI visualization** of moves.

## Author
[Dhruv Pharasi](https://github.com/dhruv-pharasi)
