from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_POSITION_X = 0
WINDOW_POSITION_Y = 0

revolveday = 365.24219
rotate = 0.0

def drawPlanet(distance, rotate, planetRadius) :

    glBegin(GL_LINE_STRIP)
    for i in range(0, 361):
        theta = 2.0 * 3.141592 * i / 360.0
        x = distance * math.cos(theta)
        y = distance * math.sin(theta)
        glVertex3f(x, 0, y)
    glEnd()

    glRotatef(rotate, 0, 1, 0)
    glTranslatef(distance, 0, 0)

    glutWireSphere(planetRadius, 20, 20)
 
def drawScene() :
    global rotate
	
    # drawing
    # earth
    glPushMatrix()
    glColor3f(0,0.5,1.0)
    rotate += (revolveday / 30.4368491) / 1000    # 지구의 공전일수 30일 : 365.24219 / 12 = 30.4368491
    drawPlanet(10.0, rotate, 0.5)        # 눈으로 확인할 수 있는 속도로 조정하기위해 / 100을 해준다.
    glPopMatrix()
    glPushMatrix()
    # moon
    glColor3f(0.5,0.5,0.0)
    drawPlanet(15.0, rotate*30, 0.8) # 달의 공전일수 1일 : 365.24219 with 속도조정 / 100 = 0.36524219
    glPopMatrix()                    # 위의 속도도정된 1일 공전일수는 지구의 속도조절된 공전일수 * 30 = 10.9572657 이된다.
    
def disp() :

    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, 1.0, 0.1, 1000)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glViewport(WINDOW_POSITION_X,WINDOW_POSITION_Y,WINDOW_WIDTH,WINDOW_HEIGHT)
    gluLookAt(10,20,60, 0,0,0, 0,1,0)
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


