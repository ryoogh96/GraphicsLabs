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
        for i in range(10) :
            self.particle.append(Particle.Particle())


        self.initObjects()


    def initObjects(self):
        for i in range(10) :
            self.particle[i].set(np.array([myRand(-10,10),5.0,myRand(-10,10)]))
            self.particle[i].setRadius(0.2)
            self.particle[i].setGravity(np.array([0., -9.8, 0.]))

        return



    def frame(self):
        dt = self.getDt()


        super(myGame,self).frame()



        for p in self.particle :
            p.simulate(dt)

        # 공의 y좌표가 1보다 작거나 같아지면 y좌표를 1으로 설정하고 중력을 0으로 설정한다.
        for p in self.particle :
            if p.loc[1] <= 1 :
                p.loc[1] = 1
                p.setGravity(0)
         

        for p in self.particle :
            p.cdraw([1.0,0.0,0.0,1.0])




        super(myGame,self).afterFrame()

game = myGame(500,500, b"Lab08-p1")
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
