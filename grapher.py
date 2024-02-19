from turtle import *
import math
import numpy as np
print("test")
speed(0)
hideturtle()
tracer(0)

startPoint = -300.0
endPoint = 300.0
drawing = False

funcs = []

def function(x, string):
    string = funcEntry.get()
    string = string.replace("^", "**")
    string = string.replace("x", "(x)")
    string = string.replace("x", str(x))
    return eval(string)
    #return (0.5*x*x*x + 10*x*x + x)
    #return x*5000000000 and 30/x 

def draw(funcs, drawing, zoom, zoomy, startPoint, endPoint):
    if (drawing == False):
        clear()
        axis(startPoint, endPoint)
        drawing = True
        print(funcs)
        for i in range(len(funcs)):
            fString = funcs[i].get()
            penup()
            goto(startPoint, function(startPoint, fString))
            pendown()
            for x in np.arange(startPoint, endPoint, 0.8):
                goto(x, function(x / zoom, fString) * zoomy)

        drawing = False
        update()

#tkinter window
import tkinter as tk
window = tk.Tk()
window.title = "grapher"
zoomLable = tk.Label(window, text="Zoom:")
zoomLable.grid(row = 1, column = 0)

zoomxInput = tk.Entry(window)
zoomxInput.grid(row = 1, column = 1)
zoomxInput.insert(0, "1")

zoomyInput = tk.Entry(window)
zoomyInput.grid(row = 1, column = 2)
zoomyInput.insert(0, "1")

#zoom in or out buttonsdfasdfs
zoomxInButton = tk.Button(window, text="+", command=lambda: changeZoom(1, 0))
zoomxInButton.grid(row = 0, column = 1)

zoomyInButton = tk.Button(window, text="+", command=lambda: changeZoom(0, 1))
zoomyInButton.grid(row = 0, column = 2)

zoomxOutButton = tk.Button(window, text="-", command=lambda: changeZoom(-1, 0))
zoomxOutButton.grid(row = 2, column = 1)

zoomyOutButton = tk.Button(window, text="-", command=lambda: changeZoom(0, -1))
zoomyOutButton.grid(row = 2, column = 2)

zoomInButton = tk.Button(window, text="+", command=lambda: changeZoom(1, 1))
zoomInButton.grid(row = 0, column = 3)

zoomOutButton = tk.Button(window, text="-", command=lambda: changeZoom(-1, -1))
zoomOutButton.grid(row = 2, column = 3)

drawButton = tk.Button(window, text = "Draw", command=lambda: draw(funcs, drawing, float(zoomxInput.get()), float(zoomyInput.get()), startPoint, endPoint))
drawButton.grid(row = 3, column = 0)

#Entry field for the function of the graph
funcEntry = tk.Entry(window)
funcEntry.grid(column = 4, row = 0)
funcs.append(funcEntry)

def newFunc():
    addedFunc = tk.Entry(window)
    addedFunc.grid(column = 4, row = len(funcs))
    funcs.append(addedFunc)
    addFunc.grid(column = 4, row = (len(funcs) + 1))
    addedFunc.bind("<KeyRelease>", lambda *args: draw(funcs, drawing, float(zoomxInput.get()), float(zoomyInput.get()), startPoint, endPoint))

addFunc = tk.Button(window, text="add function", command=newFunc)
addFunc.grid(column = 4, row = 1)


#draw axis
def axis(startPoint, endPoint):
    penup()
    goto(startPoint, 0)
    pendown()
    goto(endPoint, 0)
    penup()
    goto(0, startPoint)
    pendown()
    goto(0, endPoint)

axis(startPoint, endPoint)
update()

def changeZoom(x, y):
    zoomx = float(zoomxInput.get())
    zoomx += x

    zoomy = float(zoomyInput.get())
    zoomy += y

    zoomxInput.delete(0, tk.END)
    zoomxInput.insert(0, zoomx)

    zoomyInput.delete(0, tk.END)
    zoomyInput.insert(0, zoomy)
    draw(funcs, drawing, zoomx, zoomy, startPoint, endPoint)

#making it so

zoomxInput.bind("<KeyRelease>", lambda *args: draw(funcs, drawing, float(zoomxInput.get()), float(zoomyInput.get()), startPoint, endPoint))
zoomyInput.bind("<KeyRelease>", lambda *args: draw(funcs, drawing, float(zoomxInput.get()), float(zoomyInput.get()), startPoint, endPoint))
funcEntry.bind("<KeyRelease>", lambda *args: draw(funcs, drawing, float(zoomxInput.get()), float(zoomyInput.get()), startPoint, endPoint))

mainloop()
