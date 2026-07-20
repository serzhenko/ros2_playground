#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Car(Node):
    """
    Узел-подписчик, который получает новости робота.
    """
    
    def __init__(self):
        super().__init__('smartphone')
        
        # Создаём Subscriber
        self.subscriber_ = self.create_subscription(
            String,                    # тип сообщения
            'traffic_light',              # имя топика
            self.callback_news,        # функция обработки
            10                         # размер очереди
        )
        
        self.get_logger().info('Машинка готова ловить сигналы светофора!')
    
    def callback_news(self, msg):
        """
        Эта функция вызывается при получении каждого сообщения.
        """
        if msg.data == "RED":
            action = "Остановка!"
        elif msg.data == "YELLOW":
            action = "Замедляюсь…"
        elif msg.data == "GREEN":
            action = "Еду!"
        else:
            action = "WTF"
        self.get_logger().info(action)


def main(args=None):
    rclpy.init(args=args)
    node = Car()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()