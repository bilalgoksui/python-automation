import time
import pyautogui
import tkinter as tk
import random

def move_cursor_periodically(seconds):
    while not stop_flag:
        time.sleep(seconds)
        print(f"{seconds} saniye sonra fare hareket edecek")
        screen_width, screen_height = pyautogui.size()
        x_target = random.randint(0, screen_width)
        y_target = random.randint(0, screen_height)
        pyautogui.moveTo(x_target, y_target, duration=5)

def start_movement():
    global stop_flag
    seconds = int(entry.get())
    stop_flag = False
    move_cursor_periodically(seconds)

def stop_movement():
    global stop_flag
    stop_flag = True

root = tk.Tk()
root.title("Cursor Mover")

label = tk.Label(root, text="Her kaç saniyede bir hareket etsin?")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

start_button = tk.Button(root, text="Başlat", command=start_movement)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Durdur", command=stop_movement)
stop_button.pack(pady=5)

stop_flag = False  
root.mainloop()
