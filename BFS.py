import sys
from collections import deque
from helper_functions import read_cities, read_roads, reconstruct_path

# BFS algorithm implementation
def bfs(cities, roads, start, goal):
    queue = deque([(start, 0)])  # Queue stores (city, distance_traveled)
    visited = {start}
    came_from = {}
    total_distances = {start: 0}

    while queue:
        current, current_distance = queue.popleft()

        if current == goal:
            return reconstruct_path(came_from, current), total_distances[goal]

        for neighbor, distance in roads.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                total_distances[neighbor] = current_distance + distance
                queue.append((neighbor, total_distances[neighbor]))

    return None, float('inf')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gns938_BFS.py <start_city> <goal_city>")
        sys.exit(1)

    start_city = sys.argv[1]
    goal_city = sys.argv[2]

    cities = read_cities('cities.csv')
    roads = read_roads('roads.csv', cities)

    if start_city not in cities or goal_city not in cities:
        print("Error: One or both cities not found in the dataset.")
        sys.exit(1)

    path, total_distance = bfs(cities, roads, start_city, goal_city)

    if path:
        print(" - ".join(path))
        print(f"Total Distance - {total_distance:.2f} km")
    else:
        print("Path not found!")
