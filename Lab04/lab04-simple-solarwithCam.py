from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_POSITION_X = 0
WINDOW_POSITION_Y = 0




class Camera :

    def __init__(self):  #constructor
        self.loc = np.array([0.0, 0.0,  0.0])
        self.tar = np.array([0.0, 0.0, 0.0])
        self.up  = np.array([0.0, 1.0,  0.0])
        self.right = np.array([1.0, 0.0, 0.0])
        self.dir = np.array([0.0, 0.0, -1.0])
        self.asp = 1.0	# aspect
        self.fov = 60
        self.near= 0.1
        self.far = 100.0

    def setCameraLoc(self, loc):
        self.loc = loc
        self.tar = self.loc + self.dir

    def setCamera(self, loc, tar, up):
        self.loc, self.tar, self.up = loc, tar, up

        self.dir = self.tar - self.loc
        l = np.linalg.norm(self.dir)
        if l > 0.0 :
            self.dir = self.dir / l

        l = np.linalg.norm(self.up)
        if l > 0.0 :
            self.up = self.up / l

        self.right = np.cross(self.dir, self.up)


    def setLens(self, fov, asp, near, far):
        self.fov, self.asp, self.near, self.far = fov, asp, near, far

    def applyCamera(self):
        gluLookAt(self.loc[0], self.loc[1], self.loc[2],
                  self.tar[0], self.tar[1], self.tar[2],
                  self.up [0], self.up [1], self.up [2])

    def applyLens(self):
        gluPerspective(self.fov, self.asp, self.near, self.far)

    def moveForward(self, step=1.0):
        self.tar += self.dir*step
        self.loc += self.dir*step

angle = 0.0

def drawPlanet(distance, angle, planetRadius, spin=0.0, slope=0.0 ) :

    glRotatef(slope, 1, 0, 0)
    glBegin(GL_LINE_STRIP)
    for i in range(0, 360):
        theta = 2.0 * 3.141592 * i / 360.0
        x = distance * math.cos(theta)
        y = distance * math.sin(theta)
        glVertex3f(x, 0, y)
    glEnd()
    
    glRotatef(angle, 0, 1, 0)
    glTranslatef(distance, 0, 0)
    glPushMatrix()
    glRotatef(spin, 0, 1, 0)
    glutWireSphere(planetRadius, 10, 10)
    glPopMatrix()
 
def drawScene() :
    global angle

    # drawing
    # sun
    glColor3f(1,0,0)
    glutSolidSphere(1.0, 20, 20)

    angle += 0.1
    
    # earth
    glPushMatrix()
    glColor3f(0,0.5,1.0)
    drawPlanet(10.0, angle, 0.5, angle*33.33, -5 )

    # moon
    glColor(1.0, 1.0, 0.0)
    drawPlanet(2.0, 14.231*angle, 0.2, 0.0, slope=10)
    glPopMatrix()
    
def disp() :

    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, 1.0, 0.1, 100)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glViewport(WINDOW_POSITION_X,WINDOW_POSITION_Y,WINDOW_WIDTH,WINDOW_HEIGHT)
    #gluLookAt(10,20,60, 0,0,-1, 0,1,0)
    gluLookAt(0,50,0, 0,0,0, 0,0,1)
    #gluLookAt(0,10,50, 0,0,0, 0,1,0)
    drawScene()
    
    glFlush()

def main():
    # windowing
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH,WINDOW_HEIGHT)
    glutInitWindowPosition(WINDOW_POSITION_X,WINDOW_POSITION_Y)
    glutCreateWindow(b"Simple Solar")

    glClearColor(0, 0.0, 0.0, 0)

    # register callbacks
    glutDisplayFunc(disp)
    glutIdleFunc(disp)

    # enter main infinite-loop
    glutMainLoop()

if __name__=="__main__":
    main()


