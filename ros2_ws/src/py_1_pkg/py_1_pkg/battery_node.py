#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from led_interfaces.srv import SetLed
from functools import partial
from time import sleep

class Battery_Node(Node):
    def __init__(self,name):
        super().__init__(name)
        while True:
            self.call_led_panel_server(1,"off")
            sleep(4)
            self.call_led_panel_server(1,"on")
            sleep(6)

    def call_led_panel_server(self, number, battery_state):
        self.client = self.create_client(SetLed, "set_led")
        while not self.client.wait_for_service(1.0):
            self.get_logger().info("Waiting for Led Panel")
        
        request = SetLed.Request()
        request.led_number = number
        request.state = battery_state

        future = self.client.call_async(request)
        future.add_done_callback(partial(
            self.callback_call_add_two_ints,number= number, battery_state= battery_state))

    
    def callback_call_add_two_ints(self, future, number, battery_state):
        try:
            response = future.result()
            self.get_logger().info("Operation success")
        except Exception as e:
            self.get_logger().info("Service has error")



def main(args = None):
    rclpy.init(args = args)
    node  = Battery_Node("battery")
    rclpy.spin(node)
    rclpy.shutdown()