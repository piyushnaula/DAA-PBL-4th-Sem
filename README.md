# Maze Master – Pathfinding Algorithm Visualizer

**Maze Master** is a Python-based project designed to visualize and compare five fundamental pathfinding algorithms: **A* Heuristic**, **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, **Dijkstra's Algorithm**, and **Bellman-Ford Algorithm**. The project aims to provide an interactive way to understand how these algorithms navigate through a maze to find the shortest path.

## Project Overview

* **Language:** Python
* **Library Used:** `pyamaze` for maze generation and visualization
* **Purpose:** To demonstrate and compare the efficiency and pathfinding capabilities of different algorithms in a maze environment.

## Repository Structure

```
DAA-PBL-4th-Sem/
├── Algorithms/
│   ├── aStar.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   └── bellman_ford.py
├── README.md
```

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/piyushnaula/DAA-PBL-4th-Sem.git
   cd DAA-PBL-4th-Sem/Algorithms
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Then, install the required library:

   ```bash
   pip install pyamaze
   ```

3. **Run an Algorithm:**
   Execute any of the algorithm scripts to see the visualization. For example:

   ```bash
   python aStar.py
   ```

   You'll be prompted to enter the number of rows and columns for the maze. After inputting, the maze will be generated, and the algorithm will visualize the pathfinding process.

## Algorithms Implemented

* **A* Heuristic Algorithm:** Combines the benefits of Dijkstra's Algorithm and a heuristic to find the most efficient path.
* **Breadth-First Search (BFS):** Explores all neighboring nodes at the present depth before moving on to nodes at the next depth level.
* **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking.
* **Dijkstra's Algorithm:** Finds the shortest path between nodes in a graph, which may represent, for example, road networks.
* **Bellman-Ford Algorithm:** Computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.([GitHub][1])

## Visualization Details

* **Visited Paths:** Displayed in yellow.
* **Final Shortest Path:** Displayed in blue or green, depending on the algorithm.
* **Metrics Displayed:** Path length and execution time are shown using on-screen labels.([GitHub][2])

## Contributors

* **Piyush Naula:** Implemented the A\* Heuristic Algorithm and integrated visualization features.
* **Yogesh Shahi:** Implemented the Dijkstra Algorithm and integrated visualization features.
* **Mrityunjay:** Implemented the BFS Algorithm and integrated visualization features.
* **Harshit Mahara:** Implemented the DFS and Bellman Ford and integrated visualization features.
