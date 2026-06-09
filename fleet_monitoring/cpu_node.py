#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

class CpuNode(Node):

    def __init__(self):
        super().__init__('cpu_node')

        self.publisher_ = self.create_publisher(
            Float32,
            '/cpu_usage',
            10)

        self.timer = self.create_timer(
            2.0,
            self.publish_cpu)

    def publish_cpu(self):
        msg = Float32()

        msg.data = psutil.cpu_percent()

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'CPU Usage: {msg.data}%')


def main(args=None):
    rclpy.init(args=args)

    node = CpuNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()