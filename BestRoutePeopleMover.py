import random
import math
import matplotlib.pyplot as plt
import numpy as np

#Matt Hefner: Main, plot_Points, plot_Move, and comments.
#Kerry and Luca: RanCoord
#Both Michaels and Morgan: research and syntax development for matplotlib usage
#Marcia and Branden: eval_Points

X1_Point = 0  #Intialize the variables to zero
Y1_Point = 0
X2_Point = 0
Y2_Point = 0
X3_Point = 0
Y3_Point = 0

debug = False #Used to check the distance between points for debugging

def RanCoord():               #Find random numbers for the points
    global X1_Point
    global Y1_Point
    global X2_Point
    global Y2_Point
    
    X1_Point = random.randint(0,10) 

    Y1_Point = random.randint(0,10)

    X2_Point = random.randint(0,10)

    Y2_Point = random.randint(0,10)
    
def plot_Points():      #This function is used if the points are within 2 feet and plots just the points
    global X1_Point
    global Y1_Point
    global X2_Point
    global Y2_Point
    
    plt.plot([X1_Point,X2_Point], [Y1_Point,Y2_Point], 'ro')      #plots the points
    plt.axis([-1, 11, -1, 11])
    plt.text((X1_Point - 0.25), (Y1_Point + 0.25), 'P1')
    plt.text((X2_Point - 0.25), (Y2_Point + 0.25), 'P2')
    plt.title('Move the People')
    plt.show()
    
def plot_Move():             #Used to plot a line to the point that is within 2 feet of point 1
    
    plt.plot([X1_Point], [Y1_Point], 'ro')      #plots the points
    plt.axis([-1, 11, -1, 11])
    plt.text((X1_Point - 0.25), (Y1_Point + 0.25), 'P1')
    plt.title('Move the People')
    
    plt.plot([X2_Point,X3_Point], [Y2_Point,Y3_Point], 'bo--')
    plt.text((X2_Point - 0.25), (Y2_Point + 0.25), 'P2')
    plt.text((X3_Point - 0.25), (Y3_Point + 0.25), 'Move Here')
    plt.show()
    
def eval_points():       #Checks to see if the points are within 2 feet, if not calculate the new point that point 2 can move to, thus meeting the criteria
    global X3_Point
    global Y3_Point
    
    
    if ((X2_Point - X1_Point)**(2)) + ((Y2_Point - Y1_Point)**(2))**(1/2) == 0:
        RanCoord()
    elif (((X2_Point - X1_Point)**(2)) + ((Y2_Point - Y1_Point)**(2)))**(1/2) > 2:
        if (X1_Point == X2_Point and Y1_Point < Y2_Point):
            Y3_Point = Y2_Point - 2
            X3_Point = X2_Point
        if (X1_Point == X2_Point and Y1_Point > Y2_Point):
            Y3_Point = Y2_Point + 2
            X3_Point = X2_Point
        if (Y1_Point == Y2_Point and X1_Point < X2_Point):
            X3_Point = X2_Point - 2
            Y3_Point = Y2_Point
        if (Y1_Point == Y2_Point and X1_Point > X2_Point):
            X3_Point = X2_Point + 2
            Y3_Point = Y2_Point
        if (X1_Point != X2_Point and Y1_Point != Y2_Point):
            if (X2_Point > X1_Point and Y2_Point > Y1_Point):
                angle = math.atan ((X2_Point - X1_Point) / (Y2_Point - Y1_Point))
                X3_Point = X1_Point + 2*math.cos(angle)
                Y3_Point = Y1_Point + 2*math.sin(angle)
            if (X2_Point > X1_Point and Y2_Point < Y1_Point):
                angle = math.atan ((X2_Point - X1_Point) / (Y1_Point - Y2_Point))
                X3_Point = X1_Point - 2*math.cos(angle)
                Y3_Point = Y1_Point - 2*math.sin(angle)
            if (X2_Point < X1_Point and Y2_Point > Y1_Point):
                angle = math.atan ((X1_Point - X2_Point) / (Y2_Point - Y1_Point))
                X3_Point = X1_Point - 2*math.cos(angle)
                Y3_Point = Y1_Point + 2*math.sin(angle)
            if (X2_Point < X1_Point and Y2_Point < Y1_Point):
                angle = math.atan ((X1_Point - X2_Point) / (Y1_Point - Y2_Point))
                X3_Point = X1_Point - 2*math.cos(angle)
                Y3_Point = Y1_Point - 2*math.sin(angle)







def main():              #This runs the whole code together to make the program run
    global X1_Point      #Takes the variables from the start to use and evaluate
    global Y1_Point
    global X2_Point
    global Y2_Point
    global X3_Point
    global Y3_Point
    global debug
    
    RanCoord()            #Finds the random points
    
    if debug == True:
        print((((X2_Point - X1_Point)**(2)) + ((Y2_Point - Y1_Point)**(2)))**(1/2))        #checks distance
        print(X1_Point, Y1_Point)
        print(X2_Point, Y2_Point)     #checks Points
        
   
    if (((X2_Point - X1_Point)**(2)) + ((Y2_Point - Y1_Point)**(2)))**(1/2) <= 2:  #If the points are within 2 feet print the position
        plot_Points()
    elif (((X2_Point - X1_Point)**(2)) + ((Y2_Point - Y1_Point)**(2)))**(1/2) > 2:  #Double checks to make sure points are not within 2 feet of each other
        eval_points()  #runs the eval function to get a point to move to that is within 2 feet of point 1
        plot_Move()    #Plots the points where P2 is moving to a new position 2 feet from P1
        
    

   
    
    
     

    
    
    return 0          #Exits the code



main()