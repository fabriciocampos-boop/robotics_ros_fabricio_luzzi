import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from velocity_interfaces.msg import VelocityHistory


class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        self.publisher_ = self.create_publisher(VelocityHistory, 'velocity_history', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

        
    def timer_callback(self):
        msg = VelocityHistory()
        msg.linear_velocities = [0.5, 0.7, 0.9, 1.1]
        msg.angular_velocities = [0.1, 0.05, -0.05, -0.1]
        msg.sample_count = len(msg.linear_velocities)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando amostra {self.count}: {msg.sample_count} pontos')
        self.count += 1


class VelocitySubscriber(Node):
    def __init__(self):
        super().__init__('velocity_subscriber')
        self.subscription = self.create_subscription(
            VelocityHistory,
            'velocity_history',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Amostras recebidas: {msg.sample_count}')
        self.get_logger().info(f'Velocidades lineares: {list(msg.linear_velocities)}')
        self.get_logger().info(f'Velocidades angulares: {list(msg.angular_velocities)}')


def main(args=None):
    rclpy.init(args=args)

    publisher_node = VelocityPublisher()
    subscriber_node = VelocitySubscriber()

    executor = MultiThreadedExecutor()
    executor.add_node(publisher_node)
    executor.add_node(subscriber_node)
    executor.spin()
    pass
    publisher_node.destroy_node()
    subscriber_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()