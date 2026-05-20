#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        # GPS 驱动
        Node(
            package="gps_driver",
            executable="gps_node",
            name="gps_node",
            output="screen",
        ),

        # IMU 驱动
        Node(
            package="imu_driver",
            executable="imu_node",
            name="imu_node",
            output="screen",
        ),

        # 串口数传
        Node(
            package="ros2_serial_bridge",
            executable="serial_bridge_node",
            name="serial_bridge_node",
            output="screen",
        ),

        # 数据融合（完整版：YAW + PITCH）
        Node(
            package="ros2_data_fusion",
            executable="data_fusion_node",
            name="data_fusion_node",
            output="screen",
        ),

        # 转台控制（完整版：YAW + PITCH）
        Node(
            package="sciroad1",
            executable="turntable_control_node",
            name="turntable_control_node",
            output="screen",
        ),
    ])

