import rclpy
from rclpy.node import Node
from robot_interfaces.msg import RobotState
from robot_interfaces.msg import Obstacles, Obstacle

class Teste(Node):
    def __init__(self):
        super().__init__("nome_no")

        self.publisher = self.create_publisher(RobotState, "/topico_name", 10)

        self.subscriber = self.create_subscription(RobotState, "/receba", self.callback, 10)

    def callback(self, msg : RobotState):
        temp = RobotState() 
        temp = msg 
        self.publisher.publish(temp)

def main(args=None):
    rclpy.init(args=args)
    node = Teste()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



