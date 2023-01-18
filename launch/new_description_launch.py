import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue

def generate_launch_description():

    params = {
        "arm": "gen3", #Not use
        "dof": "7", #Not use
        "vision": "true", #Not use
        "sim": "false", #Not use
        "gripper": "robotiq_2f_85", #Not use
        "start_rviz": "false" #Not use
    }

    package = get_package_share_directory("marmotte_description")
    xacro_path = os.path.join(package, "new_urdf_01-16-2023/urdf/marmotte.urdf.xacro")

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{"robot_description": ParameterValue(Command(["xacro ",xacro_path]), value_type=str)
                        #  "dof": params["dof"],
                        #  "vision": params["vision"],
                        #  "sim": params["sim"]
                         }]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        )
    ])