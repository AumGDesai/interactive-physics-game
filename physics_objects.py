"""
Aum Desai
Fall 2022
CS152B Project 08

This program is for Project 08. It creates a parent class called thing. Then it can
create other objects via inheritance.
This file can be run by putting python3 physics_objects.py in the terminal.
"""

import graphicsPlus as gr

class Thing():
    '''
    Parent Class: Thing
    '''

    def __init__(self, win, the_type):
        self.type = the_type
        self.mass = 1
        self.pos = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.elasticity = 0
        self.scale = 10
        self.win = win
        self.vis = []
        self.color = (0,0,0)
        self.drawn = False

    # method to return the object's position

    def getPosition(self):

        '''
        This method will return the object's position
        Input: Nothing
        Output: The object's position
        '''

        return self.pos[:]


    #  method to return the object's velocity
    def getVelocity(self):
        '''
        method will return the object's current velocity
        :return: A list of x and y velocity of the object
        '''
        return self.velocity[:]


    #  method to return the object's acceleration
    def getAcceleration(self):
        '''
        method will get the object's acceleration
        :return: Object's acceleration, horizontally and vertically
        '''
        return self.acceleration[:]

    #  method to return the object's elasticity
    def getElasticity(self):
        '''
        method will get the object's elasticity
        :return: Object's elasticity
        '''
        return self.elasticity


    # method to return the object's scale

    def getScale(self):
        '''
        method will get the object's scale
        :return: Object's elasticity
        '''
        return self.scale


    #  method to return the object's color

    def getColor(self):
        '''
        method will get the object's elasticity
        :return: Object's rgb color
        '''
        return self.color


    #  method to return the object's mass
    def getMass(self):
        '''
        method will set the object's mass
        :return: Object's mass
        '''
        return self.mass


    # Creating a method to return the object's mass
    def getType(self):
        '''
        method will set the object's type
        :return: Object's type
        '''
        return self.type


    # Creating a method to draw the object onto the window
    def draw(self):
        '''
        method will draw the object onto the window
        Input: Nothing
        Output: Objects drawn onto the window
        '''
        for item in self.vis:
            item.draw(self.win)

        self.drawn = True


    # method to undraw the object onto the window
    def undraw(self):
        '''
        This method will undraw the object onto the window
        Input: Nothing
        Output: Objects undrawn onto the window
        '''
        for item in self.vis:
            item.undraw(self.win)

        self.drawn = False


    # method to set the object's initial velocity
    def setVelocity(self, vx, vy):
        """
        method will set the object's velocity
        :param vx: New horizontal velocity
        :param vy: New vertical velocity
        :return: Change to new velocity
        """
        self.velocity[0] = vx
        self.velocity[1] = vy


    # method to set the object's initial acceleration
    def setAcceleration(self, ax, ay):
        """
        method will set the object's acceleration
        :param vx: New horizontal acceleration
        :param vy: New vertical acceleration
        :return: Change to new acceleration
        """
        self.acceleration[0] = ax
        self.acceleration[1] = ay


    #  method to set the object's mass
    def setMass(self, m):
        """
        This method allows user to set the mass of the object
        :param m: Mass of object
        :return: Nothing
        """
        self.mass = m


    #  method to set the object's elasticity
    def setElasticity(self, e):
        """
        This method allows user to set the elasticity of the object
        :param e: Elasticity of object
        :return: Nothing
        """
        self.elasticity = e



    #  method to set the object's initial position
    def setPosition(self, px, py):
        """
        This method will set the object's initial position
        :param px: The new x-position
        :param py: The new y-position
        :return: Move the object px and py
        """
        x_old = self.pos[0]
        y_old = self.pos[1]

        self.pos[0] = px
        self.pos[1] = py

        dx = (px - x_old) * self.scale
        dy = (py - y_old) * self.scale * (-1)

        for item in self.vis:
            item.move(dx, dy)


    #  method to set the color of an object
    def setColor(self, c):
        """
        This method will set the color of the object
        :param c: New color
        :return: Nothing
        """
        self.color = c

        if c != None:
            for item in self.vis:
                item.setFill((gr.color_rgb(c[0],c[1],c[2])))


    #  method to update the object every time
    def update(self, dt):
        """
        This method will update the position of the object based on the given velocities and acceleration every dt time
        period
        :param dt: time period
        :return: Nothing
        """
        

        x_old = self.pos[0]
        y_old = self.pos[1]

        x_vel = self.velocity[0]
        x_acc = self.acceleration[0]

        y_vel = self.velocity[1]
        y_acc = self.acceleration[1]

    

        self.pos[0] = x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.pos[1] = y_old + y_vel*dt + 0.5*y_acc * dt*dt

        x_new = self.pos[0]
        y_new = self.pos[1]

        # assign to dx the change in the x position times the scale factor (self.scale)
        # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        # for each item in self.vis
            # call the move method of the graphics object with dx and dy as arguments..

        dx = (x_new - x_old) * self.scale
        dy = (y_new - y_old) * self.scale * (-1)

        for item in self.vis:
            item.move(dx, dy)

    

        self.velocity[0] = x_acc * dt + x_vel
        self.velocity[1] = y_acc * dt + y_vel




# Defining a Ball class

