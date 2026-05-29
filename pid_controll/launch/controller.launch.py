from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('p', default_value='1.0'),
        DeclareLaunchArgument('i', default_value='0.0'),
        DeclareLaunchArgument('d', default_value='0.0'),
        DeclareLaunchArgument('reference', default_value='1.0'),

        Node(
            package='pid_controll',
            executable='controller',
            name='pid_controll',
            output='screen',
            parameters=[{
                'p': LaunchConfiguration('p'),
                'i': LaunchConfiguration('i'),
                'd': LaunchConfiguration('d'),
                'reference': LaunchConfiguration('reference'),
            }]
        ),
    ])