import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue

from launch import LaunchDescription
from launch.substitutions import Command


def generate_launch_description():
    package = get_package_share_directory("marmotte_description")
    xacro_path = os.path.join(package, "urdf/marmotte.urdf.xacro")

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                parameters=[
                    {
                        "robot_description": ParameterValue(
                            Command(["xacro ", xacro_path]), value_type=str
                        )
                    }
                ],
            ),
        ]
    )
