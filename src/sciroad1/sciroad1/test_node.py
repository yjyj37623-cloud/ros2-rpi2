#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time

from utils.cmdIO import TrackingConfig
from utils.sampling.base_sampling import SamplePitchand200RotationBase


class GimbalTestNode(Node):
    def __init__(self):
        super().__init__('gimbal_test_node')
        self.get_logger().info("✅ 测试：0→20 加速 → 匀速10秒 → 20→0减速")

        # 初始化转台
        config = TrackingConfig()
        args = config.args
        self.gimbal = SamplePitchand200RotationBase(args)

        # 回零
        self.get_logger().info("pan200 回零...")
        self.gimbal.pan200.set_zero()
        self.gimbal.pan200.p_rel(10) 


def main():
    rclpy.init()
    node = GimbalTestNode()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

