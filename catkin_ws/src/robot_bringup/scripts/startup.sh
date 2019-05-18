#! /bin/bash

sudo python /home/udooer/catkin_ws/src/robot_bringup/scripts/ping.py
sleep 10
roscore
sleep 5
roslaunch robot_bringup minimal.launch
