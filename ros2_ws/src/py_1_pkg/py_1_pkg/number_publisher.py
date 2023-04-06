#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from example_interfaces.msg import Int64

class Number_publisher_Node(Node):
    def __init__(self,name):
        super().__init__(name)
        self.declare_parameter("number_to_publish", 1)
        self.value = self.get_parameter("number_to_publish").value
        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(1,self.publish_value)
        self.get_logger().info("Number publisher is starting!")
    
    def publish_value(self):
        msg = Int64()
        msg.data = self.value
        self.publisher_.publish(msg)




def main(args = None):
    rclpy.init(args = args)
    node  = Number_publisher_Node("number_publisher")
    rclpy.spin(node)
    rclpy.shutdown()





if __name__ == '__main__':
    main()