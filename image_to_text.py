import cv2
import numpy as np
from PIL import Image
import pytesseract
import sys

# Load image
image_path = sys.argv[1] if len(sys.argv) > 1 else 'sample.jpg'
image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image {image_path}")
    sys.exit(1)

# Preprocessing: Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Preprocessing: Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Preprocessing: Thresholding (Otsu's method)
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Feature extraction: Contours (as an example)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"Number of contours (features) found: {len(contours)}")

# Save preprocessed image for reference
cv2.imwrite('preprocessed.png', thresh)

# OCR with Tesseract
pil_img = Image.fromarray(thresh)
text = pytesseract.image_to_string(pil_img)

# Output results
print("Extracted Text:\n", text)
with open('extracted_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)