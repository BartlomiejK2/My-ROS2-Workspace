#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from led_interfaces.srv import SetLed
from led_interfaces.msg import LedPanelState

class Led_Panel_Node(Node):
    def __init__(self,name):
        super().__init__(name)
        self.server = self.create_service(SetLed, "set_led", self.server_callback)
        self.publisher_ = self.create_publisher(LedPanelState, "led_panel_state", 10)
        self.get_logger().info("Led Panel is working!")
    

    def server_callback(self, request, response):
        LedState = LedPanelState()
        if request.led_number == 1:
            LedState.led_1 = True
            LedState.led_2 = False
            LedState.led_3 = False
        elif request.led_number == 2:
            LedState.led_1 = False
            LedState.led_2 = True
            LedState.led_3 = False
        elif request.led_number == 3:
            LedState.led_1 = False
            LedState.led_2 = False
            LedState.led_3 = True

        response.success = True

        if request.state == "off":
            led_state = "on"

        else:
            led_state = "off"
        

        self.publisher_.publish(LedState)
        self.get_logger().info("Led " + str(request.led_number) + " is " + led_state) 
        return response



def main(args = None):
    rclpy.init(args = args)
    node  = Led_Panel_Node("led_panel")
    rclpy.spin(node)
    rclpy.shutdown()





if __name__ == '__main__':
    main()