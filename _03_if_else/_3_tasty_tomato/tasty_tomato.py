import tkinter
import turtle
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':

    window_width = 600
    window_height = 600

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")

    canvas.grid()

    # 1. Ask the user what color tomato they would like and save their response
    #    You can give them up to three choices
    s = simpledialog.askstring('f', 'do you want your tomato red, green, or blue?')
    # 2. Use if-else statements to draw the tomato in the color that they chose
    #    You can modify the code below or draw your own tomato
    if s == 'red':
        canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="red", outline="")

        canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
    elif s == 'green':
        canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="green", outline="")

        canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
    elif s == 'blue':

        canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")

        canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

    root.mainloop()
