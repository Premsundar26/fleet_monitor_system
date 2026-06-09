
#!/usr/bin/env python3

import sqlite3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class FleetMonitor(Node):

    def __init__(self):
        super().__init__('fleet_monitor')

        self.battery = 0.0
        self.temperature = 0.0
        self.cpu = 0.0

        self.create_subscription(
            Float32,
            '/battery_status',
            self.battery_callback,
            10)

        self.create_subscription(
            Float32,
            '/temperature',
            self.temperature_callback,
            10)

        self.create_subscription(
            Float32,
            '/cpu_usage',
            self.cpu_callback,
            10)

        self.conn = sqlite3.connect(
            'health.db')

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS health(
            battery REAL,
            temperature REAL,
            cpu REAL
        )
        """)

        self.timer = self.create_timer(
            5.0,
            self.store_data)

    def battery_callback(self, msg):
        self.battery = msg.data

    def temperature_callback(self, msg):
        self.temperature = msg.data

    def cpu_callback(self, msg):
        self.cpu = msg.data

    def store_data(self):

        self.cursor.execute(
            """
            INSERT INTO health
            VALUES (?, ?, ?)
            """,
            (
                self.battery,
                self.temperature,
                self.cpu
            )
        )

        self.conn.commit()

        self.get_logger().info(
            f"""
Battery: {self.battery:.2f}%
Temperature: {self.temperature:.2f} C
CPU: {self.cpu:.2f}%
"""
        )

        if self.battery < 25:
            self.get_logger().warn(
                "LOW BATTERY ALERT")

        if self.temperature > 80:
            self.get_logger().warn(
                "HIGH TEMPERATURE ALERT")

        if self.cpu > 90:
            self.get_logger().warn(
                "HIGH CPU ALERT")


def main(args=None):

    rclpy.init(args=args)

    node = FleetMonitor()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()