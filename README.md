# Autonomous TurtleBot3 Navigation

This project implements **autonomous navigation** for the TurtleBot3 in a simulated **maze environment** using ROS 2. It includes **SLAM mapping**, **path planning**, and **goal-based navigation** using Nav2.

## Installation & Build

Clone the repository:
```bash
git clone https://github.com/Emaaaad/autonomous_turtle_bot3.git
cd autonomous_turtle_bot3
```
### Install dependencies:
```bash
sudo apt update && rosdep install --from-paths src --ignore-src -r -y
```
### Build the package:
```bash
colcon build
source install/setup.bash
```
### Running the Simulation
Launch Gazebo & SLAM:
```bash
ros2 launch autonomous_tb3 maze_navigation.launch.py
```
Save the map (after exploration):
```bash
ros2 run nav2_map_server map_saver_cli -f <path_to_save>
```
Run autonomous navigation:
```bash
ros2 run autonomous_tb3 maze_solver
```

Notes:
    -  The robot starts at (-9, 8) in the maze.
    -  The project supports both Google Cartographer and SLAM Toolbox for mapping you have to choose between them. 
    -  If the robot spawns in the wrong location, restart Gazebo.
