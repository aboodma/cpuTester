import itertools
import random
import time
import psutil
from tqdm import tqdm

def calculate_distance(city1, city2):
    # Calculate the Euclidean distance between two cities
    x1, y1 = city1
    x2, y2 = city2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def tsp_brute_force(cities):
    # Generate all possible permutations of cities
    permutations = list(itertools.permutations(cities))

    shortest_distance = float('inf')
    shortest_path = None

    # Create a progress bar
    progress_bar = tqdm(total=len(permutations), unit=' permutations', dynamic_ncols=True)

    # Start the timer
    start_time = time.time()

    # Iterate through each permutation and calculate the total distance
    for path in permutations:
        total_distance = 0

        # Calculate the distance of the current permutation
        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]
            total_distance += calculate_distance(city1, city2)

        # Update the shortest distance and path if the current permutation is shorter
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path

        # Update the progress bar description
        progress_bar.set_description(f"Shortest Distance: {shortest_distance:.2f}")

        # Update the progress bar
        progress_bar.update(1)

    # Stop the timer
    end_time = time.time()

    # Close the progress bar
    progress_bar.close()

    # Calculate the execution time
    execution_time = end_time - start_time

    return shortest_distance, shortest_path, execution_time


print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||| Abdulrahman Mardinli ||||||||||||||||||||||||||||||||||||||")
print("|||||||||||||||||||||||||||||||||||||||| aboodma@gmail.com ||||||||||||||||||||||||||||||||||||||||")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


# Generate a random set of cities
random.seed(40)
num_cities = 5
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)]

shortest_distance, shortest_path, execution_time = tsp_brute_force(cities)

# Calculate CPU speed rating
baseline_time = 1.0  # Baseline execution time in seconds
cpu_mark = int(baseline_time / execution_time * 100)

print("Number of Cities:", num_cities)
print("Shortest Distance:", shortest_distance)
print("Shortest Path:", shortest_path)
print("Execution Time:", execution_time, "seconds")
print("CPU Speed Rating :", cpu_mark)
