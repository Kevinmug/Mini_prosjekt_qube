from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('qube_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'qube.urdf')

    with open(urdf_file, 'r', encoding='utf-8') as f:
        robot_description = f.read()

    return LaunchDescription([
        DeclareLaunchArgument('p', default_value='1.0'),
        DeclareLaunchArgument('i', default_value='0.0'),
        DeclareLaunchArgument('d', default_value='0.0'),
        DeclareLaunchArgument('reference', default_value='1.0'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-f', 'world'],
            output='screen'
        ),

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