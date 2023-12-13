# Mobile Manpulator For Final Project

## 1. 모바일 메니퓰레이터의 팔에 대한 moveit 만들기
```
    제공되는 파일의 mobile_manipulator_description pkg의 mobile_manipulator.xacro 를 읽어와 moveit pkg를 만드세요.
    Virtual Joints 및 end-effectors는 설정할 필요 없습니다.
    플래닝 그룹은 joint_world, joint1-6 까지 포함하세요.
    그 뒤, 완성된 moveit pkg에서 demo_gazebo를 실행하여 Rviz상에서 메니퓰레이터가 작동하는지 확인합니다. 
```

## 2. 모바일 베이스의 제어
위의 mobile_manipulator_moveit pkg의 demo_gazebo가 실행된 상태에서, 
```
    roslaunch를 활용하여 scout_control의 Control_mobile.launch를 실행 한 뒤, teleop twist keyboard를 활용하여, 모바일 베이스가 정상적으로 움직이는지 확인합니다. 
```

## 3. 지도 상의 3개의 소화전을 검사하는 자율 작업 코드를 작성합니다.
위의 mobile_manipulator_gazebo pkg의 demo_gazebo가 실행된 상태에서, 메니퓰레이터에 부착된 카메라를 이용하여 3개의 빨간 색 소화전을 바라보게 하는 자율 주행 및 작업 코드를 완성해 보세요.

먼저 모바일 제어를 편리하게 하기 위해 다음의 코드를 수정합니다.
```
    moveit pkg의 gazebo.launch 파일의 6번째 줄을 다음과 같이 고쳐주세요.
    <arg name="world_name" value="$(find scout_gazebo)/worlds/test_playpen.world"/>
    그 다음, 아무 빈 칸에 다음의 줄을 추가해 주세요.
    <include file="$(find scout_control)/launch/control_mobile.launch"/>  
```

모바일 메니퓰레이터의 네비게이션은 다음을 이용합니다.
```
    roslaunch your_moveit_pkg demo_gazebo.launch use_rviz:=false
    roslaunch scout_viz view_mm_robot.launch
    roslaunch scout_navigation amcl_demo.launch
```
파이썬 스크립트를 만들어, 3개의 위치의 소화전 앞에 모바일 베이스를 움직이고, 그 뒤, 모바일 메니퓰레이터를 작동시키는 코드를 작성해보세요. 