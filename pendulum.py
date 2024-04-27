# Program to show a circle that moves back and forth
# TPRG 1131 W2016 Test 2 Review
#
# This program was broken by introducing two problems.
# For full marks:
# 1) determine what the problems were; 
# 2) explain why they were a problem,
# 3) and make the correction.
#
from cs1graphics import *
import time

WIDTH = 320
HEIGHT = 240
paper = Canvas(WIDTH,HEIGHT)
paper.setTitle("TPRG1131 Test 2 Prep")
paper.setBackgroundColor("lightgray")

xpos = WIDTH//2
disk = Circle(30, Point(xpos,HEIGHT//2))
disk.setFillColor("red")

dx = 5
while true:
    if xpos > WIDTH - 50 or xpos < 50 :
        dx = -dx
    disk.move(dx,0)
    xpos += dx
    time.sleep(0.1) # pause 1/10 second
# end of program