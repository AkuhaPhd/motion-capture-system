# Motion Capture System
## System Design
1. Overview:

   The motion capture system aims to accurately estimate and display the skeletal pose of a person in video feeds or 
   recorded videos using pre-trained deep learning models for human pose estimation.
   The system will process the input video, detect poses, generate a JSON output with key-point coordinates, 
   video with pose overlay, and a pose-based game called "Pose Race" for interactive experiences.

2. System Components:
   1. Data Processing:
      - Read the input video file or stream video from a camera source.
      - Extract frames from the video for processing.
   2. Pose Estimation:
      - Utilises Google's mediapipe pre-trained deep learning models suitable for human pose estimation in each frame.
      - Extract key-point coordinates and relevant pose information from the model's output.
      - Overlay the visualization on the video frames.
   3. JSON Output Generation:
      - Creates a JSON output file for all frame of the input video.
      - Include the key-point coordinates and frame information.
   4. Pose Race:
   
   A game where the player needs to match a series of predefined poses in a limited time to score points.

   Here's a high-level overview of how the game could work:

    * Display a random pose on the screen that the player needs to mimic.
    * Utilize the pose estimation module to continuously track the player's pose in real-time.
    * Compare the player's pose with the target pose and calculate a similarity score.
    * If the similarity score matches a predefined threshold, the player earns points and moves on to the next pose.
    * Repeat the process with a new pose until the time limit is reached.
    * Display the player's score at the end of the game.
  
   The game provides visual prompts to engage the player and make it more enjoyable. Additionally, difficulty levels is 
   increased as the player earn more points to make game more challenging.


System developed and tested on `ubuntu 20.04 lts` and `python 3.8`

## Installation and Usage
### General set up
run `./setup.sh` file once you are in root directory `/motion_capture_system` to install package requirements.

or

`pip install -r requirements.txt` if using non bash system.

### Extract pose landmark from video file 
* run `python3 ./src/main.py --input data/input/cam01_walking_01.mp4` if you want to display pose and downsize to file normal display.

* run `python3 ./src/main.py --input data/input/cam01_walking_01.mp4 --display 0` if you **don't** want to display pose.

* run `python3 ./src/main.py --input data/input/cam01_walking_01.mp4 --downsize 1` if you **don't** want to downsize video frames.

### To play pose game 
* run `python3 ./src/pose_race.py` .
* if your default webcam id is not `0` run `python3 ./src/pose_race.py --webcam <your-webcam-id>`.

## Tests
* run `pip install tox` to install automated testing tool.
* run `tox` to generate pytest coverage report.