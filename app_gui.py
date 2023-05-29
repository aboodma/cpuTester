import itertools
import random
import time
import psutil
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
def calculate_distance(city1, city2):
    # Calculate the Euclidean distance between two cities
    x1, y1 = city1
    x2, y2 = city2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def tsp_brute_force(cities, progress_var):
    # Generate all possible permutations of cities
    permutations = list(itertools.permutations(cities))

    shortest_distance = float('inf')
    shortest_path = None

    # Start the timer
    start_time = time.time()

    # Iterate through each permutation and calculate the total distance
    for i, path in enumerate(permutations):
        total_distance = 0

        # Calculate the distance of the current permutation
        for j in range(len(path) - 1):
            city1 = path[j]
            city2 = path[j + 1]
            total_distance += calculate_distance(city1, city2)

        # Update the shortest distance and path if the current permutation is shorter
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path

        # Update the progress variable
        progress_var.set(int((i + 1) / len(permutations) * 100))

    # Calculate the execution time
    execution_time = time.time() - start_time

    return shortest_distance, shortest_path, execution_time

def generate_chart(shortest_path):
    # Create a figure and plot the shortest path
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(*zip(*shortest_path), marker='o')
    plot.set_title("Shortest Path")
    plot.set_xlabel("X")
    plot.set_ylabel("Y")

    return fig

def run_algorithm():
    num_cities = int(num_cities_entry.get())
    seed = int(seed_entry.get())

    # Generate a random set of cities
    random.seed(seed)
    cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)]

    # Create a progress bar
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.grid(row=3, column=2, columnspan=2, padx=10, pady=20)

    # Run the TSP algorithm
    shortest_distance, shortest_path, execution_time = tsp_brute_force(cities, progress_var)

    # Update the progress bar to show completion
    progress_var.set(100)

    # Generate the chart
    fig = generate_chart(shortest_path)

    # Create a canvas to display the chart
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Display the results
    result_label.config(text=f"Shortest Distance: {shortest_distance:.2f}\nExecution Time: {execution_time:.2f} seconds")

# Create the main window
root = tk.Tk()
root.title("TSP Test")

# Create and position the input controls
num_cities_label = tk.Label(root, text="Number of Cities:")
num_cities_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
num_cities_entry = tk.Entry(root)
num_cities_entry.grid(row=0, column=1, padx=10, pady=5)

seed_label = tk.Label(root, text="Seed:")
seed_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
seed_entry = tk.Entry(root)
seed_entry.grid(row=1, column=1, padx=10, pady=5)

run_button = tk.Button(root, text="Run", command=run_algorithm)
run_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the results
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
