"""
(Saturday Oct 4 2025)
I am a grade 12 student, diving deep into lagragian mechanics, I had to teach myself calculus (mainly derivative rules), and how lagragian mechanics work.
This is my attempt to calculate double pendulum's motion, without ANY Tutorials, just pure calculations, and i think i got close to an actual functioning pendulum

I used lagragian's equation to derive the physics of the double pendulum's motion
The core equation being L = T - V

(the result of when i finally got the pendulum's motion is not perfect, there are still some artificial dampening that I had to do to make the double pendulum stable, because it can act out of probably due to minor calculation errors. It is really easy to mess up, because of the long tedious calculations required.)

if you draw a diagram of the double pendulum, the height of the pendulum 1 will be Length1*cos(theta1) and x be Lenght1*sin(theta1).
Because the y side is adjacent to theta and x side is opposite to theta

For the attatched pendulum, the position will be summed with the first pendulum's position
x2=L1*sin(theta1) + L2*sin(theta2)
y2=L1*cos(theta1) + L2*cos(theta2)

getting the position derivatives get angular velocity, because theta with respect to time is a function, so angular velocity is just a dervitation of the theta(time) function in a nutshell

chain rule:
f(g(t))=f'(g(t))*g'(t)
in this cause for the x position sin(theta(time)) = cos(theta(time))*theta'(time)
theta'(time) = angular velocity
x1'=L1*cos(theta1)*theta1_v (theta1_v being angular velocity)
y1'=-L1*sin(theta1)*theta1_v

you do the same calculations for theta 2

then plug in the angular velocities into kinetic energy
T=1/2*m1*v1^2 + 1/2*m2*v2^2
and the position of the y values to potential energy
V=m1gh1 + m2gh2 (h being the y position of the pendulum)

then get the partial derivates of theta for potential energy
and partial derviates of angular velocity
so lets represent T' as kinetic energy's partial derivative for angular velocity and V' as potential energy's partial derivative for theta
then,
V' remains partial, however you get the time derivative for T'
T'' is the time derivative (this is important to get angular acceleration)
V' is the partial for potential

Energy can not be created nor destroyed, so
T'' - V' = 0
the 0 in the equation represents that energy is conserved
use this equation to rearrange for angular acceleration for theta1 and theta2
then substitute and solve an angle's acceleration, because you will have two Lagragian equations representing both pendulums.
"""
import pygame as pg
from math import *

pg.init()
w=1400
h=1200
win=pg.display.set_mode((w,h))

fps=120

t1=pi/2
tv1=0
ta1=0
l1=250
m1=25

t2=pi/2
tv2=0
ta2=0
l2=125
m2=25

origin_x,origin_y=(w/2,h/2)

ps=[]

dt=0.34
g=9.8
clock=pg.time.Clock()
run=True
while run:
    mp=pg.mouse.get_pressed()
    mx,my=pg.mouse.get_pos()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run=False
    win.fill((0,0,0))

    a=(m1+m2)*l1*l1
    b=-m2*l1*l2*cos(t1-t2)
    ta2=(b*m2*l1*l2*sin(t1-t2)*tv2*(tv1-tv2)-b*(m1+m2)*g*l1*sin(t1)-a*m2*l1*l2*tv1*sin(t1-t2)*(tv1-tv2)-a*m2*g*l2*sin(t2))/(a*m2*l2*l2+b*m2*l1*l2*cos(t1-t2))
    ta1=(m2*l1*l2*sin(t1-t2)*tv2*(tv1-tv2)-m2*l1*l2*ta2*cos(t1-t2)-(m1+m2)*g*l1*sin(t1))/(a)

        
    tv1+=ta1*dt*dt
    tv1*=0.999625
    t1+=tv1*dt
    if mp[0]:
        ta1=0
        tv1=0
        t1=atan2(mx-origin_x,my-origin_y)


    tv2+=ta2*dt*dt
    tv2*=0.999625
    t2+=tv2*dt

    x1=origin_x+sin(t1)*l1
    y1=origin_y+cos(t1)*l1
    x2=x1+sin(t2)*l2
    y2=y1+cos(t2)*l2

    ps.append([x2,y2,m2])
    for p in ps:
        pg.draw.circle(win,(25,15,15),(p[0],p[1]),p[2])
        p[2]-=0.1
        if p[2]<=0:
            ps.remove(p)

    pg.draw.line(win,(155,155,155),(origin_x,origin_y),(x1,y1),m1)
    pg.draw.circle(win,(100,100,100),(origin_x+sin(t1)*abs(tv1)*m1,origin_y+cos(t1)*abs(tv1)*m1),m1)
    pg.draw.line(win,(155,155,155),(x1,y1),(x2,y2),m2)
    pg.draw.circle(win,(255,255,255),(x1+sin(t2)*abs(tv2)*m1,y1+cos(t2)*abs(tv2)*m1),m1)
    pg.draw.circle(win,(255,255,255),(x2,y2),m2)


    pg.display.update()
    clock.tick(fps)
pg.quit()
