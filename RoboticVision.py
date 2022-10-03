# Robotic vision by ti4ni

import time
import numpy as np
import pyscreenshot as RoboticVision
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "D:\\PyCharm\Project\\venv\\Lib\Tesseract\\tesseract.exe"

filename = 'Image.png'
last_time = time.time()

while True:
    screen = np.array(RoboticVision.grab(bbox=[141, 108, 1305, 137]))  # разрешение рабочей области
    print('Поиск занял: {} секунд(ы)'.format(
        time.time() - last_time))  # Если нужно выводить время поиска, по умолчанию включено
    last_time = time.time()
    cv2.imwrite(filename, screen)

    img = cv2.imread('Image.png')
    time.sleep(3)  # Если нужна задержка в выводе данных, по умолчанию включено. Значение задержки возможно изменять    
    text = pytesseract.image_to_string(img)
    print(
        "_______________________________________________________________________________________________________________________________________")
    print("Найденный текст:", text)

    index = text.find("time")
    if index == -1:
        print("Результат: слово не найдено")
    else:
        print("Результат: слово найдено")
        #break  # Если нужно останавливать программу сразу же, когда слово было найдено
