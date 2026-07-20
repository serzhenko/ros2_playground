from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), 
        glob('launch/*.launch.py')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='dmitry@serzhenko.me',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'battery_node = my_robot_controller.battery_node:main',
            'motor_simulator = my_robot_controller.motor_simulator:main',
            'system_monitor = my_robot_controller.system_monitor:main',
            'distance_sensor = my_robot_controller.distance_sensor:main',
            'temperature_sensor = my_robot_controller.temperature_sensor:main'
        ],
    },
)
