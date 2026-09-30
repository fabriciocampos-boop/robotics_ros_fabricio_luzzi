import rclpy
from rclpy.node import Node
from robot_interfaces.msg import LaserData
import random
import math

class Laser(Node):
    def __init__(self):
        super().__init__("laser_publisher")
        
        self.publisher_ = self.create_publisher(LaserData, "/scan_data", 10)
        self.timer_ = self.create_timer(10.0, self.publish_scan) 
        self.subscriber_ = self.create_subscription(LaserData, "/scan_data", self.callback, 10)

    def publish_scan(self):
        msg = LaserData()
        msg.angle_min = 0.0
        msg.angle_max = math.pi

        msg.angle_increment = math.pi / 9 
        msg.ranges = [round(random.uniform(0.2, 5.0), 2) for _ in range(10)]


        self.publisher_.publish(msg)
        self.get_logger().info(f"Publicado: {[round(r, 2) for r in msg.ranges]}\n")

    def callback(self, msg : LaserData):
        menor_distancia = min(msg.ranges)
        indice = msg.ranges.index(menor_distancia)
        angulo = msg.angle_min + indice * msg.angle_increment

        self.get_logger().info(
            f"Menor distância: {menor_distancia:.2f} m (no ângulo {angulo:.2f} rad)"
        )

def main(args=None):
    rclpy.init(args=args)
    node = Laser()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()