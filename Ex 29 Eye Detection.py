import os
import cv2

def detect_eyes(image_path="face_image.jpg", output_path="29.jpg"):
    """
    Exercise 29: Implement an Eye detection algorithm using OpenCV to detect and locate human eyes in images.
    Detects faces first, then locates eyes inside each face ROI and marks with blue rectangles.
    """
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    if eye_cascade.empty() and os.path.exists("haarcascade_eye_tree_eyeglasses.xml"):
        eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

    # Read image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image '{image_path}'")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces first
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    print(f"Detected {len(faces)} face(s).")

    for (x, y, w, h) in faces:
        # Extract face region of interest (ROI)
        face_roi_gray = gray[y:y+h, x:x+w]

        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.05, minNeighbors=2, minSize=(15, 15))
        if len(eyes) == 0 and os.path.exists("haarcascade_eye_tree_eyeglasses.xml"):
            glass_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
            eyes = glass_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.05, minNeighbors=2, minSize=(15, 15))

        print(f"Detected {len(eyes)} eye(s) inside face.")

        # Draw blue rectangles (255, 0, 0) around detected eyes as required by the PDF
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(image, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2)
            cv2.putText(image, "Eye", (x + ex, max(15, y + ey - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)

    # Save output
    cv2.imwrite(output_path, image)
    print(f"Eye detection output saved to '{output_path}'.")

    # Display image
    if os.environ.get("HEADLESS", "0") != "1":
        cv2.imshow("Eye Detection", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_eyes()
