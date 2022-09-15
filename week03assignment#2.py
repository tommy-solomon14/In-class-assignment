# This is the in-class assignment for Week 03
# Create a python program that draws a traffic light!
from turtle import * # And this is another


# Inputting here.
# Processing here.
# Outputting here.

shape("turtle")
speed(10)
setup(800,800) # Setup the turtle window size

#Move to center traffic light position
penup()
goto(0,-50)

# Draw the yellow traffic light
pendown()
pensize(5)
fillcolor("yellow")
begin_fill()
circle(50)
end_fill()

#Move to top traffic light position
penup()
goto(0,90)

# Draw the red traffic light
pendown()
pensize(5)
fillcolor("red")
begin_fill()
circle(50)
end_fill()

#Move to bottom traffic light position
penup()
goto(0,-190)

# Draw the green traffic light
pendown()
pensize(5)
fillcolor("green")
begin_fill()
circle(50)
end_fill()

#Move to traffic light frame position
penup()
goto(-70,-230)
pendown()
forward(140)
left(90)
forward(460)
left(90)
forward(140)
left(90)
forward(460)

hideturtle()

# This is to stop the window from closing
done()