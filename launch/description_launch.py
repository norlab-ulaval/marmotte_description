import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue


def generate_launch_description():
    package = get_package_share_directory("marmotte_description")
    xacro_path = os.path.join(package, "urdf/robot.urdf.xacro")

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
            Node(
                package="tf2_ros",
                executable="static_transform_publisher",
                name="static_transform_publisher",
                arguments=["-0.08", "0", "0.347", "0", "0", "0", "base_link", "arm_base_link"],
            ),
        ]
    )
