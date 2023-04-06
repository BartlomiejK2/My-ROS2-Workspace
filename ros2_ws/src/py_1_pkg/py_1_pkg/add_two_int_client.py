#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Add_Two_Ints_Client_Node(Node):
    def __init__(self,name):
        super().__init__(name)
        self.call_add_two_ints_server(7,3)
        self.call_add_two_ints_server(7,3)

    def call_add_two_ints_server(self, a, b):
        self.client = self.create_client(AddTwoInts,"add_two_ints")
        while not self.client.wait_for_service(1.0):
            self.get_logger().info("Waiting for server Add_Two_Ints :(")
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = self.client.call_async(request)
        future.add_done_callback(self.callback_call_add_two_ints)

    
    def callback_call_add_two_ints(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().info("Service has error")



def main(args = None):
    rclpy.init(args = args)
    node  = Add_Two_Ints_Client_Node("add_two_ints_client")
    rclpy.spin(node)
    rclpy.shutdown()
