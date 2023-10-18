# 画图，学用rectangle画方形。

from tkinter import *

canvas = Canvas(width=800, height=600, bg="white")
canvas.pack(expand=YES, fill=BOTH)

x0 = 100
y0 = 100
x1 = 200
y1 = 200

canvas.create_rectangle(x0, y0, x1, y1, fill="red") # x0 y0 为矩形左上角点 x1 y1为矩形右下角点
canvas.create_rectangle(x0 + 200, y0, x1 + 300, y1, fill="green")

mainloop()