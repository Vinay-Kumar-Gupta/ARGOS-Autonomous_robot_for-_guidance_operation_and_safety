# This is a Publisher Module for publishing goal_pose 
# This Can be imported and used as a function directly by passing the argument
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class GoalPosePublisher(Node):

    def __init__(self):
        super().__init__('goal_pose_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, '/goal_pose', 10)

        # Dictionary storing room names and their coordinates (x, y)
        self.room_coordinates = {
            'room305': (8.0, -0.7),
            'room311': (0.6, -4.8),
            'room303': (5.1, 6.3)
        }

    def post_goal(self, room_name):
        if room_name in self.room_coordinates:
            x, y = self.room_coordinates[room_name]

            msg = PoseStamped()

            # Set the current time in the header
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'map'

            # Set the position in the PoseStamped message
            msg.pose.position.x = x
            msg.pose.position.y = y
            msg.pose.position.z = 0.0

            # Set a default orientation (quaternion)
            msg.pose.orientation.x = 0.0
            msg.pose.orientation.y = 0.0
            msg.pose.orientation.z = 0.0
            msg.pose.orientation.w = 1.0

            # Publish the message
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published goal pose for {room_name} - x: {x}, y: {y}')
            # rclpy.shutdown()  # Exit the code after publishing
        else:
            self.get_logger().error(f'Room name {room_name} not found!')

# def main(args=None):
#     rclpy.init(args=args)
#     node = GoalPosePublisher()
    
#     # Example of publishing a goal pose
#     node.post_goal('room301')  # You can change the room name as needed

# if __name__ == '__main__':
#     main()
