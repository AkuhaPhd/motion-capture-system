"""Extract pose landmarks from any given video. cd into motion capture dir and
run $ python3 ./src/main.py --input data/input/cam01_walking_01.mp4
run $ python3 ./src/main.py --input data/input/cam01_walking_01.mp4 --display 0,
if you want extract pose without display pose estimation. """
import cv2
import argparse
from pathlib import Path
from data_processing.data_processing import DataHandler
from pose_estimation.pose_estimation import PoseEstimation
from json_export.json_export import JsonExport


parser = argparse.ArgumentParser(
    prog="Human pose estimation from video.",
    description="Estimates the pose info of a single person from video.",
)

parser.add_argument("--input", type=str, help="Path to video input.")
parser.add_argument(
    "--display", default=1, type=int, help="Expects 1 (display) or 0 (don't display)."
)
parser.add_argument("--downsize", default=2, type=int, help="Downsize video frame.")

args = parser.parse_args()

# Validate input, check if path exist
if not Path(args.input).exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

# Validate resize, check if greater than zero to avoid 0 division error
if args.downsize <= 0:
    print("Downsize value must be int and greater than 0")
    raise SystemExit(1)

# Instantiate pose estimation modules
DH = DataHandler(args.input)
POSE = PoseEstimation()
frame_width, frame_height = DH.get_frame__width_height()
EXPORT = JsonExport(frame_width // args.downsize, frame_height // args.downsize)

while True:
    # Get image frames
    bgr_frame, rbg_frame = DH.get_video_frame(args.downsize)

    if bgr_frame is None:
        print("Pose estimation complete...")
        print("Json output saved at /data/output/pose.json")
        print("Video output saved at /data/output/output.avi")
        break

    landmarks = POSE.estimate_landmarks(rbg_frame)
    pose_frame = POSE.draw_landmarks(bgr_frame, landmarks)
    EXPORT.export_landmarks_to_json(landmarks)
    EXPORT.export_mp4_video_with_poses(pose_frame)

    if bool(args.display):
        DH.display_frame(pose_frame)

# When everything done, release the video capture and video write objects
DH.cap.release()
EXPORT.video_out.release()

# Closes all the frames
cv2.destroyAllWindows()
