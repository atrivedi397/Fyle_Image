import datetime
import re

import jsonify
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and
                                                              # pytesseract to detect the string in the image
    match = re.search(r'\d{2}/\d{2}/\d{2}', text)
    # date = datetime.datetime.strptime(match, '%m/%d/%Y').date()
    print("match: ", match, "\n")

    if match is not None:
        return text, str(f"date: {match}")
    else:
        return text, str("date: null")
