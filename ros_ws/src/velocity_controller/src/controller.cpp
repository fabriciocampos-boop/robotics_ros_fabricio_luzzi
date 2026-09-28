#include "velocity_controller/controller.hpp"
#include <cmath>

double Controller::limit_linear_velocity(double velocity) const{
    if (velocity == 0.0) {
        return 0.0;
    }
    if (std::abs(velocity) > max_linear_) {

        if (velocity > 0.0) {
            velocity = max_linear_;
        } else {
            velocity = -max_linear_;
        }
    }
    if (std::abs(velocity) < min_linear_) {

        if (velocity > 0.0) {
            velocity = min_linear_;
        } else {
            velocity = -min_linear_;
        }
    }

    return velocity;
}

double Controller::limit_angular_velocity(double velocity) const {
    if (velocity == 0.0) {
        return 0.0;
    }

    if (std::abs(velocity) > max_angular_) {

        if (velocity > 0.0) {
            velocity = max_angular_;
        } else {
            velocity = -max_angular_;
        }
    }

    if (std::abs(velocity) < min_angular_) {

        if (velocity > 0.0) {
            velocity = min_angular_;
        } else {
            velocity = -min_angular_;
        }
    }

    return velocity;
}

Controller::Controller(double kp_linear, double kp_angular,
                        double max_linear, double max_angular, 
                        double min_linear, double min_angular,
                        double dist_tolerance, double angle_tolerance): 
                    kp_linear_(kp_linear), kp_angular_(kp_angular),
                    max_linear_(max_linear), max_angular_(max_angular), 
                    min_linear_(min_linear), min_angular_(min_angular),
                    dist_tolerance_(dist_tolerance), angle_tolerance_(angle_tolerance){}

double Controller::get_yaw_from_quaternion(double x, double y, double z, double w){
    double num = 2 * (x * y + w * z);
    double den = 1 - 2 * (y * y + z * z);
    return std::atan2(num, den);
}

double Controller::normalize_angle(double angle){
    while (angle > M_PI) {
        angle -= 2 * M_PI;
    }
    while (angle < -M_PI) {
        angle += 2 * M_PI;
    }
    return angle;
}

Velocity Controller::compute(const Pose2D &robot, const Pose2D &goal) const {
    Velocity vel{0.0, 0.0};

    double dx = goal.x - robot.x;
    double dy = goal.y - robot.y;
    double distance = std::sqrt(dx * dx + dy * dy);
    double angle_to_goal = std::atan2(dy, dx);
    double angle_alignment = normalize_angle(angle_to_goal - robot.yaw);

    if (distance > dist_tolerance_) {
        if (std::abs(angle_alignment) > angle_tolerance_) {
            vel.angular = limit_angular_velocity(kp_angular_ * angle_alignment);
        }

        if (std::abs(angle_alignment) < angle_tolerance_) {
            vel.linear = limit_linear_velocity(kp_linear_ * distance);
        }

    } else {
        double final_angle_alignment = normalize_angle(goal.yaw - robot.yaw);

        if (std::abs(final_angle_alignment) > angle_tolerance_) {
            vel.angular = limit_angular_velocity(kp_angular_ * final_angle_alignment);        
        }
    }

    return vel;
}