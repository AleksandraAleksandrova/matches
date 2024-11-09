# Optimal Ignition Point for Minimum Burn Time in a Connected Figure of Matches

## Problem description
Given a set of matches arranged on a grid, where each match connects two points, we need to find the optimal point of ignition to ensure the entire connected structure burns in the shortest possible time. Matches can burn from either end, and fire spreads at a constant rate along each matchstick. Each match has a specified burn time when ignited from one end.
The input is provided in a text file with the following format:
- The first line contains an integer n, the number of matches.
- Each subsequent line describes a match with five integers: x1, y1, x2, y2, t, where:
  - (x1, y1) and (x2, y2) are the coordinates of the match's endpoints.
  - t is the time taken for the match to burn completely when ignited from one end.

The objective is to find the ignition point that results in the shortest burn time for the entire structure.

--------------------------------------------------------------------------------------------------------

### Approach
The problem is essentially about finding the optimal starting point in a graph with weighted edges (where each match is an edge between two nodes). The following approach details how we achieve this:
1. Graph Representation:
  - Represent each matchstick as an edge in a graph where each endpoint of a matchstick is a node.
  - Each edge is assigned a weight equal to the burn time of the matchstick (t).
  - The graph is undirected because matches can burn from both ends.

2. Bidirectional Burning Simulation:
  -  Fire can propagate from any point (node) in the structure.
  - From any node, the fire spreads through all connected nodes via edges (matches).
  - To find the optimal ignition point, we need to calculate the maximum time taken to reach any other node from each possible starting node and choose the minimum.

3. Dijkstra’s Algorithm for Shortest Path Calculation:
  - For each node, run Dijkstra’s algorithm to determine the time it would take for fire to spread to all other nodes if it started from that node.
  - Dijkstra's algorithm is chosen because it efficiently finds the shortest path in a graph with positive weights, which corresponds to finding the minimum time to reach each node from a starting node.

4. Finding the Optimal Ignition Point:
  - Calculate the maximum burn time (i.e., time taken to reach the farthest node) for each starting node.
  - The optimal ignition point is the node with the smallest maximum burn time across all starting points.

### Algorithm complexity
1. Time complexity
  - For each node, Dijkstra’s algorithm runs in O((E+V)log⁡V)O((E+V)logV), where VV is the number of nodes (unique endpoints of matches) and E is the number of edges (matches).
  - Since we repeat this process for each node, the overall time complexity is O(V⋅(E+V)log⁡V)O(V⋅(E+V)logV).

2. Space complexity
  - Storing the graph requires O(E+V)O(E+V) space, where EE is the number of edges (matches) and VV is the number of nodes (unique endpoints of matches).
  - Additional space is required for storing distances and the priority queue used in Dijkstra’s algorithm.

### Data Structures 
1. Graph Representation (Dictionary):
  - The graph is represented as a dictionary where each key is a node (coordinate pair (x, y)), and each value is a list of tuples representing edges (neighbor node and burn time).
  - This adjacency list format is efficient for storing sparse graphs, especially since each node typically connects to only a few other nodes.

2. Heap-based Priority Queue:
  - Dijkstra’s algorithm uses a priority queue (min-heap) to efficiently select the next node with the minimum distance.
  - This minimizes the time complexity for updating and retrieving the next closest node.

3. Distance Dictionary:
  - Each node's minimum distance (time taken to reach that node from the start node) is stored in a dictionary.
  - This allows efficient look-up and update operations for Dijkstra’s algorithm.

### Example usage
```python
python main.py input.txt
```