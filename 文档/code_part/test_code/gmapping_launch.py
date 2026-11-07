#!/usr/bin/env python3

import os
import launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='False')
    
    yaml_path = os.path.join(
        get_package_share_directory("slam_gmapping"),
        "params",
        "slam_gmapping.yaml"
    )

    return LaunchDescription([

        # 发布map到odom的静态变换
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='map_to_odom',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
            output='screen',
        ),

        # 发布odom到base_link的静态变换
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='odom_to_base_link',
            arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link'],
            output='screen',
        ),

        # 发布base_link到laser的静态变换
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_laser',
            arguments=['0', '0', '0.2', '0', '0', '0', 'base_link', 'laser'],
            output='screen',
        ),

        Node(
            package='slam_gmapping',
            executable='slam_gmapping',
            parameters=[{
                'map_frame': 'map',
                'odom_frame': 'odom',
                'base_frame': 'base_link',
                'laser_frame': 'laser',
                'use_sim_time': use_sim_time,
                },
                yaml_path
                ],
            output='screen',
        ),
        
    ])