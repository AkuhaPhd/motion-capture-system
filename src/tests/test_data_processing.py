import unittest
from src.data_processing.data_processing import DataHandler


class DataProcessingModule(unittest.TestCase):
    """ Simple functionality test. """

    def test_video_capture_from_file(self):
        dh = DataHandler("data/input/cam01_walking_01.mp4")
        self.assertTrue(dh.cap.isOpened())

    def test_video_capture_from_webcam(self):
        dh = DataHandler(0)
        self.assertTrue(dh.cap.isOpened())


if __name__ == "__main__":
    unittest.main()
