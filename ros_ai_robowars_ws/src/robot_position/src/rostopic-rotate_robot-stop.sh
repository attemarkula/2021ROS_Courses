#!/bin/sh
rostopic pub -1 /robot1/wheel_r_velocity_controller/command std_msgs/Float64 "data: 0.0" &
rostopic pub -1 /robot1/wheel_l_velocity_controller/command std_msgs/Float64 "data: 0.0" &
rostopic pub -1 /robot1/wheel_r_velocity_controller/command std_msgs/Float64 "data: 0.0" 
rostopic pub -1 /robot1/wheel_l_velocity_controller/command std_msgs/Float64 "data: 0.0"
