from setuptools import setup

package_name = 'joint_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/view_joint.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/joint_model.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mugis',
    maintainer_email='Mugis@todo.todo',
    description='Joint description package',
    license='TODO',
    entry_points={
        'console_scripts': [
            'angle_slider = joint_description.angle_slider:main',
        ],
    },
)