"""Pose estimation module."""
import mediapipe as mp


class PoseEstimation:
    """Pose estimation module powered by Google's mediapipe. All methods are public."""

    def __init__(
        self,
        mode=False,
        complexity=1,
        smooth=True,
        segmentation=False,
        detection_conf=0.5,
        track_conf=0.5,
    ):
        self.mp_pose = mp.solutions.pose
        self.mp_draw = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            static_image_mode=mode,
            model_complexity=complexity,
            smooth_landmarks=smooth,
            enable_segmentation=segmentation,
            smooth_segmentation=segmentation,
            min_detection_confidence=detection_conf,
            min_tracking_confidence=track_conf,
        )

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
