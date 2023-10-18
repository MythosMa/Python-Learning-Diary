# 一个最优美的图案

from tkinter import *
from math import *

canvas = Canvas(width=800, height=600, bg="white")
canvas.pack(expand=YES, fill=BOTH)

circleX, circleY = 400, 300

def drawCircle():
    canvas.create_oval(circleX - 25, circleY - 25, circleX + 25, circleY + 25) # 圆为以左上角点和右下角点内部填充的图案
    canvas.create_oval(circleX - 50, circleY - 50, circleX + 50, circleY + 50) # 圆为以左上角点和右下角点内部填充的图案
    canvas.create_oval(circleX - 75, circleY - 75, circleX + 75, circleY + 75) # 圆为以左上角点和右下角点内部填充的图案

def drawTrangle_1():
    line_1_x0, line_1_y0, line_1_x1, line_1_y1 = 400, 100, 380, 200 
    canvas.create_line(line_1_x0, line_1_y0, line_1_x1, line_1_y1, width=1, fill="black")
    
    line_2_x0, line_2_y0, line_2_x1, line_2_y1 = 380, 200, 420, 200
    canvas.create_line(line_2_x0, line_2_y0, line_2_x1, line_2_y1, width=1, fill="black")
    
    line_3_x0, line_3_y0, line_3_x1, line_3_y1 = 420, 200, 400, 100 
    canvas.create_line(line_3_x0, line_3_y0, line_3_x1, line_3_y1, width=1, fill="black")

def drawTrangle_2():
    line_1_x0, line_1_y0, line_1_x1, line_1_y1 = 400, 500, 380, 400 
    canvas.create_line(line_1_x0, line_1_y0, line_1_x1, line_1_y1, width=1, fill="black")
    
    line_2_x0, line_2_y0, line_2_x1, line_2_y1 = 380, 400, 420, 400
    canvas.create_line(line_2_x0, line_2_y0, line_2_x1, line_2_y1, width=1, fill="black")
    
    line_3_x0, line_3_y0, line_3_x1, line_3_y1 = 420, 400, 400, 500 
    canvas.create_line(line_3_x0, line_3_y0, line_3_x1, line_3_y1, width=1, fill="black")

def drawTrangle_3():
    line_1_x0, line_1_y0, line_1_x1, line_1_y1 = 200, 300, 300, 280 
    canvas.create_line(line_1_x0, line_1_y0, line_1_x1, line_1_y1, width=1, fill="black")
    
    line_2_x0, line_2_y0, line_2_x1, line_2_y1 = 300, 280, 300, 320
    canvas.create_line(line_2_x0, line_2_y0, line_2_x1, line_2_y1, width=1, fill="black")
    
    line_3_x0, line_3_y0, line_3_x1, line_3_y1 = 300, 320, 200, 300 
    canvas.create_line(line_3_x0, line_3_y0, line_3_x1, line_3_y1, width=1, fill="black")

def drawTrangle_4():
    line_1_x0, line_1_y0, line_1_x1, line_1_y1 = 600, 300, 500, 280 
    canvas.create_line(line_1_x0, line_1_y0, line_1_x1, line_1_y1, width=1, fill="black")
    
    line_2_x0, line_2_y0, line_2_x1, line_2_y1 = 500, 280, 500, 320
    canvas.create_line(line_2_x0, line_2_y0, line_2_x1, line_2_y1, width=1, fill="black")
    
    line_3_x0, line_3_y0, line_3_x1, line_3_y1 = 500, 320, 600, 300 
    canvas.create_line(line_3_x0, line_3_y0, line_3_x1, line_3_y1, width=1, fill="black")

