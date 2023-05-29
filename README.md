# TSP Solver with GUI

This is a Python application that solves the Traveling Salesman Problem (TSP) using a brute-force approach. It provides both a command-line interface (CLI) and a graphical user interface (GUI) to interact with the application.

## Features

- Generates all possible permutations of cities
- Calculates the Euclidean distance between cities
- Displays a progress bar during the computation
- Provides the shortest distance and corresponding path
- Measures the execution time of the algorithm
- Calculates the CPU speed rating based on the execution time
- Graphical User Interface (GUI) for user interaction

## Requirements

- Python 3.x
- The following Python packages:
  - itertools
  - random
  - time
  - psutil
  - tqdm
  - tkinter (for the GUI version)

## Note
The ExE version of app you can find it in "dist" folder
## Usage

1. Install the required packages using `pip install itertools random time psutil tqdm tkinter`.
2. Run the `app.py` script with Python to use the command-line interface.
3. Alternatively, run the `app_gui.py` script with Python to use the graphical user interface.
4. In the GUI version, you can input the number of cities and seed, and then click a button to start the computation.
5. The GUI will display a progress bar and update the shortest distance and path dynamically.
6. After the computation finishes, the GUI will display the final results, including the number of cities, shortest distance, shortest path, execution time, and CPU speed rating.
7. In the command-line interface, the results will be displayed in the console.

Feel free to customize the seed, number of cities, and baseline time in the scripts to experiment with different scenarios.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or enhancements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

