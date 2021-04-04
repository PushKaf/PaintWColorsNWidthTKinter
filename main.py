from tkinter import *


curX, curY = 0, 0
colors = ["black", "gray", "darkslategray", "slategray", "gray", "lightgrey", "blue", "royalblue", "dodgerblue", "deepskyblue1", "cyan2", "seagreen1", "green", "green2", "limegreen", "red", "orangered", "indianred1", "yellow", "gold", "orange"]
currColor = "black"
lineWidth = 1
def locXY(event):
    global curX, curY
    curX, curY = event.x, event.y
    # print(curX, curY)

def addLine(event):
    global curX, curY, lineWidth
    canvas.create_line((curX, curY, event.x, event.y), fill=currColor, width=lineWidth)
    curX, curY = event.x, event.y

def createColors():
    x, y, x1, y1 = 10, 10, 35, 35
    for color in colors:
        colorRect = canvas.create_rectangle((x, y, x1, y1), fill=color)
        bindTag(colorRect ,color)
        y+=30  
        y1+=30

def lineWidthChange(w):
    global lineWidth
    lineWidth = w


#NOTE I tried to do this in the for loop, but didnt really work...

def bindTag(rect, color):
    canvas.tag_bind(rect, "<Button-1>", lambda x: changeColor(color))

def changeColor(newColor):
    global currColor
    currColor = newColor

root = Tk()
root.title("Pain(t) Pog!")
root.state("zoomed")
# root.geometry("1280x720")
# root.resizable(False, False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

canvas.bind("<Button-1>", locXY)
canvas.bind("<B1-Motion>", addLine)

createColors()
sizeButton = Scale(canvas, from_=1, to=100, command=lineWidthChange)
sizeButton.place(x=0, y=700)
# canvas.create_line(20, 60, 40,60)


root.mainloop()