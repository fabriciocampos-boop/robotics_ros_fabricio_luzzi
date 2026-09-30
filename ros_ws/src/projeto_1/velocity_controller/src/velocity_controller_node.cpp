#include <memory>
#include <functional>
#include "rclcpp/rclcpp.hpp"
#include <cmath>
#include <chrono>

//#include "geometry_msgs/msg/vector3.hpp" - /goal vai se comunicar com Pose
#include "geometry_msgs/msg/twist_stamped.hpp" 
#include "geometry_msgs/msg/pose.hpp" 


#include "velocity_controller/controller.hpp"

using std::placeholders::_1;

class VelocityControllerNode : public rclcpp::Node{
    private:
        rclcpp::Subscription<geometry_msgs::msg::Pose>::SharedPtr subscription_goal_;
        rclcpp::Subscription<geometry_msgs::msg::Pose>::SharedPtr subscription_position_;
        rclcpp::Publisher<geometry_msgs::msg::TwistStamped>::SharedPtr publisher_vel_;
        geometry_msgs::msg::Pose::SharedPtr goal_ptr_;
        geometry_msgs::msg::Pose::SharedPtr robot_position_ptr_;
        rclcpp::TimerBase::SharedPtr timer_;
        Controller controller_;

        void goal_callback(const geometry_msgs::msg::Pose::SharedPtr msg){
            goal_ptr_ = msg;
            RCLCPP_INFO(this->get_logger(), "\nValor do /goal recebido:\nGoal: position: x=%f y=%f z=%f orientation: x=%f y=%f z=%f w=%f\n ", 
            msg->position.x, msg->position.y, msg->position.z,
            msg->orientation.x, msg->orientation.y, msg->orientation.z, msg->orientation.w);
        }

        void position_callback(const geometry_msgs::msg::Pose::SharedPtr msg){
            robot_position_ptr_ = msg;
            RCLCPP_INFO(this->get_logger(), "\nValor do /robot_position recebido:\nRobot Position: position: x=%f y=%f z=%f orientation: x=%f y=%f z=%f w=%f\n", 
            msg->position.x, msg->position.y, msg->position.z, 
            msg->orientation.x, msg->orientation.y, msg->orientation.z, msg->orientation.w);
        }

        void timer_callback(){
            geometry_msgs::msg::TwistStamped message;
            message.header.stamp = this->get_clock()->now();

            if (goal_ptr_ != nullptr && robot_position_ptr_ != nullptr) {
                Pose2D robot{
                    robot_position_ptr_->position.x,
                    robot_position_ptr_->position.y,
                    Controller::get_yaw_from_quaternion(
                        robot_position_ptr_->orientation.x, robot_position_ptr_->orientation.y,
                        robot_position_ptr_->orientation.z, robot_position_ptr_->orientation.w)
                };

                Pose2D goal{
                    goal_ptr_->position.x,
                    goal_ptr_->position.y,
                    Controller::get_yaw_from_quaternion(
                        goal_ptr_->orientation.x, goal_ptr_->orientation.y,
                        goal_ptr_->orientation.z, goal_ptr_->orientation.w)
                };

                Velocity vel = controller_.compute(robot, goal);
                message.twist.linear.x = vel.linear;
                message.twist.angular.z = vel.angular;
            }else {
                message.twist.linear.x = 0.0;
                message.twist.linear.y = 0.0;
                message.twist.linear.z = 0.0;
                message.twist.angular.x = 0.0;
                message.twist.angular.y = 0.0;
                message.twist.angular.z = 0.0;
                }

            RCLCPP_DEBUG(this->get_logger(), 
            "Linear: x='%f', y='%f', z='%f'\n"
            "Angular: x='%f', y='%f', z='%f'", 
            message.twist.linear.x, message.twist.linear.y, message.twist.linear.z, 
            message.twist.angular.x, message.twist.angular.y, message.twist.angular.z);

            publisher_vel_->publish(message);
        }

    public:
        VelocityControllerNode() : Node("velocity_controller_node"),
            controller_(

            //Valores escolhidos arbitrariamente
            this->declare_parameter("kp_linear", 1.0),
            this->declare_parameter("kp_angular", 1.5),

            this->declare_parameter("max_linear", 0.5),
            this->declare_parameter("max_angular", 2.5),

            this->declare_parameter("min_linear", 0.1),
            this->declare_parameter("min_angular", 0.2),

            this->declare_parameter("dist_tolerance", 0.10),
            this->declare_parameter("angle_tolerance", M_PI / 36.0) //5graus
            ){

            
    

            subscription_goal_ = this->create_subscription<geometry_msgs::msg::Pose>(
                "goal", 10,
                std::bind(&VelocityControllerNode::goal_callback, this, _1)
            );

            subscription_position_ = this->create_suS<std_msgbscription<geometry_msgs::msg::Pose>(
                "robot_position", 10,
                std::bind(&VelocityControllerNode::position_callback, this, _1)
            );

            publisher_vel_ = this->create_publisher<geometry_msgs::msg::TwistStamped>(
                "cmd_vel", 10);
            timer_ = this->create_wall_timer(
                std::chrono::milliseconds(100),
                std::bind(&VelocityControllerNode::timer_callback, this)
            );
        }
};


int main(int argc, char * argv[]){
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<VelocityControllerNode>());
    rclcpp::shutdown();
    return 0;
}