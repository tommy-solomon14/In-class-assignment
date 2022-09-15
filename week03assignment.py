# This is the in-class assignment for Week 03
# Create a python program that draws consecutive squares
from turtle import * # And this is another


# Inputting here.
# Processing here.
# Outputting here.

shape("turtle")
speed(1)
setup(400,600) # Setup the turtle window size

# Draw circle in center
pencolor("blue")
dot(5)
penup()

# Move to corner of inner square
goto(-50,-50)
pencolor("red")
pendown()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

# Move to corner of outer square
penup()
goto(-150,-150)

# Move to corner of outer square
pendown()
pencolor("red")
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
penup()

# Move to turtle in resting place
goto(-250,-250)

#Change color and orient upward
pencolor("blue")
left(90)

# This is here to stop the window from closing
done()