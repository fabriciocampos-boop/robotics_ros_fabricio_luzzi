#include <iostream>
#include <memory>
#include <string>
#include <chrono>
#include <functional>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class   PublisherNode : public rclcpp::Node {
    private:
        
        //std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String>> publisher_;
        //std::shared_ptr<rclcpp::TimerBase> timer_;

        rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
        rclcpp::TimerBase::SharedPtr timer_;
        size_t count_ = 0;

        void msg(){
            std_msgs::msg::String message;
            message.data = "Hello, ROS2!" + std::to_string(count_++);
            RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
            publisher_->publish(message);
        }

    public:
        PublisherNode() : Node("publisher_node") {
            publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
            timer_ = this->create_wall_timer(
                std::chrono::milliseconds(500),
                std::bind(&PublisherNode::msg, this)
            );
        }
        
};
int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PublisherNode>());
    return 0;
}