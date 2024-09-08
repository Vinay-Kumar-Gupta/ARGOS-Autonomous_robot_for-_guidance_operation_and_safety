# This function will be used for publishing various topics for controlling the robot
# you can directly import this module and use the functions

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class GoalPosePublisher(Node):

    def __init__(self):
        super().__init__('goal_pose_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, '/goal_pose', 10)


        # Dictionary storing room names and their coordinates (x, y)

        self.room_coordinates = { 'room_305': (4.9, 3.6),    'room_306': (12.8, 3.38),    'room_307': (18.5, 4.3), 
                                  'room_308': (27.0, 3.1),   'room_309': (32.9, 3.6),     'room_310': (39.25, 3.61), 
                                  'room_311': (38.8, -5.9),  'room_312': (32.49, -6.72),  'room_313': (25.41, -5.81), 
                                  'room_314': (19.91,-6.03), 'room_315': (10.96, -7.09),  'room_316': (6.03,-6.55) }
        
 # ================================== GOAL POSE PUBLISHER ==================================

    def publish_goal_pose(self, room_name):
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
    
    def publish_cmd_vel():
        pass

    def Tour_Mode():
        pass

    def Emergency_Mode():
        pass
    
# def main(args=None):
#     rclpy.init(args=args)
#     node = GoalPosePublisher()
    
#     # Example of publishing a goal pose
#     node.post_goal('room301')  # You can change the room name as needed

# if __name__ == '__main__':
#     main()
