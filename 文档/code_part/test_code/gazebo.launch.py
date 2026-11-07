from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory
import  launch
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros
from launch.actions import SetEnvironmentVariable


def generate_launch_description():
    model_path=DeclareLaunchArgument(
        name="model",
        default_value=os.path.join(
            get_package_share_directory("moxing"),
            "urdf",
            "second.urdf.xacro"
        ),
        description="URDF 文件路径",
    )

    default_world_path=os.path.join(
        get_package_share_directory("moxing"),
        "world",
        "room1.world")
    
    gazebo_launch=launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory(
            "gazebo_ros"),'/launch','/gazebo.launch.py']
        ),
        launch_arguments=[('world',default_world_path),('verbose','true')]
    )

    spawn_action=launch_ros.actions.Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=['-topic','/robot_description',
                   '-entity','robot1']
    )

    robot_description = ParameterValue(
        Command(["xacro ",LaunchConfiguration("model")]),
        value_type=str
    )


    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
         "source_list": ["/joint_states"],  # 确保订阅 Gazebo 的关节数据
        "robot_description": robot_description
    }],
        output="screen",
    )

    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
    )

    # rviz2_node = Node(
    #     package="rviz2",
    #     executable="rviz2",
    #     name="rviz2",
    #     output="screen",
    #     arguments=['-d',os.path.join(
    #         get_package_share_directory("moxing"),
    #         'rviz','model.rviz'
    #     )]
    # )

    return launch.LaunchDescription([
        SetEnvironmentVariable(name="IGN_GPU_VENDOR", value="nvidia"),  # 强制 Ignition 用 NVIDIA
        SetEnvironmentVariable(name="GAZEBO_GPU_VENDOR", value="nvidia"),  # Gazebo 用 NVIDIA
        model_path,
        robot_state_publisher,
        joint_state_publisher,  # 替换为 GUI 版本
        
        gazebo_launch,
        spawn_action,
    ])