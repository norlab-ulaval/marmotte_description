import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node


def generate_launch_description():

    xacro_path = os.path.join(get_package_share_directory("marmotte_description"), "urdf/marmotte.urdf.xacro")

    return LaunchDescription([
        # DeclareLaunchArgument('xacro_ath', default_value=None, ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{"robot_description": Command(['xacro', ' ', xacro_path])}]),
    ])
