import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Shadow  = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Shadow.shape('turtle')
    # Set your turtle's speed using .speed(2)
    Shadow.speed(7)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Shadow.color('blue')
    Shadow.pencolor ('green')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for turtle_shadow in range(4):
        Shadow.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        Shadow.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?


    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    Shadow.goto(-100, -193)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Shadow.fillcolor('blue')
    Shadow.begin_fill()
    Shadow.circle(100,30)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    Shadow.end_fill()
    # Draw 3 more shapes with different fill colors!
    Shadow.begin_fill()
    for i in range(4):
        Shadow.forward(100)
        Shadow.left(90)
    Shadow.end_fill()
    Shadow.forward(200)
    Shadow.fillcolor('green')
    Shadow.begin_fill()
    for i in range(4):
        Shadow.forward(100)
        Shadow.left(90)
    Shadow.end_fill()
    Shadow.forward(200)
    Shadow.fillcolor('red')
    Shadow.begin_fill()
    Shadow.circle(100, 400)
    Shadow.end_fill()



    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
