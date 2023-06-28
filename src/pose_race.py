"""To play pose game please run $python3 ./src/game.py.
if your default webcam id is not 0, run $python3 ./src/game.py --webcam <id>"""
import time
import argparse
import cv2
from pose_estimation.pose_estimation import PoseEstimation
from pose_game.pose_game import PoseGame
from data_processing.data_processing import DataHandler

parser = argparse.ArgumentParser(
    prog="Pose game.",
    description="A prompt will be displayed on screen telling you what pose to do."
    "you can play this game sitting down. You have a few seconds to complete "
    "pose. The more points you get the less time you will get to complete "
    "pose. Good Luck!",
)

parser.add_argument("--webcam", default=0, type=int, help="Cam id needed.")
args = parser.parse_args()

# Instantiate game modules and variables
DH = DataHandler(args.webcam)
POSE = PoseEstimation()
POSE_GAME = PoseGame()
START_GAME_TIMER = time.time()
WAS_POSE_MATCHED = True
RANDOM_POSE = None

while True:
    # Get image frames
    bgr_frame, rbg_frame = DH.get_video_frame(1)
    player_landmarks = POSE.estimate_landmarks(rbg_frame)

    if WAS_POSE_MATCHED:
        RANDOM_POSE = POSE_GAME.get_random_pose()
        POSE_GAME.selected_pose = RANDOM_POSE["name"]
        POSE_GAME.display_game_variables(bgr_frame)

    predict_player_pose = POSE_GAME.get_player_pose(player_landmarks)

    if predict_player_pose == RANDOM_POSE["pose"]:
        POSE_GAME.game_score += 2
        POSE_GAME.update_game_level()
        START_GAME_TIMER = time.time()
        WAS_POSE_MATCHED = True
    else:
        WAS_POSE_MATCHED = False

    time_left = POSE_GAME.start_count_down(START_GAME_TIMER)
    POSE_GAME.display_game_variables(bgr_frame, time_left)

    if time_left == 0:
        print(f"Game over!, your final score was {POSE_GAME.game_score}.")
        break

    DH.display_frame(bgr_frame)

# When everything done, release the video capture
DH.cap.release()

# Closes all the frames
cv2.destroyAllWindows()