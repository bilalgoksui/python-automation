import time
import pyautogui
import tkinter as tk
import threading
import random

def move_cursor_periodically(seconds):
    while not stop_event.is_set():
        time.sleep(seconds)
        print(f"{seconds} saniye sonra fare hareket edecek")
        screen_width, screen_height = pyautogui.size()
        x_target = random.randint(0, screen_width)
        y_target = random.randint(0, screen_height)
        pyautogui.moveTo(x_target, y_target, duration=5)

def start_movement():
    seconds = int(entry.get())
    global thread, stop_event
    stop_event = threading.Event()
    thread = threading.Thread(target=move_cursor_periodically, args=(seconds,))
    thread.start()

def stop_movement():
    if thread.is_alive():
        stop_event.set()
        thread.join()

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

root.mainloop()
