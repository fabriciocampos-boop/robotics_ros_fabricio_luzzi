from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    node_cylinder_area = Node(
        package='cylinder_area',
        executable='cylinder_area_node' 
    )
    node_cylinder_volume = Node(
        package='cylinder_volume',
        executable='cylinder_volume_node'
    )

    return LaunchDescription([
        node_cylinder_area, node_cylinder_volume
    ])
