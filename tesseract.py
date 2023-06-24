from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = "D:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Simple image to string
print(pytesseract.image_to_string(Image.open("tutanak_database/0_tutanak.jpg")))

"""
# Timeout/terminate the tesseract job after a period of time
try:
    print(pytesseract.image_to_string("tutanak_database/0_tutanak.jpg", timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass
"""
