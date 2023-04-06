#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from example_interfaces.msg import String
from my_robot_interfaces.msg import HardwareStatus

class Robot_News_Station_Node(Node):
    def __init__(self,name):
        super().__init__(name)

        self.publisher_ = self.create_publisher(HardwareStatus, "robot_news", 10)
        self.timer_ = self.create_timer(0.5,self.publish_news)
        self.get_logger().info("Robot Station is starting:")

    def publish_news(self):
        msg = HardwareStatus()
        msg.temperature = 10
        msg.are_motors_ready = True
        msg.debug_message = "Yo"
        self.publisher_.publish(msg)   



def main(args = None):
    rclpy.init(args = args)
    node  = Robot_News_Station_Node("robot_news_station")
    rclpy.spin(node)
    rclpy.shutdown()





if __name__ == '__main__':
    main()