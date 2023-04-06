from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    number_publisher_node = Node(
        package = "py_1_pkg",
        executable= "number_publisher",
        name = "amogus_1"
    )
    number_counter_node = Node(
        package= "py_1_pkg",
        executable= "number_counter",
        name = 'Ballz_1'
    )
    ld.add_action(number_publisher_node)
    ld.add_action(number_counter_node)
    return ld