import turtle
window=turtle.Screen()
window.tracer()
window.bgcolor('black')
turtle.hideturtle()
turtle.up
turtle.goto(0,270)
turtle.down
turtle.color('red')
turtle.write('The Maze', False,'center', ['Old English Text MT', 30, 'bold'])
#making the goal thing to reach to it to win the game
Goal=turtle.Turtle()
Goal.shape('circle')
Goal.turtlesize(1.5)
Goal.speed(0)
Goal.color('red')
Goal.up()
Goal.goto(-220,220)
Goal.down()



#Note
Note=turtle.Turtle()
Note.penup()
Note.color('cyan')
Note.hideturtle()
Note.goto(0,-300)
Note.write('Easy than you think!! :)', True, 'center', ['Old English Text MT', 20, 'bold'])
Note.pendown()




#making the thing that i can move to reach the goal to win
Person=turtle.Turtle()
Person.direction="Stop"
Person.up()
Person.speed(0)
Person.goto(215,-215)
Person.down()
Person.color('yellow')
Person.turtlesize(1.5)
Person.shape('square')

#Ending of the game
Over=turtle.Turtle()
Over.hideturtle()

Over.color('red')

#the boundary of the maze
Lines=turtle.Turtle()
Lines.speed(0)
Lines.hideturtle()
Lines.color('white')
Lines.width(5)
Lines.up()
Lines.goto(-250,-250)
Lines.down()
Lines.goto(250,-250)
Lines.goto(250,250)
Lines.goto(-250,250)
Lines.goto(-250,-250)

#making the maze lines
Maze=turtle.Turtle()
Maze.hideturtle()
Maze.color('white')
Maze.speed(0)
Maze.width(5)
Maze.up()
Maze.goto(150,-250)
Maze.down()
Maze.goto(150,-200)
Maze.goto(100,-200)
Maze.goto(100,-150)
Maze.goto(50,-150)
Maze.goto(50,-200)
Maze.goto(-50,-200)
Maze.up()
Maze.goto(-100,-250)
Maze.down()
Maze.goto(-100,-100)
Maze.up()
Maze.goto(-100,-175)
Maze.down()
Maze.goto(-175,-175)
Maze.up()
Maze.goto(-100,-125)
Maze.down()
Maze.goto(-25,-125)
Maze.up()
Maze.goto(-250,-50)
Maze.down()
Maze.goto(-10,-50)
Maze.up()
Maze.goto(-150,-50)
Maze.down()
Maze.goto(-150,10)
Maze.goto(-250,40)
Maze.up()
Maze.goto(-10,-50)
Maze.down()
Maze.goto(-10,60)
Maze.up()
Maze.goto(250,0)
Maze.down()
Maze.goto(70,0)
Maze.up()
Maze.goto(150,250)
Maze.down()
Maze.goto(150,100)
Maze.up()
Maze.goto(80,80)
Maze.down()
Maze.goto(0,80)
Maze.goto(0,160)
Maze.up()
Maze.goto(-120,250)
Maze.down()
Maze.goto(-120,80)

def up():
    Person.setheading(90)
    Person.forward(30)
    if Person.xcor() >= 250 or Person.ycor() >= 250:
        Person.up()
        Person.speed(0)
        Person.goto(215, -215)
        Person.down()
        window.clearscreen()
        window.bgcolor('black')
        Over.write('Good Luck next time :D', True, 'center', ['Old English Text MT', 20, 'bold'])
    # the winning
    if Person.distance(Goal)<30:
        window.clearscreen()
        window.bgcolor('black')
        Over.write('You Won :)', True, 'center', ['Old English Text MT', 20, 'bold'])

def down():
    Person.setheading(270)
    Person.forward(30)
    if Person.xcor() >= 250 or Person.ycor() >= 250:
        Person.up()
        Person.speed(0)
        Person.goto(215, -215)
        Person.down()
        window.clearscreen()
        window.bgcolor('black')
        Over.write('Good Luck next time :D', True, 'center', ['Old English Text MT', 20, 'bold'])
    # the winning
    if Person.distance(Goal)<30:
        window.clearscreen()
        window.bgcolor('black')
        Over.write('You Won :)', True, 'center', ['Old English Text MT', 20, 'bold'])

def left():
    Person.setheading(180)
    Person.forward(30)
    if Person.xcor() >= 250 or Person.ycor() >= 250:
        Person.up()
        Person.speed(0)
        Person.goto(215, -215)
        Person.down()
        window.clearscreen()
        window.bgcolor('black')
        Over.write('Good Luck next time :D', True, 'center', ['Old English Text MT', 20, 'bold'])
    # the winning
    if Person.distance(Goal)<30:
        window.clearscreen()
        window.bgcolor('black')
        Over.write('You Won :)', True, 'center', ['Old English Text MT', 20, 'bold'])

def right():
    Person.setheading(0)
    Person.forward(30)
    if Person.xcor() >= 250 or Person.ycor() >= 250:
        Person.up()
        Person.speed(0)
        Person.goto(215, -215)
        Person.down()
        window.clearscreen()
        window.bgcolor('black')
        Over.write('Good Luck next time :D', True, 'center', ['Old English Text MT', 20, 'bold'])
    # the winning
    if Person.distance(Goal)<30:
        window.clearscreen()
        window.bgcolor('black')
        Over.write('You Won :)', True, 'center', ['Old English Text MT', 20, 'bold'])

window.listen()
window.onkey(up, 'Up')
window.onkey(down, 'Down')
window.onkey(left, 'Left')
window.onkey(right, 'Right')

turtle.mainloop()