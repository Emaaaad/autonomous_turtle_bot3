import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import String 
from std_msgs.msg import Header
import numpy as np



class Occupancy_grid_Pub(Node):
    def __init__(self):
        super().__init__('occupancy_grid_pub_node')
        self.grid_publisher_ = self.create_publisher(OccupancyGrid, 'map', 10)
        self.timer = self.create_timer(0.5, self.og_pub_callback)
        self.get_logger().info("Occupancy Grid Publisher Node Initialized")

    def og_pub_callback(self):
        # Create OccupancyGrid message
        occupancy_grid_msg = OccupancyGrid()
        
        # Set header
        occupancy_grid_msg.header = Header()
        occupancy_grid_msg.header.stamp = self.get_clock().now().to_msg()
        occupancy_grid_msg.header.frame_id = "map_frame"

        # Set grid metadata
        occupancy_grid_msg.info.resolution = 1.0  # 1 meter per cell
        occupancy_grid_msg.info.width = 2  # 2x2 grid
        occupancy_grid_msg.info.height = 2

        occupancy_grid_msg.info.origin.position.x = 0.0
        occupancy_grid_msg.info.origin.position.y = 0.0
        occupancy_grid_msg.info.origin.position.z = 0.0

        # Grid data
        array = np.array([1, 1, 1, 1], dtype=np.int8)  # Example grid values
        occupancy_grid_msg.data = array.tolist()

        # Publish the message
        self.grid_publisher_.publish(occupancy_grid_msg)
        self.get_logger().info("Published Occupancy Grid Message")


def main(args=None):
    rclpy.init(args=args)
    occupancy_grid_publisher = Occupancy_grid_Pub()
    rclpy.spin(occupancy_grid_publisher)
    occupancy_grid_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()