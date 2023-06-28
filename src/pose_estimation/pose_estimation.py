"""Pose estimation module."""
import mediapipe as mp


class PoseEstimation:
    """Pose estimation module powered by Google's mediapipe. All methods are public."""

    def __init__(
            self, mode=False, up_body=False, smooth=True, detection_conf=0.5, track_conf=0.5
    ):
        self.mp_pose = mp.solutions.pose
        self.mp_draw = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            mode, 1, up_body, smooth, True, detection_conf, track_conf
        )
        # mode: to get fast detections and track
        # model_complexity=1: complexity of the landmark
        # up_body: whole body
        # smooth: whethe to filter landmark accross different input images to reduce jitter

    def estimate_landmarks(self, frame):
        """
        Get landmarks from video frame.
        :param frame: Video frame.
        :return: Detected landmarks.
        """
        landmarks = self.pose.process(frame)
        return landmarks

    def draw_landmarks(self, frame, landmarks):
        """
        Draw detected landmarks on video frame.
        :param frame: Video frame.
        :param landmarks: Detected landmarks.
        :return: Img with pose outlined.
        """
        if landmarks.pose_landmarks:
            self.mp_draw.draw_landmarks(
                frame, landmarks.pose_landmarks, self.mp_pose.POSE_CONNECTIONS
            )
        return frame
