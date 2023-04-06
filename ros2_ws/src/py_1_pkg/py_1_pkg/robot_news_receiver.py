#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from example_interfaces.msg import String

class Robot_News_Receiver_Node(Node):
    def __init__(self,name):
        super().__init__(name)
        self.subscriber = self.create_subscription(
            String,"robot_news",self.callback_rebot_news, 10)
        self.get_logger().info("Receiver activated!!!")

    def callback_rebot_news(self, msg):
        self.get_logger().info(msg.data)





def main(args = None):
    rclpy.init(args = args)
    node  = Robot_News_Receiver_Node("robot_news_receiver")
    rclpy.spin(node)
    rclpy.shutdown()





if __name__ == '__main__':
    main()