'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time
import math

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  """
  Creates the screen
  takes a turtle, and 3 integer values for the top left x and y and width values
  """
  myturtle.setworldcoordinates(top_left_x, top_left_y-width, top_left_x+width, top_left_y)
  myturtle.bgcolor("brown")
  plane = turtle.Turtle()
  plane.hideturtle()
  plane.up()
  plane.goto(top_left_x,top_left_y)
  plane.down()
  plane.goto(top_left_x, top_left_y-width)
  plane.goto(top_left_x+width, top_left_y-width)
  plane.goto(top_left_x+width, top_left_y)
  plane.goto(top_left_x,top_left_y)
  
def drawLine(myturtle=None, x_start=-1, y_start=-1, x_end=1, y_end=1):
  """
  Draws a horizontal and then vertical axis.
  Takes a turtle and the starting and ending x and y coordinates.
  """
  #myturtle.hideturtle()
  myturtle.up()
  myturtle.goto(x_start,0)
  myturtle.down()
  myturtle.goto(x_end,0)
  myturtle.up()
  myturtle.goto(0,y_start)
  myturtle.down()
  myturtle.goto(0,y_end)


def drawCircle(myturtle=None, radius=0):
  """
  Draws a circle.
  Takes a turtle and a radius as an integer value.
  """
  #myturtle.hideturtle()
  myturtle.goto(0,-radius)
  myturtle.circle(radius)
  
  
def setUpDartboard(myscreen=None, myturtle=None): 
  """
  Sets up the screen.
  Takes a screen and a turtle
  """
  drawSquare(myscreen, 2, -1, 1)
  drawLine(myturtle, -1, 0, 1, 0)
  drawLine(myturtle, 0, -1, 0, 1)
  drawCircle(myturtle, 1)


def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  """
  Checks if a dart thrown is in the circle.
  Takes the circle center coordinates and radius as an integer and a turtle.
  """
  distance = myturtle.distance(circle_center_x,circle_center_y)
  if distance < 1:
    #print(distance)
    return True
  else:
    #print(distance)
    return False
  
def throwDart(myturtle=None):
  """
  Places a point, simulating a dart throw
  Takes a turtle
  """
  xcoor = random.uniform(-1,1)
  ycoor = random.uniform(-1,1)
  myturtle.up()
  myturtle.speed(0)
  myturtle.goto(xcoor,ycoor)
  if isInCircle(myturtle, 0, 0, 1):
    myturtle.dot(5, "Black")
    return 1
  else:
    myturtle.dot(5, "White")
    return 0
  
def playDarts(myturtle=None):
  """
  Simulates the card game.
  Takes a turtle
  """
  pointsp1 = 0
  pointsp2 = 0
  for x in range (10):
    throwDart(myturtle)
    if throwDart(myturtle)==1:
      pointsp1+=1
    throwDart(myturtle)
    if throwDart(myturtle)==1:
      pointsp2+=1
  print("Player 1 Score: " + str(pointsp1))
  print("Player 2 Score " + str(pointsp2))
        
def montePi(myturtle=None, num_darts=0):
  """
  Throws a user-specified number of darts, and uses a miss/throw ratio to calculate the value of pi.
  Takes a number of darts to be thrown and a turtle.
  """
  accumulator = 0
  total = 0
  for x in range (num_darts):
    throwDart(myturtle)
    inside_circle = myturtle.distance(0,0)
    total += 1
    if inside_circle < 1:
      accumulator+=1
  estimation = (accumulator/total) * 4
  return estimation
      
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main provided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
