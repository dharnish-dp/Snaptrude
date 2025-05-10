import pytesseract
from PIL import Image
import re

def extract_decimal_from_image(image_path):
    # Load the image
    image = Image.open(image_path)

    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(image)
    print("Extracted Text:", extracted_text)

    # Find the decimal number followed by "m²"
    match = re.search(r"\d+\.\d+", extracted_text)
    if match:
        return match.group(0).strip()
    else:
        return None



# Extract text from the uploaded image
if __name__=="__main__":
    value = extract_decimal_from_image("screenshot/test_FR01.png")
