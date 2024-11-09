import heapq
from collections import defaultdict

def parse_input(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        matches = []
        for _ in range(n):
            x1, y1, x2, y2, t = map(int, file.readline().strip().split())
            matches.append(((x1, y1), (x2, y2), t))
    return matches

def build_graph(matches):
    graph = defaultdict(list)
    for (x1, y1), (x2, y2), t in matches:
        graph[(x1, y1)].append(((x2, y2), t))
        graph[(x2, y2)].append(((x1, y1), t))
    return graph

def dijkstra(graph, start_point):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start_point] = 0
    priority_queue = [(0, start_point)]
    
    while priority_queue:
        current_time, node = heapq.heappop(priority_queue)
        
        if current_time > distances[node]:
            continue
        
        for neighbor, burn_time in graph[node]:
            time_to_neighbor = current_time + burn_time
            if time_to_neighbor < distances[neighbor]:
                distances[neighbor] = time_to_neighbor
                heapq.heappush(priority_queue, (time_to_neighbor, neighbor))
                
    # Return the maximum time taken to reach any node
    return max(distances.values())

def find_optimal_ignition_point(graph):
    min_burn_time = float('inf')
    best_point = None
    for point in graph:
        burn_time = dijkstra(graph, point)
        if burn_time < min_burn_time:
            min_burn_time = burn_time
            best_point = point
    return best_point, min_burn_time

def main(file_path):
    matches = parse_input(file_path)
    graph = build_graph(matches)
    optimal_point, min_burn_time = find_optimal_ignition_point(graph)
    print(f"Optimal Ignition Point: {optimal_point}")
    print(f"Minimum Burn Time: {min_burn_time}")

# Run the program with the file path to your input
file_path = '/home/aleks/Desktop/uni/matches/figure.txt'
main(file_path)
