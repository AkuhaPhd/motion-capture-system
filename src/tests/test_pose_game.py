import cv2
import unittest
from src.pose_estimation.pose_estimation import PoseEstimation
from src.pose_game.pose_game import PoseGame


class PoseGameModule(unittest.TestCase):
    """ Simple functionality test. """

    def setUp(self):
        """Unit testing setup"""
        # Initialise variables for unit testing
        self.pre_defined_poses = [[0, 1, 1], [1, 0, 0],  [0, 0, 1], [0, 1, 0]]
        self.pose = PoseEstimation()
        self.pose_game = PoseGame()
        # Read test images
        self.pose_frame_1 = cv2.imread("./data/test/pose1.png")
        self.pose_frame_2 = cv2.imread("./data/test/pose2.png")

    def test_both_hands_down_valid(self):
        # Get landmark predictions.
        test_result_1 = self.pose.estimate_landmarks(self.pose_frame_1)
        predict_player_pose = self.pose_game.get_player_pose(test_result_1)
        # Test both hands down
        self.assertEqual(predict_player_pose, self.pre_defined_poses[0])

    def test_both_hands_down_invalid(self):
        # Get landmark predictions.
        test_result_2 = self.pose.estimate_landmarks(self.pose_frame_2)
        predict_player_pose = self.pose_game.get_player_pose(test_result_2)
        # Test both hands down not equal
        self.assertNotEqual(predict_player_pose, self.pre_defined_poses[1])


if __name__ == "__main__":
    unittest.main()
