import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class CylinderVolumeNode(Node):
    def __init__(self):
        super().__init__('cylinder_volume_node')
        self.declare_parameter("height", 2.5)
        self.cylinder_area = 0.0
            
        # Subscribers
        
        self.cylider_area_subscription_ = self.create_subscription(
            Float64,
            '/cylinder_area',
            self.cylinder_area_callback,
            10
            )
        
        # Publishers
        self.cylinder_volume_publisher_ = self.create_publisher(
            Float64,
            '/cylinder_volume',
            10
            )
        
        timer_ = 0.5
        self.timer_cylinder_volume_publisher_ = self.create_timer(
        timer_,
        self.cylinder_volume_callback
        )

    def cylinder_area_callback(self, cylinder_area: Float64):
        self.cylinder_area = cylinder_area.data

    def cylinder_volume_callback(self):

        height = self.get_parameter("height").get_parameter_value().double_value
        cylinder_volume = Float64()
        cylinder_volume.data = self.cylinder_area * height
        self.cylinder_volume_publisher_.publish(cylinder_volume)
        self.get_logger().info(f"Volume: {cylinder_volume.data:.4f} cm3")

def main(args=None):
    rclpy.init(args=args)
    cylinder_volume_node = CylinderVolumeNode()
    rclpy.spin(cylinder_volume_node)
    cylinder_volume_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()  