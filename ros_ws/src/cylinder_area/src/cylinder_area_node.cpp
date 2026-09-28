#include <cmath>
#include <chrono>
#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"

using namespace std::chrono_literals;
const double PI = M_PI;

class CylinderAreaNode : public rclcpp::Node{
    private:
            rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr cylinder_area_publisher_;
            rclcpp::TimerBase::SharedPtr timer_;
        void msg(){
            std_msgs::msg::Float64 area;
            double r = this->get_parameter("radius").as_double();
            area.data = std::pow(r,2)*PI;
            RCLCPP_INFO(this->get_logger(), "Área %f cm", area.data);
            cylinder_area_publisher_->publish(area);
            }
    public:
        CylinderAreaNode()
            : Node("cylinder_area_node") {
                rcl_interfaces::msg::ParameterDescriptor radius_description_;
                this->declare_parameter("radius", 5.0);
                cylinder_area_publisher_ = this->create_publisher<std_msgs::msg::Float64>("cylinder_area", 10);
                timer_ = this->create_wall_timer(500ms, std::bind(&CylinderAreaNode::msg, this));
            }
};
int main(int argc, char **argv){
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CylinderAreaNode>());
    rclcpp::shutdown();
    return 0;
}
