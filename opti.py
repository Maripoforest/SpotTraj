import rospy
from nav_msgs.msg import Odometry
import geometry_msgs.msg
import pandas as pd
import time
import csv
import os

last_x = 0.0
last_y = 0.0

def callBack(msg):
    global last_x, last_y
    rospy.loginfo(msg.pose.position.x)
    # rospy.loginfo(msg.pose.position.y)
    rospy.loginfo(msg.pose.position.z)
    if(last_x == msg.pose.position.x and last_y == msg.pose.position.z):
        pass
    else:
        content = [time.time(), msg.pose.position.x, msg.pose.position.z]
        csv_writeline(filename, content)

def record():
    print("running")
    rospy.init_node('spot_participant')
    rospy.Subscriber('/vrpn_client_node/lefthand/pose', geometry_msgs.msg.PoseStamped, callBack)
    rospy.spin()

def csv_writeline(filename, filecontent):
    with open(filename, 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(filecontent)

if __name__ == '__main__':
    filename = ""
    filename = input("Name the file:")
    filename = filename + ".csv"
    header = ["time", "x", "y"]
    try:
        open(filename, 'x')
        csv_writeline(filename, header)
        record()
    except:
        if os.stat(filename).st_size == 0:
            l = 0
        else:
            file = pd.read_csv(filename)
            l = len(file)
        print("file already exists with", l, "lines")
        rp = input("Continue? yes/no\n")
        if (rp == "yes"):
            if (l == 0):
                csv_writeline(filename, header) 
            record()