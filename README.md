# ros_autoGarbager
2024_ros_final_project


### 1. open gazebo world
<code>roslaunch autoGarbager_description gazebo.launch<code>

### 2. client for detect robot status&position
<code>rosrun autoGarbager_description getPose.py<code>

### 3. control robot with teleop(default channel is /cmd_vel)

<code>rosrun teleop_twist_keyboard teleop_twist_keyboard.py<code>