class Ball(Thing):
    def __init__(self, win, radius=3, color=(0, 0, 0)):
        Thing.__init__(self, win, "ball")
        self.radius = radius
        self.refresh()
        self.setColor(color)
        self.win = win

    def refresh(self):
        """
        Defining a method to set the vis list
        :param win:
        :return:
        """
        # assign to a local variable(e.g. drawn)the value of self.drawn
        drawn = self.drawn



        if drawn == True:
            self.undraw()

        #define the self.vis list of graphics objects using the current position, radius, and window
        self.vis = [gr.Circle(gr.Point(self.pos[0] * self.scale, self.win.getHeight() - self.pos[1] * self.scale),
                              self.radius * self.scale)]

    

        if drawn == True:
            self.draw()

    # Method to return radius of ball
    def getRadius(self):
        """
        Defining a method to return the radius of the ball
        :return: Radius of ball
        """
        return self.radius

    # Method to set radius of ball
    def setRadius(self, r):
        """
        Defining a method to set the radius of the ball
        :return: Nothing
        """
        self.radius = r
        self.refresh()



# Defining a Block class with inheritance from the Thing Class

class Block(Thing):
    def __init__(self, win, x0=0, y0=0, width=4, height=3, color=None):
        Thing.__init__(self, win, "block")
        self.dx = width
        self.dy = height
        self.x0 = x0
        self.y0 = y0
        self.win = win
        self.reshape()
        self.setColor(color)

    def reshape(self):

        """
            Defining a method to set the vis list
        """

        # assign to a local variable(e.g. drawn)the value of self.drawn
        drawn = self.drawn



        if drawn == True:
            self.undraw()

    
        self.vis = [gr.Rectangle(gr.Point((self.x0 - self.dx / 2) * self.scale,
                                          self.win.getHeight() - (self.y0 - self.dy/2) * self.scale),
                                 gr.Point((self.x0 + self.dx / 2) * self.scale,
                                          self.win.getHeight() - (self.y0 + self.dy/2) * self.scale))]

    

        if drawn == True:
            self.draw()

    # Method to return width of block
    def getWidth(self):
        """
        Defining a method to return the width of the block
        :return: Width of block
        """
        return self.dx

    # Method to return height of block
    def getHeight(self):
        """
        Defining a method to return the height of the block
        :return: height of block
        """
        return self.dy


    # Method to set width of block
    def setWidth(self, w):
        """
        Defining a method to set the width of the block
        :return: Nothing
        """
        self.dx = w
        self.reshape()

    # Method to set height of block
    def setHeight(self, h):
        """
        Defining a method to set the height of the block
        :return: Nothing
        """
        self.dy = h
        self.reshape()


# Defining a Triangle class with inheritance from the Thing Class

class Triangle(Thing):
    def __init__(self, win, x0=0, y0=0, side=5, color=None):
        Thing.__init__(self, win, "triangle")
        self.side = side
        self.x0 = x0
        self.y0 = y0
        self.win = win
        self.reshape()
        self.setColor(color)

    def reshape(self):
        """
            Defining a method to set the vis list
            :param win:
            :return:
        """

        # assign to a local variable(e.g. drawn)the value of self.drawn
        drawn = self.drawn

        # if drawn:
        #     undraw the object (use self.undraw())

        if drawn == True:
            self.undraw()

        # define the self.vis list of graphics objects using the current position, radius, and window
        # Visualizing the block onto the window
        self.vis = [gr.Polygon(
            gr.Point(self.x0 * self.scale,
                     self.win.getHeight() - (self.y0 + self.side * 0.866 - self.y0) * self.scale),
            gr.Point((self.x0 - 1/2 * self.side) * self.scale,
                     self.win.getHeight() - (self.y0 - 1/2 * self.side / 0.866 * 1/2) * self.scale),
            gr.Point((self.x0 + 1/2 * self.side) * self.scale,
                     self.win.getHeight() - (self.y0 - 1/2 * self.side / 0.866 * 1/2) * self.scale),
        )
        ]

     # if drawn:
        #    draw the object

        if drawn == True:
            self.draw()


    # Method to return side of Triangle

    def getSide(self):
        """
        Defining a method to return the side of the equilateral Triangle
        :return: side of the triangle
        """
        return self.side

    # Method to return side of Triangle

    def setSide(self, s):
        """
        Defining a method to set the side of the equilateral Triangle
        :return: Nothing
        """
        self.side = s
        self.reshape()



class Oval(Thing):
    def __init__(self, win, x0=0 , y0=0, d=3, radius=2, color=None):
        Thing.__init__(self, win, "oval")
        self.win = win
        self.x0 = x0
        self.y0 = y0
        self.distance = d
        self.radius = radius
        self.reshape()
        self.setColor(color)

    def reshape(self):
        # assign to a local variable(e.g. drawn)the value of self.drawn
        drawn = self.drawn

        if drawn:
            # undraw the object
            self.undraw()

        # define the self.vis list of graphics objects using the current position, radius, and window
        self.vis = [gr.Oval(
            gr.Point((self.x0 - self.distance) * self.scale,
                     self.win.getHeight() - (self.y0 + self.radius) * self.scale),
            gr.Point((self.x0 + self.distance) * self.scale,
                     self.win.getHeight() - (self.y0 - self.radius) * self.scale))
                    ]

    def getRadius(self):
        """ a method that returns the radius of the object"""
        return self.radius

    def setRadius(self, r):
        """a method that sets the radius to r and call the reshape function"""
        self.radius = r
        self.reshape()

    def getDistance(self):
        """a method that returns the distance of the oval's center and the points"""
        return self.distance

    def setDistance(self, d):
        """a method that sets the distance of the oval's center and the points"""
        self.distance = d
        self.reshape()









