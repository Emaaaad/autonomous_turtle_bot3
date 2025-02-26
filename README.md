# Autonomous TurtleBot3 Navigation

In this project we implement **autonomous navigation** for the TurtleBot3 in a simulated **maze environment** using ROS 2. It includes **SLAM mapping**, **path planning**, and **goal-based navigation** using Nav2.

## Demo Video
🎥 [Click here to watch the demo](https://github.com/Emaaaad/autonomous_turtle_bot3/blob/main/Demo.mp4)


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
## Notes

- The robot starts at **(-9, 8)** in the maze.
- The project supports both **Google Cartographer** and **SLAM Toolbox** for mapping. You have to **choose one** before running.
- If the robot spawns in the wrong location, restart Gazebo.
- To reset the map and start fresh, delete the previous map files before launching SLAM.
- If you experience localization issues, check that `/map` and `/tf` topics are being published.
- Always source the workspace before running commands:
  ```bash
  source install/setup.bash
  ```
- If the robot is not moving, check that Nav2 is active and the goal is correctly set.
