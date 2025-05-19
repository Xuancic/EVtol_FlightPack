import pygame
import tkinter as tk
from tkinter import ttk
import sys

class JoystickGUI:
    def __init__(self, master, joystick_index):
        self.master = master
        master.title(f"Joystick {joystick_index}")

        # 初始化pygame摇杆
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            raise Exception("No joystick found")

        if joystick_index >= pygame.joystick.get_count():
            raise Exception(f"Joystick index {joystick_index} out of range. Total available: {pygame.joystick.get_count()}")

        # 获取到指定的joystick
        self.joystick = pygame.joystick.Joystick(joystick_index)
        self.joystick.init()

        # UI初始化
        self.create_widgets()
        self.update_data()

    def create_widgets(self):
        joystick_name = self.joystick.get_name()
        ttk.Label(self.master, text=f"Joystick: {joystick_name}", font=("Arial", 14)).pack(pady=5)

        # Axes信息显示
        self.axes_labels = []
        axes_frame = ttk.LabelFrame(self.master, text="Axes", padding=10)
        axes_frame.pack(fill="x", padx=10, pady=5)

        for i in range(self.joystick.get_numaxes()):
            lbl = ttk.Label(axes_frame, text=f"Axis {i}: 0.000")
            lbl.pack(anchor='w')
            self.axes_labels.append(lbl)

        # Buttons信息显示
        self.button_labels = []
        buttons_frame = ttk.LabelFrame(self.master, text="Buttons", padding=10)
        buttons_frame.pack(fill="x", padx=10, pady=5)

        for i in range(self.joystick.get_numbuttons()):
            lbl = ttk.Label(buttons_frame, text=f"Button {i}: 0")
            lbl.pack(anchor='w')
            self.button_labels.append(lbl)

        # Hats信息显示
        self.hats_labels = []
        hats_frame = ttk.LabelFrame(self.master, text="Hats", padding=10)
        hats_frame.pack(fill="x", padx=10, pady=5)

        for i in range(self.joystick.get_numhats()):
            lbl = ttk.Label(hats_frame, text=f"Hat {i}: (0, 0)")
            lbl.pack(anchor='w')
            self.hats_labels.append(lbl)

    def update_data(self):
        pygame.event.pump()

        for i in range(self.joystick.get_numaxes()):
            axis_val = self.joystick.get_axis(i)
            self.axes_labels[i].config(text=f"Axis {i}: {axis_val:.3f}")

        for i in range(self.joystick.get_numbuttons()):
            button_val = self.joystick.get_button(i)
            self.button_labels[i].config(text=f"Button {i}: {button_val}")

        for i in range(self.joystick.get_numhats()):
            hat_val = self.joystick.get_hat(i)
            self.hats_labels[i].config(text=f"Hat {i}: {hat_val}")

        self.master.after(50, self.update_data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python joystick_gui.py <joystick_index>")
        sys.exit(1)

    try:
        joystick_index = int(sys.argv[1])
    except ValueError:
        print("Joystick index must be an integer.")
        sys.exit(1)

    root = tk.Tk()
    app = JoystickGUI(root, joystick_index)
    root.mainloop()