def drawTrangle_5():
    line_1_x0, line_1_y0, line_1_x1, line_1_y1 = 300, 200, 400 - sqrt(5000) - 10, 300 - sqrt(5000) + 10
    canvas.create_line(line_1_x0, line_1_y0, line_1_x1, line_1_y1, width=1, fill="black")
    
    line_2_x0, line_2_y0, line_2_x1, line_2_y1 = 400 - sqrt(5000) - 10, 300 - sqrt(5000) + 10, 400 - sqrt(5000) + 10, 300 - sqrt(5000) - 10
    canvas.create_line(line_2_x0, line_2_y0, line_2_x1, line_2_y1, width=1, fill="black")
    
    line_3_x0, line_3_y0, line_3_x1, line_3_y1 = 400 - sqrt(5000) + 10, 300 - sqrt(5000) - 10, 300, 200 
    canvas.create_line(line_3_x0, line_3_y0, line_3_x1, line_3_y1, width=1, fill="black")

def drawTrangle_6():
    line_1_x0, line_1_y0, line_1_x1, line_1_y1 = 500, 200, 400 + sqrt(5000) - 10, 300 - sqrt(5000) - 10
    canvas.create_line(line_1_x0, line_1_y0, line_1_x1, line_1_y1, width=1, fill="black")
    
    line_2_x0, line_2_y0, line_2_x1, line_2_y1 = 400 + sqrt(5000) - 10, 300 - sqrt(5000) - 10, 400 + sqrt(5000) + 10, 300 - sqrt(5000) + 10
    canvas.create_line(line_2_x0, line_2_y0, line_2_x1, line_2_y1, width=1, fill="black")
    
    line_3_x0, line_3_y0, line_3_x1, line_3_y1 = 400 + sqrt(5000) + 10, 300 - sqrt(5000) + 10, 500, 200
    canvas.create_line(line_3_x0, line_3_y0, line_3_x1, line_3_y1, width=1, fill="black")

def drawTrangle_7():
    line_1_x0, line_1_y0, line_1_x1, line_1_y1 = 500, 400, 400 + sqrt(5000) + 10, 300 + sqrt(5000) - 10
    canvas.create_line(line_1_x0, line_1_y0, line_1_x1, line_1_y1, width=1, fill="black")
    
    line_2_x0, line_2_y0, line_2_x1, line_2_y1 = 400 + sqrt(5000) + 10, 300 + sqrt(5000) - 10, 400 + sqrt(5000) - 10, 300 + sqrt(5000) + 10
    canvas.create_line(line_2_x0, line_2_y0, line_2_x1, line_2_y1, width=1, fill="black")
    
    line_3_x0, line_3_y0, line_3_x1, line_3_y1 = 400 + sqrt(5000) - 10, 300 + sqrt(5000) + 10, 500, 400
    canvas.create_line(line_3_x0, line_3_y0, line_3_x1, line_3_y1, width=1, fill="black")

def drawTrangle_8():
    line_1_x0, line_1_y0, line_1_x1, line_1_y1 = 300, 400, 400 - sqrt(5000) + 10, 300 + sqrt(5000) + 10
    canvas.create_line(line_1_x0, line_1_y0, line_1_x1, line_1_y1, width=1, fill="black")
    
    line_2_x0, line_2_y0, line_2_x1, line_2_y1 = 400 - sqrt(5000) + 10, 300 + sqrt(5000) + 10, 400 - sqrt(5000) - 10, 300 + sqrt(5000) - 10
    canvas.create_line(line_2_x0, line_2_y0, line_2_x1, line_2_y1, width=1, fill="black")
    
    line_3_x0, line_3_y0, line_3_x1, line_3_y1 = 400 - sqrt(5000) - 10, 300 + sqrt(5000) - 10, 300, 400
    canvas.create_line(line_3_x0, line_3_y0, line_3_x1, line_3_y1, width=1, fill="black")

drawCircle()
drawTrangle_1()
drawTrangle_2()
drawTrangle_3()
drawTrangle_4()
drawTrangle_5()
drawTrangle_6()
drawTrangle_7()
drawTrangle_8()

mainloop()