# ros_autoGarbager
2024_ros_final_project

## 1.open gazebo world

`roslaunch autoGarbager_description gazebo.launch`

## 2.client for detect robot status&position

`rosrun autoGarbager_description getPose.py`

## 3.control robot with teleop(default channel is /cmd_vel)

`rosrun teleop_twist_keyboard teleop_twist_keyboard.py`
