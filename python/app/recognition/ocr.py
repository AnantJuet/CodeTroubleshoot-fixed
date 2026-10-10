import os

import cv2
import pytesseract


def configure_tesseract():
    command = os.environ.get("TESSERACT_CMD")
    if command:
        pytesseract.pytesseract.tesseract_cmd = command
        return
    default = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.exists(default):
        pytesseract.pytesseract.tesseract_cmd = default


def tesseract_config():
    return "--oem 3 --psm 6"


def prepare_for_ocr(preprocessed):
    # preprocessing yields white text on black; Tesseract expects dark text on light.
    inverted = cv2.bitwise_not(preprocessed)
    # White margin so letters close to the image edge are not clipped.
    return cv2.copyMakeBorder(inverted, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=255)


def extract_text(image, config):
    configure_tesseract()
    return pytesseract.image_to_string(image, lang="eng", config=config)
