"""Data handler module."""
import time
import cv2


class DataHandler:
    """Data handler modules for pre, post video frame processing. Some methods are public."""
    def __init__(self, video_input):
        self.video_input = video_input
        self.cap = cv2.VideoCapture(self.video_input)
        self.previous_time = 0

    def get_video_frame(self, downsize):
        """
        Downsize video frame input. Set to 1 if you want same size as input.
        :param downsize: Downsize factor.
        :return: resized rgb and bgr image.
        """
        success, bgr_frame = self.cap.read()
        if success:
            bgr_frame = cv2.resize(
                bgr_frame, (bgr_frame.shape[1] // downsize, bgr_frame.shape[0] // downsize)
            )
            rgb_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)
            return bgr_frame, rgb_frame
        return None, None

    def _get_fps(self):
        """
        Private method gets video fps.
        :return: Video rate.
        """
        current_time = time.time()
        fps = 1 / (current_time - self.previous_time)
        self.previous_time = current_time
        return fps

    def display_frame(self, frame):
        """
        Display video frame with frame rate.
        :param frame: Video frame
        :return: None
        """
        if isinstance(self.video_input, str):
            fps = self._get_fps()
            cv2.putText(
                frame, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3
            )
        cv2.imshow("Frame", frame)
        cv2.waitKey(1)

    def get_frame__width_height(self):
        frame_width, frame_height = int(self.cap.get(3)), int(self.cap.get(4))
        return frame_width, frame_height
