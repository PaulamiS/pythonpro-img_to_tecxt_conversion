import cv2
import pytesseract
import sys
import os

# Check arguments
if len(sys.argv) < 2:
    print(f"Usage: python {os.path.basename(sys.argv[0])} <image_path>")
    sys.exit(1)

image_path = sys.argv[1]

# Read image
img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not open or find the image at {image_path}")
    sys.exit(1)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur_img = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Otsu's thresholding for better OCR accuracy
_, thresh = cv2.threshold(blur_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Optional: Use morphological operations to improve text clarity
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
processed_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Save processed image for debugging
cv2.imwrite("processed.png", processed_img)

# Configure tesseract path (for Windows)
# Uncomment and set if needed:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Perform OCR
custom_config = r'--oem 3 --psm 6'  # LSTM engine, assume a block of text
text = pytesseract.image_to_string(processed_img, lang="eng", config=custom_config)

# Output extracted text
print("Extracted Text:\n", text.strip())
