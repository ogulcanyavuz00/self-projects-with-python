import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
from io import BytesIO
import re
from rest import result


def get_images() -> list[str]:
    response = requests.get("https://cs111.wellesley.edu/labs/lab02/colors")
    response.raise_for_status()
    html_code = response.text
    soup = BeautifulSoup(html_code, "html5lib")
    all_raw_images = soup("img")
    image_links = [f"https://cs111.wellesley.edu{image['src']}" for image in all_raw_images if "colorsPage" in image["src"]]
    return image_links


def get_text_of_images():
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    color_images = get_images()
    text_in_images = []
    for image_url in color_images:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(image)
        text_in_images = [*text_in_images, text]
    return text_in_images

# def process_text():
#     raw_text = get_text_of_images()
#     for text in raw_text:
#         re.sub()


all_colors = []
for text in result:
    lowered_text = text.lower()
    # remove everything except letters, numbers, and spaces
    processed_text_1 = re.sub(r'[^a-zA-Z0-9\s]', '', lowered_text)
    # remove python turtle graphics ignoring case.
    processed_text_2 = re.sub(r'python turtle graphics', '', processed_text_1, flags=re.IGNORECASE)
    # join letter and number if there is space between them.
    processed_text_3 = re.sub(r'([a-zA-Z])\s+(\d)', r'\1\2', processed_text_2)
    # turn all space into one space only
    processed_text_4 = re.sub(r'\s+', ' ', processed_text_3)
    all_colors.append(processed_text_4)

colorss = []
for color in all_colors:
    print(color.strip(" "))
