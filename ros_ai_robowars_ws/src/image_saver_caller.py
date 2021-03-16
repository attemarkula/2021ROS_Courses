image_saver_caller.py
#!/usr/bin/python3

import rospy
from std_srvs.srv import Empty

rospy.init_node("image_saver_caller")
rate = rospy.Rate(0.2)
while not rospy.is_shutdown():	
	rospy.wait_for_service('/camera_controller/save')
	#cameracontroller määrätään ko. launch filessä.
	saver = rospy.ServiceProxy('/camera_controller/save, Empty')
	saver()
	rate.sleep()