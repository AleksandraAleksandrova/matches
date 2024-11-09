import heapq
from collections import defaultdict
import sys

# Purpose: Reads the input file and extracts the number of matches and their details.
# Input: Path to the input file.
# Output: List of tuples representing each matchstick with its endpoints and burn time.
def parse_input(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        matches = []
        for _ in range(n):
            x1, y1, x2, y2, t = map(int, file.readline().strip().split())
            matches.append(((x1, y1), (x2, y2), t))
    return matches

# Purpose: Builds a graph from the matches data.
# Input: List of matches
# Output: Dictionary representing the graph as an adjacency list.
def build_graph(matches):
    graph = defaultdict(list)
    for (x1, y1), (x2, y2), t in matches:
        graph[(x1, y1)].append(((x2, y2), t))
        graph[(x2, y2)].append(((x1, y1), t))
    return graph

# Purpose: Runs Dijkstra’s algorithm to calculate the shortest time for fire to spread from a given starting point to all other nodes.
# Input: Graph and starting node.
# Output: Maximum burn time from the start node to the farthest reachable node.
def dijkstra(graph, start_point):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start_point] = 0
    priority_queue = [(0, start_point)]
    
    # Run Dijkstra's algorithm
    while priority_queue:
        current_time, node = heapq.heappop(priority_queue)
        
        if current_time > distances[node]:
            continue
        
        # Update the distances to neighbors
        for neighbor, burn_time in graph[node]:
            time_to_neighbor = current_time + burn_time
            if time_to_neighbor < distances[neighbor]:
                distances[neighbor] = time_to_neighbor
                heapq.heappush(priority_queue, (time_to_neighbor, neighbor))
                
    # Return the maximum time taken to reach any node
    return max(distances.values())

# Purpose: Finds the optimal ignition point for minimum burn time across the entire figure.
# Input: Graph representing the figure.
# Output: Optimal ignition point coordinates and minimum burn time.
def find_optimal_ignition_point(graph):
    min_burn_time = float('inf')
    best_point = None
    for point in graph:
        burn_time = dijkstra(graph, point)
        if burn_time < min_burn_time:
            min_burn_time = burn_time
            best_point = point
    return best_point, min_burn_time


# Purpose: Main function to execute the solution by reading input, building the graph, and determining the optimal ignition point.
# Input: None
# Output: prints the optimal ignition point and minimum burn time.
def main():
    # Check if the input file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python33 main.py <input_file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    matches = parse_input(file_path)
    graph = build_graph(matches)
    optimal_point, min_burn_time = find_optimal_ignition_point(graph)
    print(f"Optimal Ignition Point: {optimal_point}")
    print(f"Minimum Burn Time: {min_burn_time}")

# Entry point of the program
if __name__ == "__main__":
    main()