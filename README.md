# Warehouse Robot Management System Design

## Objective
Develop an efficient system that manages multiple types of robots—**Humanoid**, **Quadrotor**, and **Driver**—navigating a grid to reach their respective destinations while avoiding collisions.

## Grid Initialization
- Create a square **N x N** grid.
- Randomly place **2 × N** robots on the grid.
- Each robot has a type, initial position, and destination.

## Robot Types & Properties
- Three types: Humanoid, Quadrotor, Driver
- Each robot has a defined start location and target destination.

## Movement Strategy
- Robots move stepwise towards destinations:
  - First move horizontally along the X-axis.
  - Then move vertically along the Y-axis.
- Path chosen based on Euclidean distance for shortest route.

## Collision Avoidance
- If two robots attempt to move to the same position:
  - Priority given to the robot closer to its destination.
  - If distances are equal, movement is decided randomly (e.g., coin toss).

## Decider Function (`decider()`)
- Iterates over all robots to determine their next move.
- Calls movement functions (`move_x()`, `move_y()`) to update positions.
- Checks and resolves collisions through `collision_avoidance()`.
- Updates the grid and visualizes new positions.

## Visualization
- Uses **matplotlib** to plot robot movements and destinations.
- Different colors represent different robot types.

## Execution Flow
- Continuously updates positions until all robots reach their destinations.
- Ensures efficient, collision-free navigation within the warehouse grid.
