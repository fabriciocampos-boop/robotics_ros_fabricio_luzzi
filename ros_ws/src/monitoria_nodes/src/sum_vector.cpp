#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/vector3.hpp"
#include "monitoria_nodes/msg/two_vector.hpp"
#include "robot_interfaces/msg/obstacles.hpp"

class SumVector : public rclcpp::Node {
    public:
        SumVector() : Node("sum_vector") {
            publisher_ = this->create_publisher<geometry_msgs::msg::Vector3>("vector",10);
            subscriber_ = this->create_subscription<monitoria_nodes::msg::TwoVector>(
                "two_vector",
                10,
                std::bind(&SumVector::subscription_callback, this, std::placeholders::_1));
        }
    private:
        rclcpp::Publisher<geometry_msgs::msg::Vector3>::SharedPtr publisher_;
        rclcpp::Subscription<monitoria_nodes::msg::TwoVector>::SharedPtr subscriber_;

        void subscription_callback(monitoria_nodes::msg::TwoVector msg){
            geometry_msgs::msg::Vector3 vector_sum;
            vector_sum.x = msg.one.x + msg.two.x;
            vector_sum.y = msg.one.y + msg.two.y;
            vector_sum.z = msg.one.z + msg.two.z;
            publisher_->publish(vector_sum);
        }

};

int main(int argc, char * argv[]){
  rclcpp::init(argc, argv);
  auto node = std::make_shared<SumVector>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}