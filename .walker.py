import rclpy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from rclpy.node import Node
import time

class Communication(Node):
    def __init__(self):
        super().__init__('communication')
        self.pub1 = self.create_publisher(Twist, 'Odin/twist_mux/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, 'Odin/joy_priority', 1)
        self.sub = self.create_subscription(Twist, 'Loki/muli_cmd_vel', self.communication_callback, 10)
        self.sub2 = self.create_subscription(Bool, 'Loki/joy_priority', self.lock_callback, 1)

        
        self.sub #prevent unused vairable warning
        self.sub2

    def communication_callback(self, msg):
        linear_x = msg.linear.x
        linear_y = msg.linear.y 
        linear_z = msg.linear.z 
        angular_x = msg.angular.x
        angular_y = msg.angular.y 
        angular_z = msg.angular.z

        twist_msg = Twist()

        if not linear_x == 0:
            print("Received Commands")

        elif not linear_y == 0:
            print("Received Commands")

        elif not linear_z == 0:
            print("Received Commands")
        
        elif not angular_x == 0:
            print("Received Commands")
        
        elif not angular_y == 0:
            print("Received Commands")
        
        elif not angular_z == 0:
            print("Received Commands")
        
        twist_msg.linear.x = linear_x
        twist_msg.linear.y = linear_y
        twist_msg.linear.z = linear_z
        twist_msg.angular.x = angular_x
        twist_msg.angular.y = angular_y
        twist_msg.angular.z = angular_z

        # time.sleep(2)
        

        self.pub1.publish(twist_msg)

    def lock_callback(self, msg):
        lock = msg.bool
        pub2.publish.bool = lock


def main(args=None):
    rclpy.init(args=args)

    communication = Communication()

    rclpy.spin(communication)

    rclpy.shutdown()

if __name__ == '__main__':
    main()

        



