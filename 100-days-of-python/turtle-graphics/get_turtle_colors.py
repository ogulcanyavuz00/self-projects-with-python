import random
import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
from io import BytesIO
import re
from datetime import date, datetime


def get_a_turtle_color():
    def get_images() -> list[str]:
        response = requests.get("https://cs111.wellesley.edu/labs/lab02/colors")
        response.raise_for_status()
        html_code = response.text
        soup = BeautifulSoup(html_code, "html5lib")
        all_raw_images = soup("img")
        all_color_images = [f"https://cs111.wellesley.edu{image['src']}" for image in all_raw_images if "colorsPage" in image["src"]]
        return all_color_images

    def get_text_of_images() -> list[str]:
        pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
        color_images = get_images()
        text_in_color_images = []
        for image_url in color_images:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            text = pytesseract.image_to_string(image)
            text_in_color_images = [*text_in_color_images, text]
        return text_in_color_images

    def process_text_of_images() -> list[str]:
        processed_text_main = []
        for text in get_text_of_images():
            lowered_text = text.lower()
            # remove everything except letters, numbers, and spaces
            processed_text_step_1 = re.sub(r'[^a-zA-Z0-9\s]', '', lowered_text)
            # remove python turtle graphics ignoring case.
            processed_text_step_2 = re.sub(r'python turtle graphics', '', processed_text_step_1, flags=re.IGNORECASE)
            # join letter and number if there is space between them.
            processed_text_step_3 = re.sub(r'([a-zA-Z])\s+(\d)', r'\1\2', processed_text_step_2)
            # turn all space into one space only
            processed_text_step_4 = re.sub(r'\s+', ' ', processed_text_step_3)
            processed_text_main = [*processed_text_main, processed_text_step_4.split(" ")]

        processed_text_return = [color for el in processed_text_main for color in el if color != ""]

        return processed_text_return

    def write_colors_to_file():
        with open("colors.txt", "w") as file:
            file.write(f"{date.today()}\n")
            file.writelines([f"{line}\n" for line in process_text_of_images()])

    def pick_a_random_color():
        with open("colors.txt", "r") as file:
            date_in_str = file.readline().strip()
            if datetime.strptime(date_in_str, "%Y-%m-%d").date() == date.today():
                all_colors = file.readlines()[0:]
                return_color = random.choice(all_colors)
                return return_color.strip()
            else:
                write_colors_to_file()
                pick_a_random_color()

    return pick_a_random_color()


print(get_a_turtle_color())
