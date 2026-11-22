import os
import cv2

def count_faces(image_path="face_image.jpg", cascade_path="haarcascade_frontalface_default.xml", output_path="38.jpg"):
    """
    Exercise 38: Write a Python function to Count the number of faces for the given input image using OpenCV.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image '{image_path}'")
        return 0

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load pre-trained Haar cascade face detection model
    face_cascade = cv2.CascadeClassifier(cascade_path)
    if face_cascade.empty():
        print(f"Error: Could not load cascade from '{cascade_path}'")
        return 0

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
    )

    face_count = len(faces)
    print(f"Number of faces detected: {face_count}")

    # Draw green rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Overlay face count banner
    cv2.putText(image, f"Detected Faces: {face_count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    # Save output
    cv2.imwrite(output_path, image)
    print(f"Output image with face count saved to '{output_path}'.")

    # Display image
    if os.environ.get("HEADLESS", "0") != "1":
        cv2.imshow("Face Detection", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return face_count

if __name__ == "__main__":
    count_faces()
