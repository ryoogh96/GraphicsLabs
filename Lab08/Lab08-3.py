from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np
import CGGame


class myGame(CGGame.Game):
    def __init__(self, w, h, title):
        super(myGame,self).__init__(w, h, title)

        self.loc = []
        self.initObjects()

        #self.setBackground(b"background.jpg")

    def initObjects(self):
        self.loc = [0,0,0]

    def frame(self):

        dt = self.getDt()

        super(myGame,self).frame()
        # your code here

        self.loc[0] += 0.1
        self.drawBall(self.loc)

        super(myGame,self).afterFrame()


game = myGame(500, 500, b"Lab08-3:Simple Environment")
game.grid(True)


def key(k, x, y):
    if k is b' ':
        if game.timer.timerRunning:
            game.timerStop()
        else:
            game.timerStart()
    elif k is b'r':
        game.timerReset()
        game.initObjects()


def draw():
    game.frame()


game.start(draw, key)
