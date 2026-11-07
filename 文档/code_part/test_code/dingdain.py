from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped

class dinlian(Node):
    def __init__(self):
        super().__init__("cheshi")
        self.get_logger().info("定点导航节点建立")
        self.navigater=BasicNavigator()
        self.navigater.waitUntilNav2Active()
        self.pose_sub = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.pose_callback,
            10
        )

    def pose_callback(self, msg):
        """更新当前机器人位置"""
        self.current_pose = msg.pose.pose


    def daohang(self):
        self.point=self.mubiaodian()
        self.goal_poses2=[]
        for i, pose in enumerate(self.point):
            if self.check_point(pose):
                self.goal_poses2.append(pose)
                self.get_logger().info(f"目标点{i+1}验证通过: ({pose.pose.position.x}, {pose.pose.position.y})")
            else:
                self.get_logger().warning(f"目标点{i+1}不可达，已跳过")
        if not self.goal_poses2:
            self.get_logger().error("无有效目标点，任务终止")
            return False

        self.get_logger().info("开始执行多点导航...")
        self.navigater.followWaypoints(self.goal_poses2)
        


    def mubiaodian(self):
        self.goal_poses = []
        self.goal_poses1=PoseStamped()
        self.goal_poses1.header.frame_id='map'
        self.goal_poses1.header.stamp=self.navigater.get_clock().now().to_msg()
        self.goal_poses1.pose.position.x=4.0
        self.goal_poses1.pose.position.y=0.0
        self.goal_poses1.pose.orientation.w=1.0
        self.goal_poses.append(self.goal_poses1)
        self.goal_poses2=PoseStamped()
        self.goal_poses2.header.frame_id='map'
        self.goal_poses2.header.stamp=self.navigater.get_clock().now().to_msg()
        self.goal_poses2.pose.position.x=-4.0
        self.goal_poses2.pose.position.y=-1.0
        self.goal_poses2.pose.orientation.w=1.0
        self.goal_poses.append(self.goal_poses2)
        return self.goal_poses
    
    def check_point(self, goal_pose):
        if self.current_pose is None:
            self.get_logger().error("尚未收到定位信息")
            return False

        try:
        # 构造起点PoseStamped
            start_pose = PoseStamped()
            start_pose.header.frame_id = 'map'
            start_pose.header.stamp = self.get_clock().now().to_msg()
            start_pose.pose = self.current_pose
        
        # 获取路径
            path = self.navigater.getPath(start_pose, goal_pose)
        
            if path and len(path.poses) > 0:
                return True
            self.get_logger().warning(f"目标点({goal_pose.pose.position.x}, {goal_pose.pose.position.y})无有效路径")
            return False
        except Exception as e:
            self.get_logger().error(f"路径检查异常: {str(e)}")
            return False

    def guochen_check(self,point):
        while not self.navigator.isTaskComplete():
            feedback = self.navigator.getFeedback()
            current_idx = feedback.current_waypoint
            self.get_logger().info(
                f"当前目标: {current_idx+1}/{len(point)} | "
                
            )

            if current_idx + 1 < len(point):
                next_pose = point[current_idx + 1]
                if not self.check_point(next_pose):
                    self.get_logger().error("下一目标点变得不可达，取消任务！")
                    self.navigator.cancelTask()
                    return False
        
        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            self.get_logger().info("所有目标点导航完成！")
            return True
        else:
            self.get_logger().error(f"导航失败，状态码: {result}")
            return False





def main():
    rclpy.init()
    shiyan=dinlian()
    shiyan.daohang()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
