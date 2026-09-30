#ifndef VELOCITY_CONTROLLER__VELOCITYCONTROLLER_HPP_
#define VELOCITY_CONTROLLER__CONTROLLER_HPP_ //

struct Velocity {
    double linear;
    double angular;
};

struct Pose2D {
    double x;
    double y;
    double yaw;
};

class Controller {
public:
    Controller(double kp_linear, double kp_angular,
               double max_linear, double max_angular, 
               double min_linear, double min_angular, 
               double dist_tolerance, double angle_tolerance);

    Velocity compute(const Pose2D &robot, const Pose2D &goal) const;
    double get_yaw_from_quaternion(double x, double y, double z, double w);
    static double normalize_angle(double angle);

private:
    double kp_linear_, kp_angular_;
    double max_linear_, max_angular_, min_linear_, min_angular_;
    double dist_tolerance_, angle_tolerance_;
    double limit_linear_velocity(double velocity) const;
    double limit_angular_velocity(double velocity) const;
};

#endif  