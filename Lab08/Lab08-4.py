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

        for p in self.particle :
            #p.draw()
            p.cdraw([1.0,0.0,0.0,1.0])


        super(myGame,self).afterFrame()

game = myGame(500,500, b"Lab08-4 : Gravity")
game.grid(True)


def key(k, x,y) :
    if k is b' ':
        if game.timer.timerRunning:
            game.timerStop()
        else:
            game.timerStart()
    if k is b'r':
        game.initObjects()


def draw():
    game.frame()

game.start(draw, key)
