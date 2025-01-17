# Capture The Scene

This repository contains my solution for the **Capture The Scene** challenge, where I processed a video to generate a panoramic shot by stitching overlapping frames together using Python.

## Challenge Description

The goal of the challenge was to:

1. **Extract frames from a provided video** at regular intervals.
2. **Identify overlapping frames** and stitch them together.
3. **Generate a single panoramic image** from the stitched frames.

## Solution Details

### Workflow

1. **Frame Extraction:**
   - Frames were extracted from the video at every 10th frame (configurable).
   - Saved extracted frames as `.jpg` files in the `frames` directory.

2. **Stitching Frames:**
   - Loaded all extracted frames.
   - Used OpenCV's `Stitcher_create` to combine the frames into a panorama.
   - Saved the resulting panoramic image as `panorama.jpg`.

3. **Error Handling:**
   - Checked for stitching errors and logged the status for debugging.

### Requirements

The following Python libraries are required to run this script:
- `opencv-python`
- `numpy`

### File Structure

```
.
├── main.py                # The Python script to process the video
├── requirements.txt       # Required Python libraries
├── video.mp4              # Input video (replace with your video file)
├── frames/                # Directory for extracted frames
└── panorama.jpg           # Output panoramic image
```

## Instructions

### Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd capture_scene_challenge
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Place your input video in the same directory as `main.py` and name it `video.mp4` (or update the script with your video path).

2. Run the script:
    ```bash
    python main.py
    ```

3. The extracted frames will be saved in the `frames/` directory.

4. The final panoramic image will be saved as `panorama.jpg`.

## Mistake Note

While I successfully completed the challenge, I realized in retrospect that:
- Proper error handling and edge cases (e.g., empty or non-overlapping frames) were not fully implemented.
- Additional testing on various video inputs could have ensured better generalization.

This feedback will help refine future submissions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
