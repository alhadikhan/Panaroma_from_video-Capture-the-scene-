import cv2
import numpy as np
import os

# Step 1: Extract frames from the video
def extract_frames(video_path, output_dir, step=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    extracted_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save every `step` frame
        if frame_count % step == 0:
            frame_path = os.path.join(output_dir, f"frame_{extracted_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            extracted_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {extracted_count} frames to {output_dir}")

# Step 2: Stitch frames into a panorama
def create_panorama(frames_dir, output_path):
    # Load all frames from the directory
    frame_files = sorted([os.path.join(frames_dir, f) for f in os.listdir(frames_dir) if f.endswith(".jpg")])

    # Initialize the OpenCV Stitcher
    stitcher = cv2.Stitcher_create()

    # Read all frames
    frames = [cv2.imread(f) for f in frame_files]

    # Stitch frames together
    status, panorama = stitcher.stitch(frames)

    if status == cv2.Stitcher_OK:
        cv2.imwrite(output_path, panorama)
        print(f"Panorama saved to {output_path}")
    else:
        print(f"Error during stitching: {status}")

# Define paths
video_path = "video.mp4"  # Replace with your uploaded video path
frames_dir = "frames"
panorama_path = "panorama.jpg"

# Extract frames from the video
extract_frames(video_path, frames_dir, step=10)

# Create a panorama from the extracted frames
create_panorama(frames_dir, panorama_path)
