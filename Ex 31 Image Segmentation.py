import os
import cv2

def segment_image(image_path="input_image.jpg", threshold_value=127, output_path="31.jpg"):
    """
    Exercise 31: Implement a Segmentation algorithm using OpenCV to segment the given input image based on threshold values.
    """
    # Read the input image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: Could not read image '{image_path}'")
        return

    # Apply thresholding for binary segmentation
    # Values > threshold_value become 255 (white), else 0 (black)
    _, segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Save result
    cv2.imwrite(output_path, segmented_image)
    print(f"Segmented image (threshold={threshold_value}) saved to '{output_path}'.")

    # Display images
    if os.environ.get("HEADLESS", "0") != "1":
        cv2.imshow("Original Image", image)
        cv2.imshow("Segmented Image", segmented_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    segment_image()
