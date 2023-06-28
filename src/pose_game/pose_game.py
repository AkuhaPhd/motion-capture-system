"""Pose game module."""
import time
import random
import cv2


class PoseGame:
    """Pose game module. All methods are public."""

    def __init__(self):
        self.all_pose = [
            {"name": "both hands down", "pose": [0, 1, 1]},
            {"name": "both hands up", "pose": [1, 0, 0]},
            {"name": "left hand up", "pose": [0, 0, 1]},
            {"name": "right hand up", "pose": [0, 1, 0]},
        ]
        self.player_pose = None
        self.max_timer = 10
        self.game_score = 0
        self.selected_pose = None

    def get_player_pose(self, landmarks):
        """
        Predict play pose type from landmarks.
        :param landmarks: all 33 mediapipe key points.
        :return: predicted pose.
        """
        # Default player pose
        self.player_pose = [0, 0, 0]
        if landmarks.pose_landmarks:
            head_pose = landmarks.pose_landmarks.landmark[1]
            left_wrist = landmarks.pose_landmarks.landmark[15]
            right_wrist = landmarks.pose_landmarks.landmark[16]

            if head_pose.y >= right_wrist.y and head_pose.y >= left_wrist.y:
                self.player_pose[0] = 1
            if left_wrist.y > head_pose.y:
                self.player_pose[1] = 1
            if right_wrist.y > head_pose.y:
                self.player_pose[2] = 1
        return self.player_pose

    def display_game_variables(self, img, time_left=None):
        """
        Display in game variables.
        :param img: current frame.
        :param time_left: remaining time from count down.
        :return: frame with all text added.
        """
        if time_left:
            cv2.putText(img, f"Timer:{str(int(time_left))}", (25, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

        cv2.putText(img, f"Score:{str(int(self.game_score))}", (25, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 225, 0), 3)

        if self.selected_pose:
            cv2.putText(img, self.selected_pose, (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 3)
        return img

    def get_random_pose(self):
        """
        Get pose from existing list of poses.
        :return: Selected pose.
        """
        rand_num = random.randint(0, len(self.all_pose) - 1)
        return self.all_pose[rand_num]

    def start_count_down(self, start_game_timer):
        """
        Start and reset count down timer.
        :param start_game_timer: Timer start point.
        :return: Time left.
        """
        time_so_spent = time.time() - start_game_timer
        time_limit = self.max_timer - int(time_so_spent)
        return time_limit

    def update_game_level(self):
        """
        Update game level depending on player score.
        reduce timer duration depending on score.
        :return: None
        """
        if self.game_score > 15:
            self.max_timer = 9
        if self.game_score > 30:
            self.max_timer = 6
        if self.game_score > 60:
            self.max_timer = 3
