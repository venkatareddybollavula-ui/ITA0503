import os
import cv2

def detect_smile(image_path="smiling_face.jpg", output_path="30.jpg"):
    """
    Exercise 30: Implement a Smile detection algorithm using OpenCV to detect and locate human smile in images.
    """
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image '{image_path}'")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces first
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    print(f"Detected {len(faces)} face(s).")

    for (x, y, w, h) in faces:
        # Extract face region
        face_roi = gray[y:y+h, x:x+w]

        # Detect smiles within the face region
        smiles = smile_cascade.detectMultiScale(
            face_roi,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(25, 25)
        )
        print(f"Detected {len(smiles)} smile(s).")

        # Draw green bounding boxes around smiles
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(image, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 255, 0), 2)
            cv2.putText(image, "Smile", (x + sx, max(15, y + sy - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

    # Save output
    cv2.imwrite(output_path, image)
    print(f"Smile detection output saved to '{output_path}'.")

    # Display image
    if os.environ.get("HEADLESS", "0") != "1":
        cv2.imshow("Smile Detection", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_smile()
