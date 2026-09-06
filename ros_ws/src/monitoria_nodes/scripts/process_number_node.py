#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ProcessNode(Node):
    def __init__(self):
        super().__init__("process_number_node")
        self.publisher = self.create_publisher(Float64, "result", 10)

        self.subscriber = self.create_subscription(Float64, "input", self.callback, 10)

    def callback(self, msg:Float64):
        temp_msg = Float64()
        temp_msg.data = msg.data * 2
        self.publisher.publish(temp_msg)
        
def main():
    rclpy.init()
    node = ProcessNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()