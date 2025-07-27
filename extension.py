"""
Aum Desai
Fall 2022
CS152B Project 08 Extension

This program is for Project 08. Can use adsw keys to control object movement. 
This file can be run by putting python3 extension.py in the terminal.
"""

import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import time


# Creating obstacles for the simulation
def buildObstacles(win):
    """
    This method create obstacles (blocks)
    :param win: The window being drawn onto
    :return: A list of objects created
    """
    # Create all of the obstacles in the scene and put them in a list
    obs =[]
    # Each obstacle should be a Thing (e.g. Ball, Block,other)
    block1 = pho.Block(win)
    block2 = pho.Block(win)
    block3 = pho.Block(win)

    block1.setPosition(10, 20)
    block2.setPosition(25, 20)
    block3.setPosition(40, 20)

    # block1.setWidth(4)
    # block1.setHeight(3)
    # block2.setWidth(4)
    # block2.setHeight(3)
    # block3.setWidth(4)
    # block3.setHeight(3)


    obs.append(block1)
    obs.append(block2)
    obs.append(block3)
    # You might want to give one or more the obstacles an elasticity > 1
    block1.setElasticity(0.9)
    block2.setElasticity(0.9)
    block3.setElasticity(0.9)


    # Return the list of Things
    return obs

def main():
    """
    method will create and run the simulation
    :return: A window with the simulation running
    """
    # create a GraphWin
    win = gr.GraphWin('Obstacle', 500, 500, False)
    win.setBackground("White")
    # call buildObstacles, storing the return list in a
    shapes = buildObstacles(win)
    # loop over the shapes list and have each Thing call its draw method
    for item in shapes:
        item.draw()
    # assign to dt the value 0.02
    # assign to frame the value 0

    dt = 0.01
    frame = 0

    # create a ball, give it an initial velocity and acceleration, and draw it
    ball1 = pho.Ball(win)
    ball1.setElasticity(0.9)
    ball1.setPosition(35, 25)
    ball1.setVelocity(5, 15)
    ball1.setRadius(1)
    ball1.setAcceleration(0, -10)
    ball1.setColor((420, 420, 420))
    ball1.draw()

    # create an oval, give it an initial velocity and acceleration, and draw it
    oval1 = pho.Oval(win)
    oval1.setPosition(15, 25)
    oval1.setVelocity(5, 15)
    oval1.setAcceleration(0, -10)
    oval1.setElasticity(0.9)
    oval1.setColor((123, 123, 123))
    oval1.draw()

    triangle1 = pho.Triangle(win)
    triangle1.setPosition(15, 25)
    triangle1.setVelocity(5, 15)
    triangle1.setAcceleration(0, -10)
    triangle1.setElasticity(0.9)
    triangle1.setColor((223, 223, 223))
    triangle1.draw()


    # start an infinite loop
    while True:
        # if frame modulo 10 is equal to 0
        if frame % 10 == 0:
            win.update()
            # call win.update()
        # using checKey, if the user typed a 'q' then break
        key = win.checkKey()
        time.sleep(0.001)
        if key == 'q':
            break

        # if the ball is out of bounds, re-launch it
        pos = ball1.getPosition()
        velo_ball = ball1.getVelocity()

        pos1 = oval1.getPosition()
        velo_oval = oval1.getVelocity()

        pos2 = triangle1.getPosition()
        velo_tri = triangle1.getVelocity()

        # if the ball or the oval is at the boundary, have it bounce back
        if pos[0] < 0 or pos[0] > 50:
            col_pos = ball1.getVelocity()
            ball1.setVelocity(col_pos[0] * -1, col_pos[1])

        if pos[1] < 0 or pos[1] > 50:
            col_pos = ball1.getVelocity()
            ball1.setVelocity(col_pos[0], col_pos[1] * -1)

        if pos1[0] - 3 < 0 or pos1[0] + 3 > 50:
            col_pos = oval1.getVelocity()
            oval1.setVelocity(col_pos[0] * -1, col_pos[1])

        if pos1[1] < 0 or pos1[1] > 50:
            col_pos = oval1.getVelocity()
            oval1.setVelocity(col_pos[0], col_pos[1] * -1)

        if pos2[0] - 3 < 0 or pos2[0] + 3 > 50:
            col_pos = triangle1.getVelocity()
            triangle1.setVelocity(col_pos[0] * -1, col_pos[1])

        if pos2[1] < 0 or pos2[1] > 50:
            col_pos = triangle1.getVelocity()
            triangle1.setVelocity(col_pos[0], col_pos[1] * -1)

        # Setting up the control keys for the ball
        if key == "Left":
            ball1.setVelocity(velo_ball[0] - 1, velo_ball[1])

        if key == "Right":
            ball1.setVelocity(velo_ball[0] + 1, velo_ball[1])

        if key == "Up":
            ball1.setVelocity(velo_ball[0], velo_ball[1] + 1)

        if key == "Down":
            ball1.setVelocity(velo_ball[0], velo_ball[1] - 1)

        # Setting up the control keys for the oval
        if key == "a":
            oval1.setVelocity(velo_oval[0] - 1, velo_oval[1])

        if key == "d":
            oval1.setVelocity(velo_oval[0] + 1, velo_oval[1])

        if key == "w":
            oval1.setVelocity(velo_oval[0], velo_oval[1] + 1)

        if key == "s":
            oval1.setVelocity(velo_oval[0], velo_oval[1] - 1)

        if key == "Left":
            triangle1.setVelocity(velo_tri[0] - 1, velo_tri[1])

        if key == "Right":
            triangle1.setVelocity(velo_tri[0] + 1, velo_tri[1])

        if key == "Up":
            triangle1.setVelocity(velo_tri[0], velo_tri[1] + 1)

        if key == "Down":
            triangle1.setVelocity(velo_tri[0], velo_tri[1] - 1)

        # assign to collided the value False
        collided = False
        collided1 = False
        collided2 = False
        # for each item in the shapes list
            # if the result of calling the collision function with the ball and the item is True
                # set collided to True
        for item in shapes:
            if coll.collision(ball1, item, dt) == True:
                collided = True

            if coll.collision(oval1, item, dt) == True:
                collided1 = True

        

        ball_collided = False
        if coll.collision_ball_ball(ball1,oval1, dt) == True:
            ball_collided = True

        # if collided is equal to False
            # call the update method of the ball with dt as the time step
        if collided == False:
            ball1.update(dt)

        if collided1 == False:
            oval1.update(dt)

        if ball_collided == False:
            ball1.update(dt)
            oval1.update(dt)

        # increment frame
        frame += 1


    # close the window

        if win.checkMouse() != None:
            break

    win.close()

    
if __name__ == "__main__":
    main()
