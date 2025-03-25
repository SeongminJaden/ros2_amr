from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': open('/home/ubuntu/ros2_ws/src/amr/urdf/amr.urdf').read(),
            }],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'config': 'home/ubuntu/ros2_ws/src/amr/rviz/amr.rviz',  # RViz 설정 파일 경로
            }],
            remappings=[
                ('/tf', '/tf'),
                ('/tf_static', '/tf_static'),
                ('/robot_description', 'robot_description'),
            ],
        ),
    ])

