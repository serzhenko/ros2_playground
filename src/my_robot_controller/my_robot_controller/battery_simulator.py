#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # Импортируем тип сообщения


class RobotBatterySimulator(Node):
    """
    Узел-издатель, который публикует новости робота.
    """
    
    def __init__(self):
        super().__init__('battery_simulator')
        
        # Создаём Publisher
        self.publisher_ = self.create_publisher(
            Float32,          # тип сообщения
            'battery_level',  # имя топика
            10                # размер очереди
        )
        
        self.timer = self.create_timer(1, self.publish_level)
        
        self.level = 1.0

        self.get_logger().info('Батарея заряжена!')
    
    def publish_level(self):
        """
        Функция публикации новостей.
        """
        # Создаём сообщение
        msg = Float32()
        msg.data = self.level
        
        # Публикуем сообщение
        self.publisher_.publish(msg)
        
        # Выводим в лог
        self.get_logger().info(f'Публикую: "{msg.data}"')
        if self.level > 0.01:        
            self.level -= 0.01


def main(args=None):
    rclpy.init(args=args)
    node = RobotBatterySimulator()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()