#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

from utils.cmdIO import TrackingConfig
from utils.sampling.base_sampling import SamplePitchand200RotationBase


class TurntableControlYawNode(Node):
    """
    仅Yaw轴转台控制节点（稳定优化版）
    订阅 /track/gimbal_cmd:
        msg.x -> yaw 角速度 deg/s
        msg.y -> 忽略
        msg.z -> 忽略
    控制：固定50Hz周期，相对角度步进控制
    """

    def __init__(self):
        super().__init__('turntable_control_yaw_node')

        # ========= 初始化转台 =========
        config = TrackingConfig()
        args = config.args
        self.gimbal = SamplePitchand200RotationBase(args)
        self.init_gimbal()

        # ========= 控制参数 =========
        self.acc = 6.0
        self.dec = 6.0
        self.vel = 10.0
        self.vel_limit_yaw = 10.0
        self.control_dt = 0.2  # 50Hz 正确周期
        self.min_step_yaw_deg = 0.2
        self.set_motion_param()

        # ========= 指令缓存 =========
        self.target_yaw_vel = 0.0

        # ========= 50Hz 固定定时器控制 =========
        self.control_timer = self.create_timer(self.control_dt, self.control_loop)

        # ========= 订阅指令 =========
        self.create_subscription(
            Vector3,
            '/track/gimbal_cmd',
            self.cmd_callback,
            10
        )

        self.last_print_time = time.time()
        self.get_logger().info('✅ turntable_control_yaw_node 启动成功（仅Yaw控制 | 50Hz）')

    def init_gimbal(self):
        """Yaw回零，Pitch不动"""
        self.get_logger().info('正在回零...')
        try:
            self.gimbal.pan200.set_zero()
            self.get_logger().info('✅ Yaw回零完成')
        except Exception as e:
            self.get_logger().error(f'❌ 回零失败：{str(e)}')

    def set_motion_param(self):
        self.gimbal.pan200.set_acc_dec_v(self.acc, self.dec, self.vel)

    def cmd_callback(self, msg: Vector3):
        """仅保存最新指令"""
        self.target_yaw_vel = float(msg.x)

    def control_loop(self):
        """50Hz固定控制主循环"""
        try:
            # 限速
            yaw_vel = max(min(self.target_yaw_vel, self.vel_limit_yaw), -self.vel_limit_yaw)

            # 计算步进
            dyaw = yaw_vel * self.control_dt

            # 最小位移过滤（防抖）
            if abs(dyaw) >= self.min_step_yaw_deg:
                self.gimbal.pan200.p_rel(dyaw)

            # 定时打印日志
            now = time.time()
            if now - self.last_print_time >= 1.0:
                self.get_logger().info(f'速度: {yaw_vel:5.1f}°/s | 步进: dyaw={dyaw:5.2f}°')
                self.last_print_time = now

        except Exception as e:
            self.get_logger().error(f'❌ 控制异常：{str(e)}')


def main():
    rclpy.init()
    node = TurntableControlYawNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('🛑 节点已关闭')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

