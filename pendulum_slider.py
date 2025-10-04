"""
Lagragian Mechanics, for a sliding single pendulum
"""
import pygame as pg
from math import *

pg.init()
w=2000
h=1200
win=pg.display.set_mode((w,h))

fps=120

t=-pi/1.001
tv=0
ta=0

sx,origin_y=(w/2,h/2)
sv=0
sa=0

x=0
y=0

l=250
m=25
M=25
nx=sx
dt=0.01
g=9.8
uk=M
vx=0
clock=pg.time.Clock()
run=True
while run:
    mp=pg.mouse.get_pressed()
    mx,my=pg.mouse.get_pos()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run=False
    if nx!=mx:
        vx=mx-nx
        nx=mx
    win.fill((0,0,0))
    
    a=m*l*l
    b=m*l*cos(t)
    sa=(b*m*l*sin(t)*tv-b*m*g*sin(t)*l-a*m*l*sin(t)*tv+a*sv*uk)/(b*m*l*cos(t)-a*(M+m))
    ta=(m*l*sin(t)*tv-m*g*sin(t)*l-m*l*cos(t)*sa-b*uk*tv)/(m*l*l)
    
    if mp[0]:
        # sv+=vx*dt
        sa=(mx-sx)*dt
        ta=(m*l*sin(t)*tv-m*g*sin(t)*l-m*l*cos(t)*sa-b*uk*tv)/(m*l*l)
        
    tv+=ta*dt
    tv*=0.999
    t+=tv
    
    sv+=sa*dt
    sv*=0.999
    sx+=sv
    
    x=sx+sin(t)*l
    y=origin_y+cos(t)*l
    

    pg.draw.line(win,(55,55,55),(0,origin_y),(w,origin_y),M*2)
    if x>w-m:
        pg.draw.circle(win,(155,155,155),(sx-w-M,origin_y),M)
        pg.draw.circle(win,(255,255,255),(x-w-m,y),m)
        pg.draw.line(win,(255,255,255),(sx-w-M,origin_y),(x-w-m,y))
    elif x<m:
        pg.draw.circle(win,(155,155,155),(sx+w+M,origin_y),M)
        pg.draw.circle(win,(255,255,255),(x+w+m,y),m)
        pg.draw.line(win,(255,255,255),(sx+w+M,origin_y),(x+w+m,y))
    
    if sx<-M:
        sx=w+M
    elif sx >w+M:
        sx=-M
    else:
        pg.draw.line(win,(255,255,255),(sx,origin_y),(x,y))
        pg.draw.circle(win,(155,155,155),(sx,origin_y),M)
        pg.draw.circle(win,(255,255,255),(x,y),m)

    pg.display.update()
    clock.tick(fps)
pg.quit()
