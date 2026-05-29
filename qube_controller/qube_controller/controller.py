import rclpy
from rclpy.node import Node

class QubeController(Node):
    def __init__(self):
        super().__init__('qube_controller')
        self.get_logger().info('Qube controller started')

def main(args=None):
    rclpy.init(args=args)
    node = QubeController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()