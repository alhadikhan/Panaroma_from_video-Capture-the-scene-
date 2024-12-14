import cv2
import numpy as np

# Function to create panorama from video
def create_panorama_from_video(video_path, output_path, frame_skip=10):
    # Open the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return
    
    # Initialize ORB detector and BFMatcher
    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Initialize variables for stitching
    prev_frame = None
    prev_kp = None
    prev_des = None
    panorama = None
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Skip frames if needed
        if cap.get(cv2.CAP_PROP_POS_FRAMES) % frame_skip != 0:
            continue
        
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect ORB keypoints and descriptors
        kp, des = orb.detectAndCompute(gray, None)

        if prev_frame is not None:
            # Match descriptors between the current and previous frames
            matches = bf.match(des, prev_des)
            matches = sorted(matches, key=lambda x: x.distance)
            
            # Extract matched keypoints
            src_pts = np.float32([kp[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([prev_kp[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
            
            # Find Homography matrix
            M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            
            # Stitch the current frame with the previous one using the Homography
            h, w = frame.shape[:2]
            panorama = cv2.warpPerspective(frame, M, (w*2, h))
            panorama[0:h, 0:w] = prev_frame
        
        # Set the current frame as the previous frame for the next iteration
        prev_frame = frame.copy()
        prev_kp = kp
        prev_des = des

        # Display the current panorama (optional)
        if panorama is not None:
            cv2.imshow("Panorama", panorama)
        
        # Wait for a key press (optional)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Save the panorama image
    if panorama is not None:
        cv2.imwrite(output_path, panorama)
        print(f"Panorama saved to {output_path}")
    
    # Release video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage
video_path = 'E:/Capture The Scene/video.mp4'
output_path = 'E:/Capture The Scene/output_panorama.jpg'
create_panorama_from_video(video_path, output_path)
