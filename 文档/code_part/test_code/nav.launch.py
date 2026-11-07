import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node

def generate_launch_description():
    # 获取包路径
    nav2_str = get_package_share_directory('daohang')
    nav2_bringup_str = get_package_share_directory('nav2_bringup')
    rviz_str = os.path.join(nav2_bringup_str, 'rviz', 'nav2_default_view.rviz')

    
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    map_path = LaunchConfiguration('map', default=os.path.join(nav2_str, 'map', 'room.yaml'))
    nav2_params_path = LaunchConfiguration('params_file', default=os.path.join(nav2_str, 'config', 'nav2_params.yaml'))
    
    static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value=use_sim_time, ), 
        DeclareLaunchArgument('map', default_value=map_path,
                             description='地图文件路径'),
        DeclareLaunchArgument('params_file', default_value=nav2_params_path,
                             description='Nav2参数文件路径'),
   
        static_tf,

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup_str, 'launch', 'bringup_launch.py')
            ),
            launch_arguments={
                'map': map_path,
                'use_sim_time': use_sim_time,
                'params_file': nav2_params_path}.items(),
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d',rviz_str],
            parameters=[{'use_sim_time': use_sim_time}],  # 直接传递布尔值
            output='screen'
            ),
    ])