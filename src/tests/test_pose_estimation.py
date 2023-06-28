import cv2
import unittest
from src.pose_estimation.pose_estimation import PoseEstimation


class PoseEstimationModule(unittest.TestCase):
    """ Simple functionality test. """

    def setUp(self):
        """Unit testing setup"""
        # Initialise variables for unit testing
        self.pose = PoseEstimation()
        # Read test images
        self.pose_frame_1 = cv2.imread("./data/test/pose1.png")
        self.pose_frame_2 = cv2.imread("./data/test/pose2.png")

    def test_pose_estimation(self):
        # Get landmark predictions.
        test_result_1 = self.pose.estimate_landmarks(self.pose_frame_1)
        self.assertIsNotNone(test_result_1.pose_landmarks)

    def test_pose_landmarks_complete(self):
        # Get landmark predictions.
        test_result_2 = self.pose.estimate_landmarks(self.pose_frame_2)
        test_result_2_size = len(test_result_2.pose_landmarks.landmark)
        self.assertEqual(test_result_2_size, 33)


if __name__ == "__main__":
    unittest.main()
