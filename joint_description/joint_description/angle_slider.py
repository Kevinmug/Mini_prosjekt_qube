import tkinter as tk

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Float32


class AngleSlider(Node):
    def __init__(self):
        super().__init__('angle_slider')

        self.angle = 0.0

        self.joint_pub = self.create_publisher(JointState, '/joint_states', 10)
        self.angle_pub = self.create_publisher(Float32, 'measured_angle', 10)

        self.root = tk.Tk()
        self.root.title('Angle Slider')

        self.scale = tk.Scale(
            self.root,
            from_=-3.14,
            to=3.14,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            length=400,
            label='angle (rad)',
            command=self.on_change
        )
        self.scale.set(0.0)
        self.scale.pack(padx=20, pady=20)

        self.create_timer(0.02, self.publish_all)
        self.root.after(10, self.update_loop)

    def on_change(self, value):
        self.angle = float(value)

    def publish_all(self):
        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = ['motor_joint']
        js.position = [self.angle]
        js.velocity = [0.0]
        js.effort = [0.0]
        self.joint_pub.publish(js)

        ang = Float32()
        ang.data = float(self.angle)
        self.angle_pub.publish(ang)

    def update_loop(self):
        rclpy.spin_once(self, timeout_sec=0)
        self.root.after(10, self.update_loop)

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def on_close(self):
        self.root.destroy()


def main(args=None):
    rclpy.init(args=args)
    node = AngleSlider()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()