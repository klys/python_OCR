from PIL import ImageGrab
import pytesseract
from PIL import Image


def grab_screen():
    cap = ImageGrab.grab(bbox =(530, 200, 1330, 1000))
    cap.save("picture.png")

def get_text():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\klys\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    image = Image.open("picture.png")
    text = pytesseract.image_to_string(image)
    return text

def save_text():
    with open("text.txt", "w") as f:
        f.write(get_text())



grab_screen()
save_text()