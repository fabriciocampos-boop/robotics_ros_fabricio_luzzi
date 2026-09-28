import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    config_area = os.path.join(
        get_package_share_directory('meu_bringup'),
        'config',
        'area_params.yaml'
    )
    config_volume = os.path.join(
        get_package_share_directory('meu_bringup'),
        'config',
        'volume_params.yaml'
    )

    node_cylinder_area = Node(
        package='cylinder_area',
        executable='cylinder_area_node',
        parameters=[config_area]
    )
    node_cylinder_volume = Node(
        package='cylinder_volume',
        executable='cylinder_volume_node',
        parameters=[config_volume]
    )

    return LaunchDescription([
        node_cylinder_area, node_cylinder_volume
    ])