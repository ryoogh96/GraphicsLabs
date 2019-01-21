# -*- coding: cp949 -*-
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np
import math

import Particle
import CGGame


def myRand(start, end) :
    interval = end - start
    return start + interval * random.random()

class myGame(CGGame.Game) :

    def __init__(self, w, h, title):
        super(myGame,self).__init__(w,h,title)

        self.particle = []
        for i in range(100) :
            self.particle.append(Particle.Particle())



        self.initObjects()


    def initObjects(self):
        root2 = math.sqrt(2.0)
        for i in range(100) :
            l = np.array([myRand(-6, 6), 5.0, myRand(-6, 6)]) # 공을 공중에 띄어놓기 위해 y좌표를 5.0으로 설정
            self.particle[i].set(l,-l*0.1)
            
            self.particle[i].setColPlane([0,1,0],1) # 충돌 면 설정
            self.particle[i].setRadius(0.2)
            self.particle[i].setGravity(np.array([0., -9.8, 0.]))

        return



    def frame(self):
        dt = self.getDt()


        super(myGame,self).frame()

        for p in self.particle :
            p.simulate(dt)
            p.colHandle()

        for i in range(100) :
            for j in range(i+1, 100) :
                self.particle[i].colHandle()
                self.particle[i].colHandlePair(self.particle[j])

        for p in self.particle :
            p.cdraw([0.0,0.0,1.0,1.0])


        super(myGame,self).afterFrame()

game = myGame(500,500, b"Lab08_p3")
game.grid(True)


def key(k, x,y) :
    if k is b's':
        if game.timer.timerRunning:
            game.timerStop()
        else:
            game.timerStart()
    if k is b'r':
        game.initObjects()


def draw():
    game.frame()

game.start(draw, key)
