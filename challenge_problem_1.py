# CHALLENGE PROBLEM 1: WAREHOUSE ROBOT MANGEMENT
# DHRUV PATHAK & OLIVIA FELTON
# =======================================

# IMPORTS
# =======================================

import math
import random
import matplotlib.pyplot as plt

# FUNCTION DEFINITIONS
# =======================================

# Function to plot the grid with the robots intial and final positions
def plotting_grid():
    global initial_xy, end_xy, robot_type, color_map, n

    # Creating plot
    fig, ax = plt.subplots(figsize=(n, n))
    ax.set_xlim(-1, n)
    ax.set_ylim(-1, n)
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.set_title("Robot Grid Navigation")

    added_labels = set()

    for i in range(len(initial_xy)):
        x_init, y_init = initial_xy[i]
        x_end, y_end = end_xy[i]
        robot_color = color_map[robot_type[i]]
        ax.plot([x_init, x_end], [y_init, y_end], linestyle='--', color=robot_color, linewidth=1)  

        # Add initial point (circle marker)
        if robot_type[i] not in added_labels:
            ax.scatter(x_init, y_init, color=robot_color, marker='o', label=robot_type[i])
            added_labels.add(robot_type[i])
        else:
            ax.scatter(x_init, y_init, color=robot_color, marker='o')

        # Add end point (square marker)
        ax.scatter(x_end, y_end, color=robot_color, marker='s')
    # Add legend
    ax.legend()

    plt.show()

# Function to update the grid with the robots
def grid_update(grid):
    global initial_xy, robot_type, rows, cols

    # Reset grid before placing robots
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 0 
    
    # Place robots at new positions
    for i, (x, y) in enumerate(initial_xy):
        grid[x][y] = robot_type[i]  

# Function to calculate the distance from intial to end point (Euclidean Distance)
def distance(start_point, end_point):
    return round(math.sqrt(((end_point[1] - start_point[1])**2) + ((end_point[0] - start_point[0])**2)), 1)

# X Axis movement of the robot
def move_x(i):
    global decider_xy, initial_xy, end_xy

    # Moving forward in X direction
    if end_xy[i][0] > initial_xy[i][0]:
        decider_xy[i][0] = initial_xy[i][0] + 1

    # Moving backward in X direction
    elif end_xy[i][0] < initial_xy[i][0]:
        decider_xy[i][0] = initial_xy[i][0] - 1

    # If X is already at the destination
    else:
        decider_xy[i][0] = initial_xy[i][0]

    # Keep Y constant
    decider_xy[i][1] = initial_xy[i][1]  

# Y Axis movement of the robot
def move_y(i):
    global decider_xy, initial_xy, end_xy

    # Moving forward in Y direction
    if end_xy[i][1] > initial_xy[i][1]:
        decider_xy[i][1] = initial_xy[i][1] + 1

    # Moving backward in Y direction
    elif end_xy[i][1] < initial_xy[i][1]:
        decider_xy[i][1] = initial_xy[i][1] - 1

    # If Y is already at the destination
    else:
        decider_xy[i][1] = initial_xy[i][1]

    # Keep X constant
    decider_xy[i][0] = initial_xy[i][0] 

# Function to avoid collision between robots
def collision_avoidance():
    global decider_xy, decider_grid, robot_type, robot_distance, initial_xy, end_xy

    # Nested loop to check for collision between robots
    for i in range (0, len(decider_xy)):
        for j in range(i+1, len(decider_xy)):

            # To check if collision is at the final destination or not
            if decider_xy[i] == decider_xy[j] and end_xy[i] != end_xy[j]:
                # Checking if its a ground robot or an aerial robot
                if ((robot_type[i] != 'quadrotor' and robot_type[j] != 'quadrotor') or (robot_type[i] == 'quadrotor' and robot_type[j] == 'quadrotor')):
                    # Move the robot which is closer to the destination
                    if robot_distance[i] < robot_distance[j]: 
                        decider_xy[i] = initial_xy[i]
                    elif robot_distance[i] > robot_distance[j]:
                        decider_xy[j] = initial_xy[j]
                    # If both robots are at the same distance from the destination
                    else:
                        toss = random.choice(['heads', 'tails'])
                        if toss == 'heads':
                            decider_xy[i] = initial_xy[i]
                        elif toss == 'tails':
                            decider_xy[j] = initial_xy[j]

# Function to decide the movement of the robots
def decider():
    global initial_xy, decider_grid, grid, decider_xy, robot_type

    # Assume all robots reached destination
    flag = 0  

    # Iterating through each robot
    for i in range(len(robot_type)):

        # Move only if not at destination
        if initial_xy[i] != end_xy[i]:
            # Updating to show all robots are not at final destination
            flag = 1  
            if initial_xy[i][0] != end_xy[i][0]:
                # Move along X first  
                move_x(i)  
            elif initial_xy[i][1] != end_xy[i][1]:
                # Move along Y after X is correct  
                move_y(i)  
        else:
            continue

    # Checking for collision avoidance
    collision_avoidance()

    # Updating decider_grid post collision avoidance
    for i, (x, y) in enumerate(decider_xy):
        if 0 <= x < rows and 0 <= y < cols:
            decider_grid[x][y] = robot_type[i]
    
    # Updating initial_xy
    for i in range(len(robot_type)):
        initial_xy[i] = decider_xy[i][:]

    # Updating the grid with the new positions
    grid_update(grid) 

    # Plotting the grid with the new positions
    plotting_grid()

    # Returning the flag value
    return flag 

# MAIN CODE EXECUTION
# =======================================

# Getting the value of N
n = int(input("Enter value of N to make a NxN Grid: "))

# Checking if the value of N is between 3 and 10
if 3 <= n <= 10:
    rows, cols = n, n
else:
    print("Please enter a value between 3 and 10")
    exit()

num_robots = 2*n
# rows, cols = 5, 5

# Generating Main Grid and Decider Grid
grid = [[0] * rows for _ in range(cols)]
decider_grid = [[0] * rows for _ in range(cols)]

# Generating Initial and End Coordinates and Robot Types
# Randomly choose 2*n combinations of 'humanoid', 'quadrotor', or 'driver'
robot_list = ['humanoid', 'quadrotor', 'driver']
robot_type = [random.choice(robot_list) for _ in range(num_robots)]

# Generate a list of 2*n random [x, y] coordinates, each between 0 and n-1
initial_xy = [[random.randint(0, n-1), random.randint(0, n-1)] for _ in range(num_robots)]
end_xy = [[random.randint(0, n-1), random.randint(0, n-1)] for _ in range(num_robots)]

# print("Initial Coordinates: ", initial_xy)  
print("Total Robots: ", num_robots)

# Initialize decider_xy to 0
decider_xy = [[0, 0] for _ in range(len(robot_type))]

# Define colors for each robot type
color_map = {'humanoid': 'blue', 'quadrotor': 'red', 'driver': 'green'}

# Define a list to store the distance of each robot from the destination
robot_distance = []

# Getting the distance of each robot
robot_distance = [distance(initial_xy[i], end_xy[i]) for i in range(len(robot_type))]

# Update the grid with the inital robots positions
grid_update(grid)

# Counter to check if all robots have reached the destination
flag1 = 1

# Plot the initial grid
plotting_grid()

# Loop to move the robots
while flag1 == 1:
    flag1 = decider()