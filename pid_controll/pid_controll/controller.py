import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')

        self.declare_parameter('p', 1.0)
        self.declare_parameter('i', 0.0)
        self.declare_parameter('d', 0.0)
        self.declare_parameter('reference', 1.0)

        self.p = float(self.get_parameter('p').value)
        self.i = float(self.get_parameter('i').value)
        self.d = float(self.get_parameter('d').value)
        self.ref = float(self.get_parameter('reference').value)

        self.integral = 0.0
        self.prev_error = 0.0

        self.sub = self.create_subscription(
            Float32,
            'measured_angle',
            self.callback,
            10
        )

        self.pub = self.create_publisher(
            Float32,
            'voltage',
            10
        )

        self.get_logger().info(
            f'PID started: P={self.p}, I={self.i}, D={self.d}, REF={self.ref}'
        )

    def callback(self, msg):
        error = self.ref - msg.data
        self.integral += error
        derivative = error - self.prev_error

        u = self.p * error + self.i * self.integral + self.d * derivative

        self.prev_error = error

        out = Float32()
        out.data = float(u)
        self.pub.publish(out)


# 🔥 THIS WAS MISSING / BROKEN
def main(args=None):
    rclpy.init(args=args)
    node = PIDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()