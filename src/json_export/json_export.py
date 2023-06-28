"""Json export module."""
import cv2
import os
import json


class JsonExport:
    """Json export module. Method is public."""

    def __init__(self, frame_width, frame_height):
        self.frame_id = 0
        self.json_output = {}
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.video_out = cv2.VideoWriter(
            "./data/output/output.avi",
            cv2.VideoWriter_fourcc("M", "J", "P", "G"),
            10,
            (self.frame_width, self.frame_height),
        )

    def export_landmarks_to_json(self, landmarks):
        """
        Export landmark estimated from a given video.
        :param landmarks: Estimated landmark.
        :return: None
        """
        output_path = "./data/output/"

        # Create output path if it's absent
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        if landmarks.pose_landmarks:
            if len(landmarks.pose_landmarks.landmark) == 33:
                key_points = []
                for landmark in landmarks.pose_landmarks.landmark:
                    key_points.append(
                        [
                            landmark.x,
                            landmark.y,
                            landmark.z,
                            self.frame_width,
                            self.frame_height,
                        ]
                    )
                self.json_output[self.frame_id] = key_points

                json_output = json.dumps(self.json_output, indent=2)
                with open(f"{output_path}/pose.json", "w") as outfile:
                    outfile.write(json_output)
                self.frame_id += 1

    def export_mp4_video_with_poses(self, frame):
        self.video_out.write(frame)
