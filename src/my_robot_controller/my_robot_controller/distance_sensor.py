#!/usr/bin/env python3

from random import randint

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32  # Импортируем тип сообщения


class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_sensor')
        
        # Создаём Publisher
        self.distance_publisher = self.create_publisher(
            Float32,          # тип сообщения
            'distance',  # имя топика
            10                # размер очереди
        )
        
        self.timer = self.create_timer(1, self.update_distance)
        
        self.distance = 5.0

        self.get_logger().info('Датчик расстояния активирован!')
    
    
    def update_distance(self):
        """
        Обновление расстояния.
        """   
        self.distance = randint(5, 50) / 10.0


        # Публикуем текущий уровень
        msg = Float32()
        msg.data = self.distance
        self.distance_publisher.publish(msg)
        
        if self.distance < 1.0:
            self.get_logger().warn('Obstacle close!')
            return
        

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSensor()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()