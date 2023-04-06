#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool
class Robot_News_Receiver_Node(Node):
    def __init__(self,name):
        super().__init__(name)
        self.counted_value = 0
        self.subscriber = self.create_subscription(
            Int64,"number",self.callback_counter, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.server = self.create_service(SetBool,"reset_counter",self.server_callback)
        self.get_logger().info("Number counter is launched!")

    def callback_counter(self, msg_in):
        self.counted_value += msg_in.data
        self.get_logger().info(str(self.counted_value))
        msg_out = Int64()
        msg_out.data = self.counted_value
        self.publisher_.publish(msg_out)
    
    

    def server_callback(self, request, response):
        if(request.data == True):
            self.counted_value = 0
            response.success = True
            response.message = "Counter have been reset"
            self.get_logger().info(response.message)
        else:
            pass
            response.success = False
            response.message = "Counter have not been reset"
        return response




def main(args = None):
    rclpy.init(args = args)
    node  = Robot_News_Receiver_Node("number_counter")
    rclpy.spin(node)
    rclpy.shutdown()





if __name__ == '__main__':
    main()