import os
import cv2

def reverse_video(input_video_path="input_video.mp4", output_video_path="26.mp4"):
    """
    Exercise 26: Implement a function to reverse the frames of the video to create a video in reverse mode using OpenCV.
    """
    # Open the video file
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print(f"Error: Could not open input video '{input_video_path}'")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Reading video '{input_video_path}' ({frame_width}x{frame_height} @ {fps:.1f} fps, {total_frames} frames)...")

    # Read all frames into memory
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()

    print(f"Read {len(frames)} frames. Reversing frame order...")
    # Reverse frames
    frames.reverse()

    # Define video writer with MP4 codec
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # Write frames in reverse order
    for frame in frames:
        out.write(frame)
    out.release()
    print(f"Reversed video saved as: {output_video_path}")

if __name__ == "__main__":
    reverse_video()
