#Alannah Steck
#U3 Project
#tree
#Good Luck Bunny has been banished by turtle :,( We live in a sean-ciety
import turtle
from random import choice, 
t = turtle.Turtle()

"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""
t.speed(1)

def recursiveTurtle(size=6,amountDrawn = 70,angle = 90,):
  if amountDrawn != 10:
    t.lt(angle)
    t.pensize(size)
    t.forward(amountDrawn)
    print("About to recurse")
    recursiveTurtle(size-1, amountDrawn-10,45)
    recursiveTurtle(size-1, amountDrawn-10,-45)
    t.backward(amountDrawn)
    t.rt(angle)


  
  else:
    print("Base Case")
    t.lt(angle)
    t.pensize(10)
    colors = ['#ff7034','#e6652f','#cc5a2a','#b34e24','#99431f']
    t.color(choice(colors))
    t.forward(amountDrawn)
    t.backward(amountDrawn)
    t.color('#4d2210')
    t.pensize(size)
    t.rt(angle)

def main():
  t.color('#4d2210')
  t.pensize(7)
  recursiveTurtle()
  turtle.mainloop()

if __name__ == "__main__":
  main()