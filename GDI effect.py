import requests
import pygame
import win32gui
import win32api
import win32con
import random
import pynput
import os
import ctypes
from tkinter import messagebox
import sys

messagebox.showwarning("WARNING!", "Данное программа может нанести вред компьютеру")
messagebox.showinfo("WARNING!", "Мы не несем ответственность за использование программы в неблагоприятных целей")
messagebox.showwarning("WARNING!", "В программе присутсвуют световые и gdi эффекты")
result = messagebox.askyesno("Вопрос", "Вы уверены что хотите запустить??")
if result:
    # скачивание звука
    if __name__ == '__main__':
        # Загружаем музыку
        req = requests.get('https://www.myinstants.com/media/sounds/salinewin-exe-bass-boost_jJTBEYe.mp3')
        if req.status_code == 200:
            # Создаем папку testing на диске C
            dir_path = 'C:\\sound'
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            else:
                pass
            # Сохраняем музыку в папке testing с названием malware.mp3
            with open(os.path.join(dir_path, 'malware.mp3'), 'wb') as f:
                f.write(req.content)

    # запуск звука
    pygame.init()
    song = pygame.mixer.music.load('C:\\sound\malware.mp3')
    pygame.mixer.music.play(-1)  # -1 тоесть на фоне

    # GDI эффекты
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0),
                user32.GetSystemMetrics(1)]
    while True:
        hdc = win32gui.GetDC(0)
        color = (random.randint(0, 122), random.randint(0, 4310), random.randint(0, 310))
        brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
        win32gui.SelectObject(hdc, brush)
        win32gui.BitBlt(hdc, random.randint(-100, 100), random.randint(-50, 10), sw, sh, hdc, 0, 0,
                        win32con.SRCCOPY)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)

        keyboard_listener = pynput.keyboard.Listener(suppress=True)
        keyboard_listener.start()
else:
    sys.exit()