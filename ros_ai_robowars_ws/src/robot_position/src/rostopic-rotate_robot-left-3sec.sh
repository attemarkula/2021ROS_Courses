#!/bin/sh
#rostopic pub -r 10 /robot1/wheel_r_velocity_controller/command std_msgs/Float64 "data: 2.0"
rostopic pub -1 /robot1/wheel_r_velocity_controller/command std_msgs/Float64 "data: 2.0"
sleep 1
rostopic pub -1 /robot1/wheel_r_velocity_controller/command std_msgs/Float64 "data: 0.0"
