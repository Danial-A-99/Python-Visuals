import turtle
import random


side1 = [-200,0]
side2 = [200,0]
side3 = [0,400]

t = turtle.Turtle()
t.speed(0)

t.goto(side1)
t.goto(side2)
t.goto(side3)
t.goto(side1)

visitedx = []
visitedy = []

randomx = random.randrange(-200,200)
randomy = random.randrange(0,400)
t.dot(4,"black")
while True:
    randomcorner = random.randrange(1,4)
    if randomcorner == 1:
        x,y = side1[0],side1[1]
    elif randomcorner == 2:
        x,y = side2[0],side2[1]
    elif randomcorner == 3:
        x,y = side3[0],side3[1]

    randomx = (randomx + x)/2
    randomy = (randomy + y)/2
    t.penup()
    t.goto([randomx,randomy])
    t.pendown()
    t.dot(4,"black")

        
    
    


turtle.done()
