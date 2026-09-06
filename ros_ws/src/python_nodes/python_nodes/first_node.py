import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class FirstNode(Node):
    def __init__(self):
        super().__init__('first_node')
        self.get_logger().info('First Node has been started!')

        self.text_publisher_ = self.create_publisher(String, "/text", 10)

        self.timer_publisher_ = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Hello from First Node!"
        self.text_publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        return

def main(args=None):
    rclpy.init(args=args)
    node = FirstNode()
    rclpy.spin(node) #dodando infinito até dar ctrl+c
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()