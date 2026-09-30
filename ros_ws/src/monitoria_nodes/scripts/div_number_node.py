#!/usr/bin/python3

import rclpy
from std_msgs.msg import Float64
from rclpy.node import Node


class DivNumberNode(Node):
    def __init__(self):
        super().__init__("div_node")
        self.publisher = self.create_publisher(Float64, "div_number", 10)
        self.subscriber = self.create_subscription(Float64, "input", self.sub_callback, 10)

    def sub_callback(self, msg:Float64):
        self.get_logger().info(f"Número recebido: {msg.data}")
        process_number = Float64()
        process_number.data = (msg.data)/2.0
        self.publisher.publish(process_number)

def main():
    rclpy.init()
    no = DivNumberNode()
    rclpy.spin(no)
    no.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()






