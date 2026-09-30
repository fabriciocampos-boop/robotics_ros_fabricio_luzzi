import rclpy 
from rclpy.node import Node
from std_msgs.msg import String 
from std_msgs.msg import Int64 

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.get_logger().info('Subscriber Node has been started!')

        #Subscriptions
        self.text_subscriber_ = self.create_subscription(String, "/text", self.subscriber_callback, 10)

        #Publishers
        self.count_publisher_ = self.create_publisher(Int64, "/text_count", 10)
        self.count_min_publisher_ = self.create_publisher(Int64, "/text_count_min", 10)

        #Timer
        self.one_min_timer = self.create_timer(60, self.one_min_callback)


        #Variavéis
        self.count: int = 0

    def subscriber_callback(self, msg):
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.count += 1


        msg_count = Int64()
        msg_count.data = self.count
        self.get_logger().info('Count: "%d"' % msg_count.data)
        self.count_publisher_.publish(msg_count)

    def one_min_callback(self):
        msg_count_min = Int64()
        msg_count_min.data = self.count
        self.get_logger().info('Count in the last minute: "%d"' % msg_count_min.data)
        self.count_min_publisher_.publish(msg_count_min)


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()

    rclpy.spin(node) #dodando infinito até dar ctrl+c
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()