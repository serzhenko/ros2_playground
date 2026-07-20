#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryMonitor(Node):
    """
    Узел-подписчик, который получает новости робота.
    """
    
    def __init__(self):
        super().__init__('battery_monitor')
        
        # Создаём Subscriber
        self.subscriber_ = self.create_subscription(
            Float32,                   # тип сообщения
            'battery_level',           # имя топика
            self.callback_news,        # функция обработки
            10                         # размер очереди
        )
        
        self.get_logger().info('Монитор аккумулятора запущен!')
    
    def callback_news(self, msg):
        """
        Эта функция вызывается при получении каждого сообщения.
        """

        if msg.data > 0.5:
            action = "OK"
        elif msg.data >= 0.2:
            action = "Батарея разряжается"
        else:
            action = "Критический уровень"
        self.get_logger().info(f'"{round(msg.data * 100)}%" -> {action}')


def main(args=None):
    rclpy.init(args=args)
    node = BatteryMonitor()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()