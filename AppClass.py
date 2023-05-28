from CanvClass import Canv
import tkinter as tk


class MainApplication:
    def __init__(self, root, width, height, c_width, c_height, prev_coords):
        self.root = root
        self.root.title("Double Pendulum")
        self.root.resizable(False, False)
        self.root.geometry(f"{width}x{height}")
        self.root.configure(bg="turquoise")
        self.canvas = Canv(c_width, c_height, root, prev_coords)
        self.frame = tk.Frame(root, height=200, width=790, bg="turquoise", pady= 10)
        self.frame.pack(side="bottom", padx=5)
        self.stop_button = tk.Button(self.frame, text="START/STOP", width=10, height=4, command=self.canvas.start_stop)
        self.reset_button = tk.Button(self.frame, text="RESET", width=10, height=4, command=self.canvas.reset)
        self.button3 = tk.Button(self.frame, text="HIDE/SHOW", width=10, height=4,
                                 command=self.canvas.hide_show_pendulum)
        self.button4 = tk.Button(self.frame, text="CLEAR LINES", width=10, height=4, command=self.canvas.clear_lines)

        self.stop_button.grid(column=1, row=1)
        self.reset_button.grid(column=2, row=1)
        self.button3.grid(column=1, row=2)
        self.button4.grid(column=2, row=2)

