from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

IsRect = False
Color = 0
TopLeftX = 0
TopLeftY = 0
BottomRightX = 0
BottomRightY = 0

def MyDisplay():
    global IsRect, Color
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5,0.0,0.5)
    if Color == 1:
        glClearColor(0.0,1.0,1.0,1.0)
    elif Color == 2:
        glColor3f(0.0,0.0,1.0)
    if IsRect:
        glBegin(GL_POLYGON)
        glVertex3f(TopLeftX/300.0,(300-TopLeftY)/300.0,0.0)
        glVertex3f(TopLeftX/300.0,(300-BottomRightY)/300.0,0.0)
        glVertex3f(BottomRightX/300.0,(300-BottomRightY)/300.0,0.0)
        glVertex3f(BottomRightX/300.0,(300-TopLeftY)/300.0,0.0)
        glEnd()
    glFlush()


def MyMouseClick(Button,State,X,Y):
    global TopLeftX,TopLeftY
    if Button == GLUT_LEFT_BUTTON and State == GLUT_DOWN:
        TopLeftX = X
        TopLeftY = Y
        
def MyMouseMove(X,Y):
    global BottomRightX,BottomRightY
    BottomRightX = X
    BottomRightY = Y
    glutPostRedisplay()


def MyRectMenu(entryID):    
    global IsRect
    if entryID == 1:
        IsRect = True
    glutPostRedisplay()
    return 0

def MyColorMenu(entryID):
    global Color
    if entryID == 1:
        Color = 1
    elif entryID == 2:
        Color = 2
    elif entryID == 3:
        exit(0)
    glutPostRedisplay()
    return 0
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(300,300)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b"OpenGL Example Drawing")
    glClearColor(1.0,1.0,1.0,1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,1.0,0.0,1.0,-1.0,1.0)
    MyColorMenuID = glutCreateMenu(MyColorMenu)
    glutAddMenuEntry('Change Background Color',1)
    glutAddMenuEntry('Change Rectangle Color', 2)
    MyMainMenuID = glutCreateMenu(MyRectMenu)
    glutAddMenuEntry('Draw Rectangle',1)
    glutAddSubMenu('Change Color',MyColorMenuID)
    glutAddMenuEntry('Exit',3)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutDisplayFunc(MyDisplay)
    glutMouseFunc(MyMouseClick)
    glutMotionFunc(MyMouseMove)
    glutMainLoop()

if __name__ == '__main__':
    main()
