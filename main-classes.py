import tkinter as tk
import math as m
from CanvClass import Canv
from PendulumClass import Pendulum
from AppClass import MainApplication


def calc_init_pos(x0, y0, len, ang):
    x1 = x0 + len * m.sin(ang)
    y1 = y0 + len * m.cos(ang)
    return x1, y1


def _create_circle(self, x, y, r, **kwargs):
    """
    Function to create a circle relative to its center
    :param self: canvas
    :param x: x-coordinate of circle
    :param y: y-coordinate of circle
    :param r: radius of circle
    :param kwargs: optional coordinates, see canvas.create.oval()
    :return: tkinter shape
    """
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


def game_loop():
    # CONSTS
    win_width = 800
    win_height = 800
    canv_width = 800 
    canv_height = 600

    # Angles
    a1 = m.pi / 2
    a2 = 3 * m.pi / 4

    # Variables
    m1 = 40
    m2 = 40
    l1 = 150
    l2 = 150
    x0, y0 = (400, 270)
    x1, y1 = calc_init_pos(x0, y0, l1, a1)
    x2, y2 = calc_init_pos(x1, y1, l2, a2)
    prev_coords = [(x1, y1), (x2, y2)]

    tk.Canvas.create_circle = _create_circle
    main = tk.Tk()
    app = MainApplication(main, win_width, win_height, canv_width, canv_height, prev_coords)
    app.canvas.create_pends(m1, m2, l1, l2, x0, y0, x1, y1, a1, a2)
    app.canvas.update()
    main.mainloop()


if __name__ == "__main__":
    game_loop()
