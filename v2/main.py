import tkinter as tk
from launch import launch_guardian_tales
from stop import stop_guardian_tales
from aventure import aventure_daily
from shop import shop_daily, shop_menu
from guild import guilde_daily
from utils import search_string_on_screenshot

def create_main_window():
    window = tk.Tk()
    window.title("Guardian Tales Bot")
    window.geometry("500x500")

    button_frame = tk.Frame(window)
    button_frame.pack(expand=True)

    launch_button = tk.Button(button_frame, text="Start Guardian Tales", command=lambda: (launch_guardian_tales()))
    launch_button.pack(pady=5)

    frame = tk.Frame(button_frame)
    frame.pack(pady=5)

    adventure_button = tk.Button(frame, text="[Daily] Donjon eveil", command=aventure_daily)
    adventure_button.pack(side=tk.LEFT, padx=5)

    shop_button = tk.Button(frame, text="[Daily] Shop", command=shop_daily)
    shop_button.pack(side=tk.LEFT, padx=5)

    guilde_button = tk.Button(button_frame, text="(Daily_in_DEV) Guilde", command=guilde_daily)
    guilde_button.pack(pady=5)

    test_button = tk.Button(button_frame, text="Shop and stop app", command=lambda: (shop_menu(), stop_guardian_tales()))
    test_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
