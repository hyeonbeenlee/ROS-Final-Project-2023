import numpy as np
import rospy
from geometry_msgs.msg import Pose, PoseStamped, PoseArray, Twist
import threading
import cmd, sys, os
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from nav_msgs.msg import Odometry
import tf2_geometry_msgs
import tf2_ros
import actionlib
from actionlib_msgs.msg import GoalStatus as goal_status
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ControlSuiteShell(cmd.Cmd):
    intro = bcolors.OKBLUE + "Welcome to the control suite shell.\nType help or ? to list commands.\n" + bcolors.ENDC
    prompt = "(csuite) "

    def __init__(self, args):
        cmd.Cmd.__init__(self)
        rospy.init_node('simple_docking_scenario')
        self.movebase_client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        self.args=args

    def do_navigation(self, arg):
        'navigation to target'
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.pose.position.x = float(self.args.x)
        goal.target_pose.pose.position.y = float(self.args.y)
        goal.target_pose.pose.position.z = 0

        goal.target_pose.pose.orientation.x = 0
        goal.target_pose.pose.orientation.y = 0
        goal.target_pose.pose.orientation.z = -1
        goal.target_pose.pose.orientation.w = 0.0

        self.movebase_client.send_goal(goal)

    def do_quit(self, arg):
        return True
    
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-x', default=0)
    parser.add_argument('-y', default=0)
    ControlSuiteShell(parser.parse_args()).cmdloop()