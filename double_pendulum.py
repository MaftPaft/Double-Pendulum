import pygame as pg
from pyextensions.mygame import white,black,CircleClass
from math import *


#Python Double Pendulum

#initalize
pg.init()
#width,height
width,height=800,900
#window
win=pg.display.set_mode((width,height))
#fps rate (frames per second)
fps=60
# Creating the Pendulum Balls named p1 and p2
p1=CircleClass(width/2,height/2,25,white,win,0,0,0,0)
p2=CircleClass(width/2,height/1.25,25,white,win,0,0,0,0)

#Double Penulum Mass
mass1=p1.radius
mass2=p2.radius
#Length apart from both objects
length1=150
length2=150
#angle of both objects
angle1=pi/1.5
angle2=pi/1.5
#angle velocities
av1=0
av2=0
#angle acceleration
aa1=0
aa2=0
#gravity
g=1
#acceleration formula for the object p1
def first_acceleration(t1, t2, m1, m2, L1, L2, G, v1, v2):
    numerator1 = -G * (2 * m1 + m2) * sin(t1)
    numerator2 = -m2 * G * sin(t1 - 2 * t2)
    numerator3 = -2 * sin(t1-t2)
    numerator4 =  m2 * ((v2 * v2) * L2 + (v1 * v1) * L1 * cos(t1-t2))
    numerator = numerator1 + numerator2 + (numerator3 * numerator4)
    denominator = L1 * (2 * m1 + m2 - m2 * cos(2 * t1 - 2 * t2))
    return numerator/denominator
#acceleration formula for object p2
def second_acceleration(t1, t2, m1, m2, L1, L2, G, v1, v2):
    numerator1 = 2 * sin(t1 - t2)
    numerator2 = (v1 * v1) * L1 * (m1 + m2) + G * (m1+ m2) * cos(t1)
    numerator3 = (v2 * v2) * L2 * m2 * cos(t1-t2)

    numerator = numerator1 * (numerator2 + numerator3)
    denominator = L2 * (2 * m1 + m2 - m2 * cos(2 * t1 - 2 * t2))

    return float(numerator/denominator)

#speeding up the simulation when left click press
speed_up=False
speed=fps

#history to go back in time
history1=[]
#running the loop
run=True
clock=pg.time.Clock()
while run:
    mp=pg.mouse.get_pressed()

    if mp[2] and len(history1) > 0:
        #go back in time
        n=len(history1)-1
        pressed=True
        while n >= 0:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    run=False
                    pg.quit()
                if i.type == pg.MOUSEBUTTONDOWN:
                    if i.button == pg.BUTTON_MIDDLE:
                        print('f')
                        pressed=False
            if pressed == True:
                win.fill((255,255,255))
                
                p1.x=history1[n][0]
                p1.y=history1[n][1]
                p2.x=history1[n][2]
                p2.y=history1[n][3]
                angle1=history1[n][4]
                angle2=history1[n][5]
                av1=history1[n][6]
                av2=history1[n][7]
                pg.draw.circle(win,(0,0,0),(p1.x,p1.y),p1.radius)
                pg.draw.circle(win,(0,0,0),(p2.x,p2.y),p2.radius)
                pg.draw.line(win,(0,0,0),(width/2,height/2),(p1.x,p1.y))
                pg.draw.line(win,(0,0,0),(p1.x,p1.y),(p2.x,p2.y))
                pg.display.update()
                clock.tick(fps)
                n-=1
            else:
                break
        history1.clear()
            
    else:
        mx,my=pg.mouse.get_pos()
        mp=pg.mouse.get_pressed()
        for i in pg.event.get():
            if i.type == pg.QUIT:
                run=False
            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == pg.BUTTON_RIGHT:
                    print('f')
            
        win.fill(black)
        #if left mouse pressed speed up the simulation time
        if mp[0]:
            speed_up=True
            speed+=1
        else:
            speed_up=False
            if speed > 120:
                speed-=1

        #applying the formulas to angle acceleration
        aa1 = first_acceleration(angle1,angle2,mass1,mass2,length1,length2,g,av1,av2)
        aa2 = second_acceleration(angle1,angle2,mass1,mass2,length1,length2,g,av1,av2)

        #for the objects to swing as a double pendulum
        #the objects go in a circular motion because of multiplying the length with the sin angle for x and cos angle for y
        p1.x = length1*sin(angle1)+(width/2)
        p1.y = length1*cos(angle1)+(height/2)
        p2.x = p1.x+length2*sin(angle2)
        p2.y = p1.y+length2*cos(angle2)

        #angle velocity changing by angle accelerations
        av1+=aa1
        av2+=aa2
        #angle is chaning by angle velocity
        angle1+=av1
        angle2+=av2
        
        #drawing a line to connect the pendulum
        pg.draw.line(win,white,(width/2,height/2),(p1.x,p1.y))
        pg.draw.line(win,white,(p1.x,p1.y),(p2.x,p2.y))

        #drawing objects
        p1.draw(win)
        p2.draw(win)
        
        # collecting data from the pendulum to go back go back in time
        history1.append((p1.x,p1.y,p2.x,p2.y,angle1,angle2,av1,av2))

        #updating display
        pg.display.update()
        #if you want to speed up the simulation
        if speed_up==False and speed <= fps:
            clock.tick(fps)
        else:
            clock.tick(int(speed))
pg.quit()
