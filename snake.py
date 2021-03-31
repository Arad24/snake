######################
#       Imports      #
######################

import turtle
import random
import time
import winsound

######################
#        Defim       #
######################

######################
#      New Snake     #
######################
# Add a new snake
def NewSnake():
    new_snake = turtle.Turtle()
    new_snake.color('black')
    new_snake.shape('square')
    new_snake.speed(0)
    new_snake.penup()
    snake.append(new_snake)

def NewToHead():
    # Move the end snake to the head
    for i in range(len(snake)-1, 0, -1):
        SnakeX = snake[i-1].xcor()
        SnakeY = snake[i-1].ycor()
        snake[i].goto(SnakeX,SnakeY)

    #Move snake 0 to the head
    if len(snake) > 0:
        SnakeX = head.xcor()
        SnakeY = head.ycor()
        snake[0].goto(SnakeX,SnakeY)


# check if the snake eat the food
def checkapCrash():
    global sc
    if (head.distance(ap)<20):
        # Play Sound
        winsound.PlaySound('eat.wav', winsound.SND_ASYNC)
        locateap()
        NewSnake()
        sc += 10
        updateScore()


######################
#        Food        #
######################
# Set a food in random location
def locateap():
    x=random.randint(-260, 260)
    y=random.randint(-250,230)
    ap.goto(x,y)

######################
#     Move Snake     #
######################
# Set Keys
def SnakeMove():
    if head.direction == 'left':
        headX = head.xcor()
        head.setx(headX-15)
    if head.direction == 'right':
        headX = head.xcor()
        head.setx(headX+15)
    if head.direction == 'up':
        headY = head.ycor()
        head.sety(headY+15)
    if head.direction == 'down':
        headY = head.ycor()
        head.sety(headY-15)

def leftArrow():
    if head.direction != "right":
        head.direction = 'left'
def rightArrow():
    if head.direction != "left":
        head.direction = 'right'
def upArrow():
    if head.direction != "down":
        head.direction = 'up'
def downArrow():
    if head.direction != "up":
        head.direction = 'down'


######################
#   Check if u lost  #
######################

# Check if u touched the wall
def CheckWall():
    if head.xcor()<=-280 or head.xcor()>=270 or head.ycor()<=-260 or head.ycor()>=240:
        time.sleep(1)
        # Stop the snake
        head.goto(1000, 1000)
        # Clear the snake
        for i in snake:
            i.goto(1000,1000)
        snake.clear()
        # Show buttons
        ex.showturtle()
        res.showturtle()
        # Onclick buttons
        ex.onclick(exitGame)
        res.onclick(restartGame)

# Check if u touched the body
def CheckHead():
    for i in snake[2:]:
        if (i.distance(head) < 15):
            time.sleep(1)
            # Stop the snake
            head.goto(1000, 1000)
            # Clear the snake
            for i in snake:
                i.goto(1000,1000)
            snake.clear()
            # Show buttons
            ex.showturtle()
            res.showturtle()
            # Onclick buttons
            ex.onclick(exitGame)
            res.onclick(restartGame)

######################
#    Update Score    #
######################

def updateScore():
    global sc
    global bs

    if sc>bs:
        bs=sc

    score.clear()
    score.write("Score: %s  Best Score: %s" %(sc, bs), align="center", font=("Courier", 16, "normal"))

######################
#         Map        #
######################

def writeMap():
    map.setpos(-280,240)
    map.pendown()
    for i in range(2):
        map.fd(550)
        map.right(90)
        map.fd(500)
        map.right(90)

######################
#    Exit Screen     #
######################
# Close screen
def exitGame(x,y):
    screen.bye()

# Restart game
def restartGame(x,y):
    global sc
    # Hide buttons
    ex.hideturtle()
    res.hideturtle()
    # Return the head to 0,0 and stop him
    head.goto(0,0)
    head.direction = 'stop'

    # Clear the snake
    for i in snake:
        i.goto(1000,1000)
    snake.clear()

    # Rest score
    sc = 0
    updateScore()
    # Fix Bug
    NewSnake()


######################
#    Main Program    #
######################

if __name__ == '__main__':
    ###### create screen ######
    screen = turtle.Screen()
    screen.title('Arad Snake Game')
    screen.bgcolor('green')
    screen.setup(width=0.3, height=0.5)
    screen.tracer(0)
    ###### create snake head ######
    head = turtle.Turtle()
    head.color('black')
    head.penup()
    head.shape('square')
    head.setpos(0,0)
    head.direction = ''
    snake = []
    ###### create apple ######
    ap=turtle.Turtle()
    ap.shape('circle')
    ap.color('red')
    ap.penup()
    ###### Create Score Turtle ######
    # Score turtle
    score = turtle.Turtle()
    score.color("white")
    score.penup()
    score.hideturtle()
    score.goto(0, 245)
    score.write("Score: 0  Best Score: 0", align="center", font=("Courier", 16, "normal"))
    # Score number
    sc = 0
    bs = 0
    ###### Create Map Turtle ######
    map = turtle.Turtle()
    map.color("white")
    map.penup()
    map.hideturtle()
    ###### Create buttons ######
    ex = turtle.Turtle()
    res = turtle.Turtle()
    screen.addshape('exit.gif')
    screen.addshape('restart.gif')
    ex.shape('exit.gif')
    res.shape('restart.gif')
    ex.penup()
    res.penup()
    ex.hideturtle()
    res.hideturtle()
    ex.goto(70,0)
    res.goto(-70,0)

    ##### call functions######
    locateap()
    writeMap()
    NewSnake()

    ###### delay ######
    delay = 0.1

    ##### Onkeys #####
    turtle.onkey(downArrow, 'Down')
    turtle.onkey(upArrow, 'Up')
    turtle.onkey(leftArrow, 'Left')
    turtle.onkey(rightArrow, 'Right')
    turtle.listen()

    while True:
        screen.update()
        ##### Calls functions #####
        SnakeMove()
        checkapCrash()
        NewToHead()
        CheckWall()
        CheckHead()

        time.sleep(delay)
    screen.mainloop()