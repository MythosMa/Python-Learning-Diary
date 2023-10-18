# 利用 ellipse 和 rectangle 画图

from tkinter import *

canvas = Canvas(width=800, height=600, bg="white")
canvas.pack(expand=YES, fill=BOTH)

rectX0, rectY0 = 10, 10
rectX1, rectY1 = 100, 100

for i in range(10):
    canvas.create_rectangle(rectX0 + i * 10, rectY0 + i * 10, rectX0 + 100 - i * 10, rectY0 + 100 - i * 10)
    canvas.create_rectangle(rectX1 + i * 4, rectY1 + i * 4, rectX1 + 500 - i * 40, rectY1 + 500 - i * 40)

x0, y0 = 600, 200
x1, y1 = 800, 400

canvas.create_rectangle(x0, y0, x1, y1) # x0 y0 为矩形左上角点 x1 y1为矩形右下角点
canvas.create_oval(x0, y0, x1, y1, fill="red") # 圆为以左上角点和右下角点内部填充的图案

canvas.create_rectangle(x0 + 50, y0 - 100, x1 - 50, y1 + 100) # x0 y0 为矩形左上角点 x1 y1为矩形右下角点
canvas.create_oval(x0 + 50, y0 - 100, x1 - 50, y1 + 100, fill="red") # 圆为以左上角点和右下角点内部填充的图案

mainloop()