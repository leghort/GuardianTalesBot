import tkinter as tk
from launch import launch_guardian_tales
from stop import stop_guardian_tales
from aventure import aventure_daily
from shop import shop_daily, shop_menu

def create_main_window():
    window = tk.Tk()
    window.title("Guardian Tales Bot")
    window.geometry("500x500")

    button_frame = tk.Frame(window)
    button_frame.pack(expand=True)

    launch_button = tk.Button(button_frame, text="Restart Guardian Tales", command=lambda: (stop_guardian_tales(), launch_guardian_tales()))
    launch_button.pack(pady=5)

    # Création du cadre pour les boutons Daily
    frame = tk.Frame(button_frame)
    frame.pack(pady=5)

    adventure_button = tk.Button(frame, text="[Daily] Donjon eveil", command=aventure_daily)
    adventure_button.pack(side=tk.LEFT, padx=5)

    shop_button = tk.Button(frame, text="[Daily] Shop", command=shop_daily)
    shop_button.pack(side=tk.LEFT, padx=5)

    test_button = tk.Button(button_frame, text="Shop and stop app", command=lambda: (shop_menu(), stop_guardian_tales()))
    test_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
