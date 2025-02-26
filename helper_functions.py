import csv
import math

# Function to read city data from CSV file
def read_cities(file_path):
    cities = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            city, lat, lon = row
            cities[city] = (float(lat), float(lon))
    return cities

# Function to read road connections from CSV file
def read_roads(file_path, cities):
    roads = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            city1, city2 = row
            distance = haversine(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
            if city1 not in roads:
                roads[city1] = []
            if city2 not in roads:
                roads[city2] = []
            roads[city1].append((city2, distance))
            roads[city2].append((city1, distance))
    return roads

# Haversine distance formula
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Function to reconstruct the path from start to goal
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path
