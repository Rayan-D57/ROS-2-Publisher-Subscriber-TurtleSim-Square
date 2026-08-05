import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time


class TurtleSquare(Node):

    def __init__(self):
        super().__init__('turtle_square')

        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)

        self.pose = None

        while self.pose is None:
            rclpy.spin_once(self)

        time.sleep(1)

        self.reset_orientation()

        for i in range(4):
            self.move_forward(2.5)
            self.turn_90()

        self.stop()
        self.get_logger().info("تم رسم المربع بنجاح!")

    def pose_callback(self, msg):
        self.pose = msg

    def reset_orientation(self):
        target = 0.0
        msg = Twist()

        while True:
            rclpy.spin_once(self)
            error = target - self.pose.theta
            error = math.atan2(math.sin(error), math.cos(error))

            if abs(error) < 0.01:
                break

            speed = abs(error)
            if speed > 1.0:
                speed = 1.0
            if speed < 0.3:
                speed = 0.3

            if error > 0:
                msg.angular.z = speed
            else:
                msg.angular.z = -speed

            self.publisher.publish(msg)

        self.stop()

    def move_forward(self, distance):
        start_x = self.pose.x
        start_y = self.pose.y
        msg = Twist()

        while True:
            rclpy.spin_once(self)
            dx = self.pose.x - start_x
            dy = self.pose.y - start_y
            traveled = math.sqrt(dx**2 + dy**2)
            remaining = distance - traveled

            if remaining <= 0:
                break

            speed = remaining
            if speed > 1.0:
                speed = 1.0
            if speed < 0.2:
                speed = 0.2

            msg.linear.x = speed
            self.publisher.publish(msg)

        self.stop()

    def turn_90(self):
        start_angle = self.pose.theta
        target = math.atan2(
            math.sin(start_angle + math.pi / 2),
            math.cos(start_angle + math.pi / 2)
        )
        msg = Twist()

        while True:
            rclpy.spin_once(self)
            error = target - self.pose.theta
            error = math.atan2(math.sin(error), math.cos(error))

            if abs(error) < 0.01:
                break

            speed = abs(error)
            if speed > 1.0:
                speed = 1.0
            if speed < 0.3:
                speed = 0.3

            if error > 0:
                msg.angular.z = speed
            else:
                msg.angular.z = -speed

            self.publisher.publish(msg)

        self.stop()

    def stop(self):
        msg = Twist()
        self.publisher.publish(msg)
        time.sleep(0.2)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleSquare()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()