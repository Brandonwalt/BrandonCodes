## graphics1 module application assignment starter file
# TPRG 1131 Winter 2016 Week 8
# 
# Create a simple app based on the "Apple Basket" S4A exercise
# This file creates the AppleBasket class for the scene;
# the Apple class for the object that falls;
# and the Basket class for the object that catches the apple.
# The main loop reads lines from the Arduino and communicates
# with the three game objects to manage the game behaviour.
# Score is kept in the main loop and displayed in the AppleBasket object 
#
# The starter file moves the basket and makes the apple drop once,
# but the apple never detects any collision with the ground or the basket.
####


# Import the contents of the cs1graphics module (* means "wild card", everything)
from cs1graphics import *
import serial  # PySerial module to read from COM port
import time  # needed for the sleep function
import random  # Pseudo-random number generator

# Constants (needed for geometry calculations)
WIDTH=640
HEIGHT=480
BASKET_Y=420 # the basket will slide along the bottom


# The AppleBasket is the object that will draw and maintain the scene
# Add any objects to be displayed
class AppleBasket (object) :
    # Constructor
    def __init__(self):
        print("AppleBasket.__init__()")
        # New blank window
        self.paper = Canvas()

        # Modify the canvas
        self.paper.setBackgroundColor('skyBlue')
        self.paper.setWidth(640)
        self.paper.setHeight(480)
        self.paper.setTitle('Apple Basket Game')

        # Sun
        self.sun = Circle()
        self.paper.add(self.sun)

        # Move sun from the origin, make it larger and colour it yellow
        self.sun.setRadius(30)
        self.sun.setFillColor('Yellow')
        self.sun.move(50, 50)

        # Tree trunk
        self.trunk = Rectangle(60, 350, Point(300,240))
        self.trunk.setFillColor('brown')
        self.paper.add(self.trunk)

        # Grass, behind existing objects
        self.grass = Rectangle(WIDTH, 80, Point(WIDTH//2,HEIGHT-40))
        self.grass.setFillColor('green')
        self.grass.setBorderColor('green')
        self.grass.setDepth(75) # must be behind basket and trunk
        self.paper.add(self.grass)

        # Tree leaves
        self.leaves = Polygon(Point(300,50),Point(100,80),Point(50,120), \
            Point(60,140),Point(300,160),Point(540,140), \
            Point(550,120),Point(500,80))
        self.leaves.setFillColor('darkGreen')
        self.leaves.setDepth(20) # in front of trunk
        self.paper.add(self.leaves)

        # Apples in front of leaves, and move leaves further to the front
        apples = [Point(95,135), Point(125,130), Point(280,125), Point(390,140), Point(530,130)]
        for a in apples :
            circle = Circle( 10, a)
            circle.setFillColor('red')
            circle.setDepth(10)  # apple in front of leaves
            self.paper.add(circle)

        # Score will be provided by the mainloop
        # but needs to be stored before updating
        self.score = 0
        self.scorebox = Text( "Score=0", 24, Point(550,50))
        self.paper.add(self.scorebox)

    # Add a cs1graphics drawable object to be displayed
    def add(self, item):
        self.paper.add(item)
        return

    # Update the score display
    def setScore(self, s):
        self.score = s
        self.scorebox.setMessage("Score=" + str(s))

    
        

## End of class AppleBasket


## Apple is the object in motion and is responsible for detecting collisions
#  There are two collision situations: with basket, and with ground
#  Collision with basket is determined by detectCollision() called by mainloop
#  Collision with ground is handled by the routine update()
#  Apple extends Circle -- it's just a red Circle with extra methods for the game
class Apple (Circle):
    def __init__(self,pos=Point(0,0)):
        # This runs the __init__() method for the superclass, Circle
        super().__init__(12, pos)
        print("Apple.__init__(): pos =", pos)
        self.setFillColor('red')
        self.setDepth(5)
        self.speed = 10  # initial downward speed
        return
  
        
    # Update the position of the Apple object and detect collision with the ground
    def update(self,other):
        self.move(0, int(self.speed))

    ## Collision detection using bounding box 
    #  See the discussion in the tutorial
    #  
   
        
    def detectCollision(self, other):
        myRef = self.getReferencePoint()
        myRadius = self.getRadius()
        refX = myRef.getX()
        refY = myRef.getY()
        otherRef = other.getReferencePoint()
        size = other.getSize()
        otherX = otherRef.getX()
        otherY = otherRef.getY()
        myTop = (refY - myRadius)   
        myLeft = (refX - myRadius)
        myRight = (refX + myRadius) 
        myBottom =  refY + myRadius 
        otherTop = otherY - size//2 
        otherLeft = (otherX - size//2)
        otherRight = (otherX + size//2)
        otherBottom = (otherY + size//2) 
        ## determine for self:
        #  myRef, myRadius, myLeft, myRight, myTop, myBottom
        #  and for other:
        #  otherRef, otherSize, otherLeft, otherRight, otherTop, otherBottom
        #
##        if myBottom >= otherTop:
##            return True       
        
        if  \
        (myLeft <= otherRight and otherLeft <= myRight \
         and myTop <= otherBottom and otherTop <= myBottom):
            return True
        else:
            return False

    def ground(self, other):
        myRef = self.getReferencePoint()
        myRadius = self.getRadius()
        refX = myRef.getX()
        refY = myRef.getY()
        otherRef = other.getReferencePoint()
        size = other.getSize()
        otherX = otherRef.getX()
        otherY = otherRef.getY() 
        myBottom =  refY + myRadius 
        otherTop = otherY - size//2  
        otherBottom = (otherY + size//2) 
        
        
        if myBottom >= otherBottom:
            return True
        else :
            return False
        

##    if detectCollision is True:
##        self.rand =random.Random()
##        self.moveTo(self.rand.randint(50,WIDTH-50),100)
        
    def update(self):
        self.move(0,int(self.speed))
        

class BadApple (Circle):
    def __init__(self, pos=Point(0,0)):
        # This runs the __init__() method for the superclass, Circle
        super().__init__(12, pos)
        print("BadApple.__init__(): pos =", pos)
        self.setFillColor('yellow')
        self.setDepth(5)
        self.speed = 10  # initial downward speed
        return

    # Update the position of the Apple object and detect collision with the ground
    def update(self,other):
        self.move(0, int(self.speed))

    ## Collision detection using bounding box 
    #  See the discussion in the tutorial
    #  
    def Bad_detectCollision(self, other):# Assume other is a Square
        myRef = self.getReferencePoint()
        myRadius = self.getRadius()
        refX = myRef.getX()
        refY = myRef.getY()
        otherRef = other.getReferencePoint()
        size = other.getSize()
        otherX = otherRef.getX()
        otherY = otherRef.getY()
        myTop = (refY - myRadius)   
        myLeft = (refX - myRadius)
        myRight = (refX + myRadius) 
        myBottom =  refY + myRadius 
        otherTop = otherY - size//2 
        otherLeft = (otherX - size//2)
        otherRight = (otherX + size//2)
        otherBottom = (otherY + size//2) 
        ## determine for self:
        #  myRef, myRadius, myLeft, myRight, myTop, myBottom
        #  and for other:
        #  otherRef, otherSize, otherLeft, otherRight, otherTop, otherBottom
        #
##        if myBottom >= otherTop:
##            return True       
        
        if  \
        (myLeft <= otherRight and otherLeft <= myRight \
         and myTop <= otherBottom and otherTop <= myBottom):
            return True
        else:
            return False

    def Badground(self, other):
        myRef = self.getReferencePoint()
        myRadius = self.getRadius()
        refX = myRef.getX()
        refY = myRef.getY()
        otherRef = other.getReferencePoint()
        size = other.getSize()
        otherX = otherRef.getX()
        otherY = otherRef.getY() 
        myBottom =  refY + myRadius 
        otherTop = otherY - size//2 
        otherBottom = (otherY + size//2) 
        
        
        if myBottom >= otherBottom:
            return True
        else :
            return False
##    if detectCollision is True:
##        self.rand =random.Random()
##        self.moveTo(self.rand.randint(50,WIDTH-50),100)

    def update(self):
            self.move(0,int(self.speed))
        
        # if ... 
        # The left side of the apple is NOT to the right of the right side of the basket;
        # and left side of the basket is NOT to the right of the right side of the apple;
        # and top of the apple is NOT below the bottom of the basket;
        # and top of the basket is NOT below the bottom of the apple :
        
        # function is stubbed out for now, no collision detected 
            
## End class Apple


## Class to model the basket
#  Basket inherits from Square
#  The basket gets told its X position from the mainloop
#  The update method will use the X coordinate to update the location
#  The basket square can grow or shrink back to normal for the bonus round
class Basket(Square):
    def __init__(self, x=0):
        print("Basket.__init__(): x =", x)
        super().__init__(70, Point(x,BASKET_Y))
        self.x = x
        self.setFillColor('Goldenrod')
        self.setDepth(1)
        return

    def setX(self, x):
        # move the basket to x coordinate
        self.x = x
        return

    def update(self):
        # apply the motion
        self.moveTo(self.x,BASKET_Y)
        return

## End class Basket


## Main program

# Open the serial port (change the string to match your system)
ser = serial.Serial("COM3")
ser.timeout = 1  # Return an empty string if nothing received after waiting 2 seconds
print(ser)  # debug print; comment out when everything is working

# Create the scene object
app = AppleBasket()

# Create the Apple object and add it to the scene
rand = random.Random()

xap= (300,100,50,60,540,550,500)
yap = (50,80,120,140,160)

newton = Apple(Point(random.choice(xap),random.choice(yap)))
app.add(newton)

Badnewton = BadApple(Point(random.choice(xap),random.choice(yap)))
app.add(Badnewton)
# Create the Basket object and add it to the scene
bas = Basket(100)
app.add(bas)

# Initialize the score (and other state variables, as needed)

score = 1


# For debugging purposes, comment out when everything is working
#print("Pause to read init output")
#time.sleep(4)

# Reliability fix to ensure that we are in sync
# with the Arduino sendserial sketch
# Just before going to the mainloop, reset the serial input
# and do a throwaway readline() -- this will stall for up to 2 seconds
#ser.reset_input_buffer()  # use this line instead if using PySerial 3.x
ser.flushInput()  # for PySerial 2.7 (as installed on H136 workstations)
ser.readline()

while True :
    # Read the potentiometer Analog0 value in multiple steps:
    # 1) Read the byte string from the Arduino;
    # 2) convert to a Python 3 Unicode string;
    # 3) split the string into a list of four substrings;
    # 4) and finally convert list element at index=2 to an integer.
    # Comment out the printing when everything is working
    arduinoString = ser.readline()
    print(arduinoString)

    numberString = arduinoString.decode("ascii")
    print(numberString)

    numberList = numberString.split()
    print(numberList)

    basketX = int(numberList[2])
    print(basketX)

    if newton.detectCollision(bas) == True:
        score += 1
        app.setScore(score)
        print("collision")
        newton.moveTo(rand.randint(50,WIDTH-50),100)

    if newton.ground(bas) == True:
        newton.moveTo(rand.randint(50,WIDTH-50),100)

    if Badnewton.Badground(bas) == True:
        Badnewton.moveTo(rand.randint(50,WIDTH-50),100)

    if Badnewton.Bad_detectCollision(bas) == True:
        score -=1
        app.setScore(score)
        print("collision")
        Badnewton.moveTo(rand.randint(50,WIDTH-50),100)

        
    # Use the received value to set the basket X
    # (but first you need to scale 0--1023 to 0--WIDTH)
    bas.setX((basketX/1023)*640)

    # at the end of the main loop, update the objects
    newton.update()
    Badnewton.update()
    bas.update()

## End of main program
