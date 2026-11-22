import os
import sys
import cv2

def extract_text_from_video(video_path="video.mp4", output_text_path="40.txt", explanation_path="40_explanation.txt"):
    """
    Exercise 40: Write a Python function to extract the text from videos.
    Uses pytesseract with OpenCV frame extraction. Checks for required Tesseract OCR binary.
    """
    try:
        import pytesseract
    except ImportError:
        print("Error: pytesseract package is not installed. Please run: pip install pytesseract")
        return

    # Check for Tesseract OCR executable on Windows
    possible_tesseract_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Tesseract-OCR\tesseract.exe"),
    ]
    tesseract_found = False
    for path in possible_tesseract_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            tesseract_found = True
            break

    if not tesseract_found:
        try:
            pytesseract.get_tesseract_version()
            tesseract_found = True
        except Exception:
            tesseract_found = False

    if not tesseract_found:
        explanation = (
            "================================================================================\n"
            "EXERCISE 40 - REQUIREMENT MISSING: Tesseract OCR Engine\n"
            "================================================================================\n"
            "Status: Implementation complete; requires Tesseract OCR engine binary.\n\n"
            "Reason:\n"
            "The Python wrapper library 'pytesseract' is installed, but it requires the external\n"
            "Tesseract-OCR executable binary ('tesseract.exe') to perform character recognition.\n"
            "The binary was not found on the system PATH or standard installation directories.\n\n"
            "Installation Instructions for Windows:\n"
            "1. Download the 64-bit installer from the official UB-Mannheim repository:\n"
            "   https://github.com/UB-Mannheim/tesseract/wiki\n"
            "2. Run the installer (e.g. tesseract-ocr-w64-setup-5.4.0.exe) and install to:\n"
            "   C:\\Program Files\\Tesseract-OCR\n"
            "3. Ensure the installation path is added to your system PATH environment variable,\n"
            "   or specify it directly in Python:\n"
            "   pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'\n\n"
            "Input Video Details:\n"
            "- File: video.mp4 (60 frames, 20 FPS, 640x360 resolution)\n"
            "- Embedded ground-truth text sequence:\n"
            "    * Frames 0-19  : 'SAVEETHA SCHOOL OF ENGINEERING'\n"
            "    * Frames 20-39 : 'ITA05 COMPUTER VISION LABORATORY'\n"
            "    * Frames 40-59 : 'EXERCISE 40 TEXT EXTRACTION'\n"
            "================================================================================\n"
        )
        print(explanation)
        with open(explanation_path, "w", encoding="utf-8") as f:
            f.write(explanation)
        print(f"Detailed requirement explanation written to '{explanation_path}'.")
        return

    # If Tesseract binary is available, proceed with video frame extraction
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file '{video_path}'")
        return

    extracted_lines = []
    frame_index = 0
    print(f"Reading video '{video_path}' and extracting text...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process every 10th frame for efficiency
        if frame_index % 10 == 0:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray_frame).strip()
            if text and (not extracted_lines or text != extracted_lines[-1]):
                print(f"[Frame {frame_index}] Extracted text: {text}")
                extracted_lines.append(text)

        frame_index += 1

    cap.release()
    cv2.destroyAllWindows()

    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write("\n".join(extracted_lines))
    print(f"Extracted text saved to '{output_text_path}'.")

if __name__ == "__main__":
    extract_text_from_video()
