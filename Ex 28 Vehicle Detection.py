import os
import cv2

def detect_vehicles(video_path="traffic_video.mp4", cascade_path="cars.xml", output_path="28.mp4"):
    """
    Exercise 28: Implement a vehicle detection algorithm using OpenCV to detect and locate vehicles in each frame of the video.
    """
    # Load the pre-trained vehicle classifier
    vehicle_cascade = cv2.CascadeClassifier(cascade_path)
    if vehicle_cascade.empty():
        print(f"Error: Could not load vehicle cascade '{cascade_path}'")
        return

    # Open video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file '{video_path}'")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 20.0
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    total_detections = 0
    frame_index = 0
    print(f"Processing video '{video_path}' for vehicle detection...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_index += 1

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect vehicles in frame
        vehicles = vehicle_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(30, 30)
        )
        total_detections += len(vehicles)

        # Draw bounding boxes around detected vehicles (Green rectangles)
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Vehicle", (x, max(15, y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Write frame to output video
        out.write(frame)

        # Display if interactive
        if os.environ.get("HEADLESS", "0") != "1":
            cv2.imshow("Vehicle Detection", frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Finished processing {frame_index} frames. Total vehicle detections: {total_detections}.")
    print(f"Processed video saved to '{output_path}'.")

if __name__ == "__main__":
    detect_vehicles()
