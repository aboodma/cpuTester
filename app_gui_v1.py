import itertools
import random
import time
import psutil
from tqdm import tqdm
import tkinter as tk
from tkinter import messagebox

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

def show_contact_info():
    # Display contact information in a message box
    messagebox.showinfo("Contact Information", "Developer: Your Name\nEmail: your.email@example.com\nPhone: +1234567890")

def start_computation(num_cities, seed):
    # Generate a random set of cities
    random.seed(seed)
    cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)]

    # Solve TSP using brute force
    shortest_distance, shortest_path, execution_time = tsp_brute_force(cities)

    # Calculate CPU speed rating
    baseline_time = 1.0  # Baseline execution time in seconds
    cpu_mark = int(baseline_time / execution_time * 100)

    # Display results in a message box
    result_message = f"Number of Cities: {num_cities}\nShortest Distance: {shortest_distance}\nShortest Path: {shortest_path}\nExecution Time: {execution_time} seconds\nCPU Speed Rating: {cpu_mark}"
    messagebox.showinfo("TSP Solver Results", result_message)

# Create a tkinter window
window = tk.Tk()
window.title("TSP Solver")

# Add a label with your name and contact information
contact_label = tk.Label(window, text="Developer: Abdulrahman Mardinli\nEmail: aboodma@gmail.com\nPhone: +905523490964")
contact_label.pack()

# Add an entry field for the number of cities
num_cities_label = tk.Label(window, text="Number of Cities:")
num_cities_label.pack()
num_cities_entry = tk.Entry(window)
num_cities_entry.pack()

# Add an entry field for the seed
seed_label = tk.Label(window, text="Seed:")
seed_label.pack()
seed_entry = tk.Entry(window)
seed_entry.pack()

# Add a button to start the computation
compute_button = tk.Button(window, text="Start Computation", command=lambda: start_computation(int(num_cities_entry.get()), int(seed_entry.get())))
compute_button.pack()

# Add a button to display contact information
contact_button = tk.Button(window, text="Contact Info", command=show_contact_info)
contact_button.pack()

# Start the tkinter event loop
window.mainloop()
