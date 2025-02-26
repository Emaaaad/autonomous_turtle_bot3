#! /usr/bin/env python3
'''
This is a Python script that uses the nav2_simple_commander package to navigate a robot
through a sequence of pre-defined poses in a ROS 2 environment. The BasicNavigator class
is used to control the robot's movement, and the PoseStamped class is used to represent each goal pose.
The setInitialPose() method is used to set the robot's initial position, and goThroughPoses() is used to navigate
the robot through the sequence of goals.
 The script waits for the task to complete before printing the result and shutting down the navigator.
'''
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

def main():
    rclpy.init()
    goals=[]
    navigator = BasicNavigator()
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x =-8.9765
    initial_pose.pose.position.y =8.1152
    initial_pose.pose.orientation.z =0.0
    initial_pose.pose.orientation.w =1.0
    navigator.setInitialPose(initial_pose)

    navigator.waitUntilNav2Active()

    print("Goals List:")
    for i, g in enumerate(goals):
     print(f"Goal {i+1}: x={g.pose.position.x}, y={g.pose.position.y}")


    # Go to our demos final goal pose
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x =8.3832
    goal_pose.pose.position.y =-9.0362
    goal_pose.pose.orientation.w =1.0
    goals.append(goal_pose)

    navigator.goThroughPoses(goals)
    while not navigator.isTaskComplete():
        pass


    # Do something depending on the return code
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    navigator.lifecycleShutdown()

    exit(0)


if __name__ == '__main__':
    main()