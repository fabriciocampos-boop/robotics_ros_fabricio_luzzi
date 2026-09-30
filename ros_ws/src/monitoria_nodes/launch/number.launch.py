#!/usr/bin/python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='monitoria_nodes',
            executable='process_number_node.py',
        ),
        Node(
            package='monitoria_nodes',
            executable='div_number_node.py',
        ),
        Node(
            package='monitoria_nodes',
            executable='div_number_node.py',
        ),
    ])

