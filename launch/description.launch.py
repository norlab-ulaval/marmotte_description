import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue

from launch import LaunchDescription
from launch.substitutions import Command


def generate_launch_description():
    share_folder = get_package_share_directory("marmotte_description")
    config_file = os.path.join(share_folder, "urdf/marmotte.urdf.xacro")
    
    description_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        parameters=[{
                "robot_description": ParameterValue(
                    Command(["xacro ", config_file]), value_type=str
                )
        }],
    )
    return LaunchDescription([
            description_node
        ])
