from PIL import ImageGrab
import pytesseract
import sys


def get_image_from_most_recent_clipboard():
    image = ImageGrab.grabclipboard()
    if image:
        return image
    else:
        print('No image found in clipboard')
        return None


image = get_image_from_most_recent_clipboard()
if image:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Software\OCR\tesseract.exe'
    try:
        arg = 'jpn'
        if len(sys.argv) >= 2:
            arg = sys.argv[1]
        if arg == 'rus' or arg == 'ru':
            text = pytesseract.image_to_string(image=image, lang='rus')
        elif arg == 'en' or arg == 'eng':
            text = pytesseract.image_to_string(image=image, lang='eng')
        else:
            text = pytesseract.image_to_string(image=image, lang='jpn')
    except Exception as e:
        print('OCR failed:', e)
        exit(1)
    print(text)
    # pyperclip.copy(text)
