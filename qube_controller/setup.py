from setuptools import setup

package_name = 'qube_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='Qube controller',
    license='TODO',
    entry_points={
        'console_scripts': [
            'controller = qube_controller.controller:main',
        ],
    },
)
