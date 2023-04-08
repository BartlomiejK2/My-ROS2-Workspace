#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from my_robot_interfaces.msg import TurtleArray
from my_robot_interfaces.srv import CatchTurtle
from math import sqrt


class Turtle_Contoller_Node(Node):
    def __init__(self,name):
        super().__init__(name)

        self.K_x = 2.8;
        self.K_y = 2.8;
        self.K_t = 0.01;
        self.pose = Pose()
        self.twist = Twist()
        self.turtle_pose = Pose()
        self.turtle_array = TurtleArray()
        self.turtle_distance = []
        self.publisher_1 = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.subscriber_1 = self.create_subscription(Pose,"turtle1/pose",self.callback_pose,10)
        self.subscriber_2 = self.create_subscription(TurtleArray, "alive_turtles",  self.callback_alive,10)
        self.timer_ = self.create_timer(0.01,self.publish_value)
        self.get_logger().info("Turtle killer is active!")
    
    def publish_value(self):
        self.twist.linear.x = self.K_x*(self.turtle_pose.x  - self.pose.x)
        self.twist.linear.y = self.K_y*(self.turtle_pose.y - self.pose.y)
        self.twist.linear.z = 0.
        self.twist.angular.x = 0.
        self.twist.angular.y = 0.
        self.twist.angular.z = self.K_t*(self.turtle_pose.theta - self.pose.theta)
        self.publisher_1.publish(self.twist)
    
    def callback_pose(self,msg):
        self.pose = msg

    def callback_alive(self,msg):
        self.turtle_array = msg
        names = self.turtle_array.names
        pos_array = self.turtle_array.pos_array
        if not names:
            pass
        else: 
            for i in range(len(names)):
              turtle_distance = sqrt((pos_array[i].x - self.pose.x) * (pos_array[i].x - self.pose.x)
                                   + (pos_array[i].y - self.pose.y) * (pos_array[i].y - self.pose.y))
              if turtle_distance < 0.2:
                  self.call_catch_turtle_server(names[i])
              self.turtle_distance.append(turtle_distance)
              min_value = min(self.turtle_distance)
              min_index = self.turtle_distance.index(min_value)
              self.turtle_pose.x = pos_array[min_index].x
              self.turtle_pose.y = pos_array[min_index].y
              self.turtle_pose.theta = pos_array[min_index].theta
              
        
        
        
        self.turtle_distance.clear()




    def call_catch_turtle_server(self, name):
        self.client = self.create_client(CatchTurtle,"catch_turtle_service")
        while not self.client.wait_for_service(1.0):
           pass
        
        request = CatchTurtle.Request()
        request.name = name

        future = self.client.call_async(request)
        future.add_done_callback(self.callback_call_catch_turtle)

    
    def callback_call_catch_turtle(self, future):
        try:
            response = future.result()
            

        except Exception as e:
            self.get_logger().info("Service has error")
        
    



    



def main(args = None):
    rclpy.init(args = args)
    node  = Turtle_Contoller_Node("turtle_controller")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


