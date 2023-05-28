import tkinter as tk
import math as m


def calc_init_pos(x0, y0, len, ang):
    x1 = x0 + len * m.sin(ang)
    y1 = y0 + len * m.cos(ang)
    return x1, y1


class Pendulum:
    g = 1

    def __init__(self, mass, len, x0, y0, ang, num):
        self.mass = mass
        self.len = len
        self.ang = ang
        self.x0 = x0
        self.y0 = y0
        self.x1, self.y1 = calc_init_pos(x0, y0, len, ang)
        self.ang_v = 0
        self.circle = None
        self.line = None
        self.num = num
        self.starting = (self.x1, self.y1, ang)
        self.objs = None

    def add_ang_v(self, amount):
        self.ang_v += amount

    def add_ang(self):
        self.ang += self.ang_v

    #FIXME see other fixme
    def create_pendulum(self, canvas):
        # TODO make radius proportional or something to mass

        self.circle = canvas.create_circle(self.x1, self.y1, 15, fill="white")
        self.line = canvas.create_line(self.x0, self.y0, self.x1, self.y1)
        self.objs = (self.circle, self.line)

    def reset_ang(self, pend0, canvas, canv):
        if self.num == 1:
            self.x0, self.y0 = pend0.x1, pend0.y1
        self.ang_v = 0

        delta_x = self.starting[0] - self.x1
        delta_y = self.starting[1] - self.y1
        self.x1 = self.starting[0]
        self.y1 = self.starting[1]
        self.ang = self.starting[2]

        canvas.move(self.circle, delta_x, delta_y)

        canvas.coords(self.line, self.x0, self.y0, self.x1, self.y1)

        canv.update_prev_coords((self.x1, self.y1), self.num)

    # FIXME ugly naming and confusing add expl and/or better naming
    def move_pend(self, prev_coord, canvas, canv):
        if self.num == 1:
            self.x0 = canv.pend0.x1
            self.y0 = canv.pend0.y1
        self.x1 = self.x0 + self.len * m.sin(self.ang)
        self.y1 = self.y0 + self.len * m.cos(self.ang)

        delta_x = self.x1 - prev_coord[0]
        delta_y = self.y1 - prev_coord[1]

        if self.num == 1:
            canv.draw_line(prev_coord[0], prev_coord[1], self.x1, self.y1)

        canv.update_prev_coords((self.x1, self.y1), self.num)

        canvas.move(self.circle, delta_x, delta_y)

        canvas.coords(self.line, self.x0, self.y0, self.x1, self.y1)


