#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from turtlesim.srv import Kill
from turtlesim.srv import Spawn
from my_robot_interfaces.srv import CatchTurtle
from my_robot_interfaces.msg import TurtleArray
from turtlesim.msg import Pose
from random import random
from math import pi

class Turtle_Spawner_Node(Node):
    def __init__(self,name):
        super().__init__(name)
        self.turtle_index = 1
        self.turtle_names = []
        self.turtle_pos_array = []
        self.publisher_1 = self.create_publisher(TurtleArray, "alive_turtles", 10)
        self.server_1 = self.create_service(CatchTurtle, "catch_turtle_service", self.server_callback)
        self.timer_1= self.create_timer(2,self.create_turtle)
        self.timer_2 = self.create_timer(0.01,self.publish_value)
        self.get_logger().info("Turtle Spawner is working!")
    
    def publish_value(self):
        msg = TurtleArray()
        msg.names = self.turtle_names
        msg.pos_array = self.turtle_pos_array
        self.publisher_1.publish(msg)
    
    def create_turtle(self):
        self.turtle_index += 1
        name = "turtle" + str(self.turtle_index)
        position = Pose()
        position.x = random()*(9.0)
        position.y = random()*(9.0)
        position.theta = random()*(pi)
        position.linear_velocity = 0.
        position.angular_velocity = 0.
        self.turtle_names.append(name)
        self.turtle_pos_array.append(position)
        self.spawn_turtle(position.x, position.y, position.theta, name)
        
    def server_callback(self, request, response):
        if request.name in self.turtle_names:
            response.success = True
            del_index = self.turtle_names.index(request.name)
            self.turtle_names.pop(del_index)
            self.turtle_pos_array.pop(del_index)
            self.kill_turtle(request.name)
        else:
            response.success = False
        
        return response
        
    def spawn_turtle(self, x, y, theta, name):
        self.client_1 = self.create_client(Spawn,"spawn")
        while not self.client_1.wait_for_service(1.0):
            pass
        
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = name

        future = self.client_1.call_async(request)
        future.add_done_callback(self.callback_spawn_turtle)

    
    def callback_spawn_turtle(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().info("Service has error")
    
    def kill_turtle(self, name):
        self.client_2 = self.create_client(Kill,"kill")
        while not self.client_2.wait_for_service(1.0):
            pass
        
        request = Kill.Request()
        request.name = name

        future = self.client_2.call_async(request)
        

    
    






def main(args = None):
    rclpy.init(args = args)
    node  = Turtle_Spawner_Node("turtle_spawner")
    rclpy.spin(node)
    rclpy.shutdown()





if __name__ == '__main__':
    main()