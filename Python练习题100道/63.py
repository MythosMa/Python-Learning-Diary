# 画椭圆。　

from tkinter import *

canvas = Canvas(width=800, height=600, bg="white")
canvas.pack(expand=YES, fill=BOTH)

x0, y0 = 300, 200
x1, y1 = 500, 400

canvas.create_rectangle(x0, y0, x1, y1) # x0 y0 为矩形左上角点 x1 y1为矩形右下角点
canvas.create_oval(x0, y0, x1, y1, fill="red") # 圆为以左上角点和右下角点内部填充的图案

canvas.create_rectangle(x0 + 50, y0 - 100, x1 - 50, y1 + 100) # x0 y0 为矩形左上角点 x1 y1为矩形右下角点
canvas.create_oval(x0 + 50, y0 - 100, x1 - 50, y1 + 100, fill="red") # 圆为以左上角点和右下角点内部填充的图案

mainloop()
