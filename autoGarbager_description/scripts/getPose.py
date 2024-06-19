#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry

last_print_time = 0
last_position = None  # 儲存上次的位置資訊

def odom_callback(msg):
  global last_print_time, last_position

  position = msg.pose.pose.position
  current_time = rospy.get_time()

  if current_time - last_print_time >= 1:
    if last_position is not None:
      # 計算位置變化量
      distance = ((position.x - last_position.x)**2 + (position.y - last_position.y)** 2)**0.5
      if distance > 0.01:  # 設定一個移動距離的閾值
        print(f"目前位置：x:{position.x:.3f}, y:{position.y:.3f} - 行進中")
      else:
        print(f"目前位置：x:{position.x:.3f}, y:{position.y:.3f} - 停止中")

    last_print_time = current_time
    last_position = position

rospy.init_node('get_odom_pose')
odom_sub = rospy.Subscriber('/odom', Odometry, odom_callback)
rospy.spin()