#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Импортируем тип сообщения


class RobotTrafficLight(Node):
    """
    Узел-издатель, который публикует новости робота.
    """
    
    def __init__(self):
        super().__init__('traffic_light')
        
        # Создаём Publisher
        self.publisher_ = self.create_publisher(
            String,           # тип сообщения
            'traffic_light',     # имя топика
            10                # размер очереди
        )
        
        # Таймер для публикации каждые 3 секунды
        self.timer = self.create_timer(3, self.publish_light)
        
        # Счётчик сообщений
        self.counter = 0
        self.LIGHTS = ['RED', 'YELLOW', 'GREEN']

        self.get_logger().info('Светофор запущен!')
    
    def publish_light(self):
        """
        Функция публикации новостей.
        """
        # Создаём сообщение
        msg = String()
        msg.data = self.LIGHTS[self.counter % 3]
        
        # Публикуем сообщение
        self.publisher_.publish(msg)
        
        # Выводим в лог
        self.get_logger().info(f'Публикую: "{msg.data}"')
        
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = RobotTrafficLight()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()