from PendulumClass import Pendulum
import tkinter as tk
import math as m


class Canv:
    def __init__(self, width, height, root, prev_coords):
        self.root = root
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.pend0 = None
        self.pend1 = None
        self.should_move = False
        self.prev_coords = prev_coords
        self.lines = []
        self.pends_hidden = False

        # ---- Button functions ----
    def show_lines(self, event):
        """
        Show lines drawn to show path of bottom pendulum
        :param event: ignore
        :return: None
        """
        for i in self.lines:
            self.canvas.itemconfig(i, state="normal")

    def hide_lines(self, event):
        """
        Hide lines drawn to show path of bottom pendulum
        :param event: ignore
        :return: None
        """
        for i in self.lines:
            self.canvas.itemconfig(i, state="hidden")

    def start_stop(self):
        self.should_move = not self.should_move

    # Clear lines completely
    def clear_lines(self):
        for i in self.lines:
            self.canvas.delete(i)

    # Reset funktion av pendlar
    def reset(self):
        self.pend0.reset_ang(self.pend0, self.canvas, self)
        self.pend1.reset_ang(self.pend0, self.canvas, self)

    def hide_show_pendulum(self):
        if not self.pends_hidden:
            for obj in self.pend0.objs:
                self.canvas.itemconfig(obj, state="hidden")

            for obj in self.pend1.objs:
                self.canvas.itemconfig(obj, state="hidden")
            self.pends_hidden = True
        else:
            for obj in self.pend0.objs:
                self.canvas.itemconfig(obj, state="normal")

            for obj in self.pend1.objs:
                self.canvas.itemconfig(obj, state="normal")
            self.pends_hidden = False

    # Save image of canvas
    def save_image(self):
        pass

    @staticmethod
    def calc_acc(m1, m2, a1, a2, a1_v, a2_v, l1, l2, g):
        num1 = -g * (2 * m1 + m2) * m.sin(a1)
        num2 = -m2 * g * m.sin(a1 - 2 * a2)
        num3 = -2 * m.sin(a1 - a2) * m2
        num4 = (a2_v * a2_v) * l2 + (a1_v * a1_v) * l1 * m.cos(a1 - a2)
        den = l1 * (2 * m1 + m2 - m2 * m.cos(2 * a1 - 2 * a2))
        a1_a = (num1 + num2 + num3 * num4) / den

        num1 = 2 * m.sin(a1 - a2)
        num2 = ((a1_v * a1_v) * l1 * (m1 + m2))
        num3 = g * (m1 + m2) * m.cos(a1)
        num4 = (a2_v * a2_v) * l2 * m2 * m.cos(a1 - a2)
        den = l2 * (2 * m1 + m2 - m2 * m.cos(2 * a1 - 2 * a2))
        a2_a = (num1 * (num2 + num3 + num4)) / den

        return a1_a, a2_a

    def calc_pos(self):
        x1 = self.pend0.x0 + self.pend0.len * m.sin(self.pend0.ang)
        y1 = self.pend0.y0 + self.pend0.len * m.cos(self.pend0.ang)
        x2 = self.pend0.x1 + self.pend1.len * m.sin(self.pend1.ang)
        y2 = self.pend0.y1 + self.pend1.len * m.cos(self.pend1.ang)
        return (x1, y1), (x2, y2)

    def update(self):
        if self.should_move:
            a1_a, a2_a = Canv.calc_acc(self.pend0.mass, self.pend1.mass, self.pend0.ang, self.pend1.ang, self.pend0.ang_v, self.pend1.ang_v, self.pend0.len, self.pend1.len, Pendulum.g)
            self.pend0.add_ang_v(a1_a)
            self.pend1.add_ang_v(a2_a)
            self.pend0.add_ang()
            self.pend1.add_ang()

            self.pend0.move_pend(self.prev_coords[0], self.canvas, self)
            self.pend1.move_pend(self.prev_coords[1], self.canvas, self)

        self.canvas.after(15, self.update)

    def create_pends(self, m1, m2, l1, l2, x0, y0, x1, y1, a1, a2):
        self.pend0 = Pendulum(m1, l1, x0, y0, a1, 0)
        self.pend1 = Pendulum(m2, l2, x1, y1, a2, 1)
        self.pend0.create_pendulum(self.canvas)
        self.pend1.create_pendulum(self.canvas)

    def update_prev_coords(self, new, n):
        self.prev_coords[n] = new

    def draw_line(self, x1, y1, x2, y2):
        line = self.canvas.create_line(x1, y1, x2, y2)
        self.lines.append(line)
