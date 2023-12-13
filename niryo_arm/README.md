# Niryo Arm For Final Project

## 1. Moveit을 이용한 가제보 시뮬레이션 만들기
https://ros-planning.github.io/moveit_tutorials/doc/setup_assistant/setup_assistant_tutorial.html 참고

```
    roslaunch 명령어와 moveit_setup_assistant툴을 이용하여, niryo_one_moveit pkg를 만드세요.
    (사용하는 urdf는 niryo_robot_description pkg의 niryo_one_gripper1_n_camera.urdf.xacro 입니다.)
    (virtual joint는 Child link는 base_link, parent link는 world로 만드세요)
    (planning Group은 niryo_arm으로 만들고 joint는 world, joint_world, joint_1부터 joint_6까지 포함시키세요.)
    (controllers는 niryo_arm_controller로 만들고 position_controllers/JointTrajectoryController로 선택하세요.)

    roslaunch 명렁어를 이용하여 만들어진 niryo_one_moveit pkg의 demo_gazebo를 실행하여, Rviz상에서 다양한 관절 움직임을 만들고 가제보가 잘 작동하는지 확인하세요.
```

## 2. Moveit Control
위의 demo_gazebo가 실행된 상태에서, 
```
    python3 script_example.py를 실행한 뒤, joint_move, pose_move 등을 입력하여, 원하는 지점 혹은 관절 목표까지 로봇이 움직이는 파이썬 스크립트를 작성해봅시다. (예제 파일 참고) 
```
참고: 다음의 명령어를 이용하면, 월드 좌표계에서 바라보는 target까지의 위치를 볼 수 있습니다. 
```
rosrun tf tf_echo /world /hand_link 
```
