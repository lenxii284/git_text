from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command,LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    model_path=DeclareLaunchArgument(
        name='model',default_value=
         os.path.join(get_package_share_directory
                     ("moxing"),"urdf","first.urdf.xacro"),
        description="URDF文件路径"
                     )
    robot_description=ParameterValue(Command(["xacro ",LaunchConfiguration("model")]))
    
    joint_state_publisher_gui = Node(
    package="joint_state_publisher_gui",
    executable="joint_state_publisher_gui",
    parameters=[{"robot_description": robot_description}],  # 直接传递参数
)
    robot_state_publisher = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    parameters=[{"robot_description": robot_description}],
    output="screen",  # 可选：打印调试信息
)

    rviz2_node=Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",

    )

    return LaunchDescription(
        [
             DeclareLaunchArgument(
        "use_sim_time",
        default_value="false",
        description="Use simulation (Gazebo) clock if true",
    ),
            model_path,
            robot_state_publisher,
            joint_state_publisher_gui,
            rviz2_node,

        ]
    )
