import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    ryan = turtle.Turtle()
    ryan.shape('turtle')
    ryan.color('green')
    # ask what shape they want to draw and store it in a variable
    h = simpledialog.askstring('k', 'what shape do you want to draw')
    # Draw the shape requested by the user using if-elif-else statements
    if h == 'square':
        for i in range(4):
            ryan.forward(100)
            ryan.left(90)
    elif h == 'rectangle':
        for i in range(2):
            ryan.forward(300)
            ryan.left(90)
            ryan.forward(100)
            ryan.left(90)
    elif h == 'circle':
        ryan.circle(100, 356)
    else:
        for i in range(3):
            ryan.forward(100)
            ryan.left(120)
    # Call the turtle .done() method
    turtle.done()
