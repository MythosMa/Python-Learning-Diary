# 画图，学用line画直线。

from tkinter import *

canvas = Canvas(width=800, height=600, bg="white")
canvas.pack(expand=YES, fill=BOTH)

x0 = 100
y0 = 100
x1 = 200
y1 = 200

canvas.create_line(x0, y0, x1, y1, width=1, fill="black")

mainloop()