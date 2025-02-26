import sys
from queue import PriorityQueue
from helper_functions import read_cities, read_roads, haversine, reconstruct_path

# A* algorithm implementation
def astar(cities, roads, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    
    g_score = {city: float('inf') for city in cities}
    g_score[start] = 0
    f_score = {city: float('inf') for city in cities}
    f_score[start] = haversine(cities[start][0], cities[start][1], cities[goal][0], cities[goal][1])
    
    came_from = {}
    
    while not open_set.empty():
        current = open_set.get()[1]
        
        if current == goal:
            return reconstruct_path(came_from, current), g_score[goal]
        
        for neighbor, distance in roads.get(current, []):
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + haversine(cities[neighbor][0], cities[neighbor][1], cities[goal][0], cities[goal][1])
                open_set.put((f_score[neighbor], neighbor))
    
    return None, float('inf')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gns938_Astar.py <start_city> <goal_city>")
        sys.exit(1)

    start_city = sys.argv[1]
    goal_city = sys.argv[2]

    cities = read_cities('cities.csv')
    roads = read_roads('roads.csv', cities)

    if start_city not in cities or goal_city not in cities:
        print("Error: One or both cities not found in the dataset.")
        sys.exit(1)

    path, total_distance = astar(cities, roads, start_city, goal_city)

    if path:
        print(" - ".join(path))
        print(f"Total Distance - {total_distance:.2f} km")
    else:
        print("Path not found!")
