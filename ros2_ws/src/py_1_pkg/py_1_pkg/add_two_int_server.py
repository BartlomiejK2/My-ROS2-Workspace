#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from example_interfaces.srv import AddTwoInts

class Add_Two_Ints_Server_Node(Node):
    def __init__(self,name):
        super().__init__(name)
        self.counter = 0
        self.server = self.create_service(AddTwoInts,"add_two_ints",self.server_callback)
        self.get_logger().info("Server is launched!")
    

    def server_callback(self, request, response):
        self.counter += 1
        response.sum = request.a + request.b
        self.get_logger().info(str(self.counter))
        self.get_logger().info(str(request.a) + " + "  + str(request.b) + " = " + str(response.sum))
        return response



def main(args = None):
    rclpy.init(args = args)
    node  = Add_Two_Ints_Server_Node("add_two_ints_server")
    rclpy.spin(node)
    rclpy.shutdown()





if __name__ == '__main__':
    main()