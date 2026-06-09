#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class BatteryNode(Node):

    def __init__(self):
        super().__init__('battery_node')

        self.publisher_ = self.create_publisher(
            Float32,
            '/battery_status',
            10)

        self.timer = self.create_timer(
            2.0,
            self.publish_battery)

    def publish_battery(self):
        msg = Float32()

        msg.data = random.uniform(20.0, 100.0)

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Battery: {msg.data:.2f}%')


def main(args=None):
    rclpy.init(args=args)

    node = BatteryNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
