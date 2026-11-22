import os
import cv2

def play_video_reverse_slow(video_path="video.mp4", output_path="39.mp4"):
    """
    Exercise 39: Write a Python function to play the given video in reverse mode in slow motion.
    Saves a slowed reverse video to output_path and optionally displays frames with 100ms delay.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video '{video_path}'")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    original_fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    slow_fps = max(1.0, original_fps / 2.0) # 50% slow-motion framerate

    frames = []
    print(f"Extracting frames from '{video_path}'...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    print(f"Total frames read: {len(frames)}. Creating reversed slow-motion video...")

    # Save output video in reverse order at slowed framerate
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, slow_fps, (width, height))
    for frame in reversed(frames):
        out.write(frame)
    out.release()
    print(f"Reversed slow-motion video saved to '{output_path}' ({slow_fps:.1f} FPS).")

    # Interactive playback with 100ms delay for slow motion (as instructed in lab manual)
    if os.environ.get("HEADLESS", "0") != "1":
        for frame in reversed(frames):
            cv2.imshow('Reverse Slow Motion Video', frame)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    play_video_reverse_slow()
