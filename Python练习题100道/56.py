# 画图，学用circle画圆形

from tkinter import *

canvas = Canvas(width=800, height=600, bg="white")
canvas.pack(expand=YES, fill=BOTH)

k = 1
j = 1
for i in range(0,26):
    canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1) # x0 y0 为矩形左上角点 x1 y1为矩形右下角点
    k += j
    j += 0.3
 
mainloop()