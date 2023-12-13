# Scout Simulation For Final Project

## 0. Launch Gazebo and Rviz
```
    roslaunch 명령어를 이용하여, scout gazebo pkg의 scout_playpen을 실행하세요.
    roslaunch 명령어를 이용하여, scout viz pkg의 view_robot을 실행하세요.
```

## 1. Exploration
위의 두 패키지가 실행된 상태에서 
```
    roslaunch 명령어를 이용하여, scout navigation pkg의 gmapping_demo를 실행하세요.
    rosrun 명령어를 사용하여 teleop_twist_keyboard pkg의 teleop_twist_keyboard.py를 실행하세요.
    rviz 상의 movebase와 키보드를 이용하여, 맵을 획득하고, map server의 save기능을 이용하여 저장합니다. (저장 이름은 playpen_map으로 할 것)
    저장된 파일은 scout_navigation pkg의 maps 폴더에 넣어 둡니다. (기존 맵은 참고용임으로 덮어쓸 것)
```

## 2. Navigation
기존의 로스 관련 런치 파일들을 종료한 뒤, 다시 가제보와 Rviz를 실행합니다.
```
    roslaunch 명령어를 이용하여, scout navigation pkg의 amcl_demo를 실행하세요.
    rviz 상의 movebase를 이용하여, 자율 주행 하세요.
    python3 script_example.py를 실행한 뒤, navigation을 입력하여, 원하는 지점까지 이동하는 파이썬 스크립트를 작성해봅시다. (예제 파일 참고) 
```

