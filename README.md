# robotics-basic-grid-path-planning

Q. Design an efficient Warehouse Robot Management System where multiple types of robots (Humanoid, Quadrotor, and Driver) navigate a grid to reach their respective destinations while avoiding collisions.

#### Grid Initialization:
A square grid of size N x N is created.
A set number of robots (2*N) are randomly placed on the grid.
Robot Types & Properties:
Each robot belongs to one of three types: Humanoid, Quadrotor, or Driver.
Each robot has an initial and a destination position.

#### Movement Strategy:
Robots move towards their destinations using a step-wise movement:
First along the X-axis (horizontal movement).
Then along the Y-axis (vertical movement).
Euclidean distance is used to determine the shortest path.

#### Collision Avoidance Mechanism:
If two robots attempt to move to the same position, priority is given based on:
The robot closer to its destination continues moving.
If both robots are at the same distance, a randomized decision (coin toss) determines which one moves.

#### Decider Function (decider()):
Iterates through all robots and determines their next move.
Calls movement functions (move_x() or move_y()) to update positions.
Checks for collisions using collision_avoidance().
Updates the grid and plots the new robot positions.

#### Visualization:
A matplotlib plot shows the robots' movements and final destinations.
Different colors represent different robot types.

#### Execution Flow:
The system continuously updates positions in a loop until all robots reach their destinations.
This ensures an efficient and collision-free robot navigation system in the warehouse environment.
