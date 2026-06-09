#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TemperatureNode(Node):

    def __init__(self):
        super().__init__('temperature_node')

        self.publisher_ = self.create_publisher(
            Float32,
            '/temperature',
            10)

        self.timer = self.create_timer(
            2.0,
            self.publish_temperature)

    def publish_temperature(self):
        msg = Float32()

        msg.data = random.uniform(40.0, 90.0)

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Temperature: {msg.data:.2f} C')


def main(args=None):
    rclpy.init(args=args)

    node = TemperatureNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()