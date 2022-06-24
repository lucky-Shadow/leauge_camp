import tkinter
from tkinter import messagebox, simpledialog, Tk
import math

# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
if __name__ == '__main__':
    window = Tk()

    k = simpledialog.askinteger('h', 'what is the radius of a circle')
    h = simpledialog.askstring('l', 'would you like to calculate the area or circumference of a circle?')
    if h == 'area':
        area = math.pi * k * k
        messagebox.showinfo('w', 'the area of a circle with radius ' + str(k) + ' is ' + str(area))
    elif h == 'circumference':
        f = math.pi * 2 * k
        messagebox.showinfo('s', 'the circumference of a circle with radius ' + str(k) + 'is' + str(f))
#Area = πr^2
#Circumference = 2πr 
