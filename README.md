# Image to Text Converter using Python and Tesseract OCR

## Description
This project loads an image (JPG/PNG), processes it, and extracts the textual content from it using the Tesseract OCR Engine. It also extracts basic image features and applies preprocessing (grayscale, Gaussian blur, thresholding).

## Prerequisites
- Python 3.7+
- Tesseract OCR (installed via `sudo apt-get install -y tesseract-ocr`)

## Setup
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your image file (e.g., `sample.jpg`) in the project directory.
2. Run the script:
   ```bash
   python image_to_text.py your_image.jpg
   ```
   If no image is specified, it defaults to `sample.jpg`.

3. The extracted text will be printed and saved to `extracted_text.txt`. The preprocessed image will be saved as `preprocessed.png`.
