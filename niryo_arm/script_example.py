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
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import copy
from moveit_commander.conversions import pose_to_list
import warnings
warnings.filterwarnings("ignore")

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

    def __init__(self):
        cmd.Cmd.__init__(self)
        rospy.init_node('simple_docking_scenario')
        moveit_commander.roscpp_initialize(sys.argv)
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group_name = "niryo_arm"
        self.group = moveit_commander.MoveGroupCommander(group_name)


    def do_joint_move(self, arg):
        'moving joint to target joint'
        joint_goal = self.group.get_current_joint_values()
        joint_goal[0] = float(input("Enter joint 1 angle: "))
        joint_goal[1] = float(input("Enter joint 2 angle: "))
        joint_goal[2] = float(input("Enter joint 3 angle: "))
        joint_goal[3] = float(input("Enter joint 4 angle: "))
        joint_goal[4] = float(input("Enter joint 5 angle: "))
        joint_goal[5] = float(input("Enter joint 6 angle: "))

        self.group.go(joint_goal, wait=True)
        self.group.stop()

    def do_pose_move(self, arg):
        'moving joint to target pose'
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.x = float(input("Enter ROLL: "))
        pose_goal.orientation.y = float(input("Enter PITCH: "))
        pose_goal.orientation.z = float(input("Enter YAW: "))
        pose_goal.orientation.w = float(input("Enter QUATERNION: "))
        pose_goal.position.x = float(input("Enter X: "))
        pose_goal.position.y = float(input("Enter Y: "))
        pose_goal.position.z = float(input("Enter Z: "))
        self.group.set_pose_target(pose_goal)
        plan = self.group.go(wait=True)
        self.group.stop()
        self.group.clear_pose_targets()

    def do_quit(self, arg):
        return True
    
if __name__ == '__main__':
    ControlSuiteShell().cmdloop()