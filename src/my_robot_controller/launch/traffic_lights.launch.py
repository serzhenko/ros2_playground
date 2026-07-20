from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """
    Генерирует описание запуска для симуляции робота.
    """
    return LaunchDescription([
        # Узел светофора
        Node(
            package='my_robot_controller',
            executable='traffic_light',
            name='traffic_light',
            output='screen'  # вывод в консоль
        ),
        
        # Узел автомобиля
        Node(
            package='my_robot_controller',
            executable='car',
            name='car',
            output='screen'
        ),
        
    ])