import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_msgs.msg import JointState


class Simulator(Node):
    def __init__(self):
        super().__init__('simulator')

        self.angle = 0.0
        self.velocity = 0.0
        self.u = 0.0

        self.sub = self.create_subscription(
            Float32,
            'voltage',
            self.voltage_callback,
            10
        )

        self.angle_pub = self.create_publisher(
            Float32,
            'measured_angle',
            10
        )

        self.joint_pub = self.create_publisher(
            JointState,
            '/joint_states',
            10
        )

        self.timer = self.create_timer(0.02, self.update)

        self.get_logger().info('Simulator started')

    def voltage_callback(self, msg):
        self.u = msg.data

    def update(self):
        self.velocity += self.u * 0.01
        self.angle += self.velocity * 0.02

        angle_msg = Float32()
        angle_msg.data = float(self.angle)
        self.angle_pub.publish(angle_msg)

        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = ['motor_joint']
        js.position = [float(self.angle)]
        js.velocity = [float(self.velocity)]
        js.effort = [0.0]
        self.joint_pub.publish(js)


def main(args=None):
    rclpy.init(args=args)
    node = Simulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()