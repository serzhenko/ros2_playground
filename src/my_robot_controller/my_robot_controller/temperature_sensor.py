#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32  # Импортируем тип сообщения


class TemperatureSensor(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        
        # Создаём Publisher
        self.temperature_publisher = self.create_publisher(
            Float32,          # тип сообщения
            'temperature',  # имя топика
            10                # размер очереди
        )
        
        self.timer = self.create_timer(1, self.update_temperature)
        
        self.temperature = 25.0

        self.get_logger().info('Датчик температуры активирован!')
    
    
    def motor_state_callback(self, msg):
        """
        Получаем информацию о состоянии моторов.
        """
        self.is_robot_moving = msg.data
        state = "MOVING" if self.is_robot_moving else "IDLE"
        self.get_logger().info(f'Motor state changed: {state}')

    def update_temperature(self):
        """
        Обновление уровня температуры.
        """   
        # Температура зависит от состояния моторов
        if self.is_robot_moving:
            heat_rate = 2.0 
        else:
            heat_rate = -1.0 
        
        self.temperature += heat_rate
        
        if self.temperature <= 25.0:
            self.temperature = 25.0
        elif self.temperature > 100.0:
            self.temperature = 100.0


        # Публикуем текущий уровень
        msg = Float32()
        msg.data = self.temperature
        self.temperature_publisher.publish(msg)
        
        if self.temperature > 80.0:
            self.get_logger().warn('Overheating!')
            return
        

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensor()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()