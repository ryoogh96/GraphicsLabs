from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

IsRect = False
IsSphere = False
IsTorus = False
Color = 0
TopLeftX = 0
TopLeftY = 0
BottomRightX = 0
BottomRightY = 0
SphereRadius = 0.5
TorusRadius = 0.1

def MyDisplay():
    global IsRect, Color, SphereRadius, TorusRadius
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0,0,300,300)
    glColor3f(0.5,0.0,0.5)
    if Color == 1:
        glClearColor(0.0,1.0,1.0,1.0)
        glutPostRedisplay()
    elif Color == 2:
        glColor3f(0.0,0.0,1.0)
    if IsRect == True:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0,1.0,0.0,1.0,-1.0,1.0)
        glBegin(GL_POLYGON)
        glVertex3f(TopLeftX/300.0,(300-TopLeftY)/300.0,0.0)
        glVertex3f(TopLeftX/300.0,(300-BottomRightY)/300.0,0.0)
        glVertex3f(BottomRightX/300.0,(300-BottomRightY)/300.0,0.0)
        glVertex3f(BottomRightX/300.0,(300-TopLeftY)/300.0,0.0)
        glEnd()
    elif IsSphere == True:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0)
        glutSolidSphere(SphereRadius,30,30)
    elif IsTorus == True:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0)
        glutSolidTorus(TorusRadius,0.3,40,20)   
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
    global IsRect, IsSphere, IsTorus
    if entryID == 1:
        IsRect = True
        IsSphere = False
        IsTorus = False
    elif entryID == 2:
        IsSphere = True
        IsRect = False
        IsTorus = False
    elif entryID == 3:
        IsTorus = True
        IsSphere = False
        IsRect = False
    glutPostRedisplay()
    return 0

def MyColorMenu(entryID):
    global Color
    if entryID == 1:
        Color = 1
    elif entryID == 2:
        Color = 2
    glutPostRedisplay()
    return 0

def MySphereRadiusMenu(entryID):
    global SphereRadius
    if entryID == 3:
        SphereRadius = 0.3
    elif entryID == 7:
        SphereRadius = 0.7
    elif entryID == 10:
        SphereRadius = 1.0
    glutPostRedisplay()
    return 0
def MyTorusRadiusMenu(entryID):
    global TorusRadius
    if entryID == 5:
        TorusRadius = 0.05
    elif entryID == 25:
        TorusRadius = 0.025
    elif entryID == 1:
        TorusRadius = 0.01
    glutPostRedisplay()
    return 0
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(300,300)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b"OpenGL Example Drawing")
    glClearColor(1.0,1.0,1.0,1.0)
    MyColorMenuID = glutCreateMenu(MyColorMenu)
    glutAddMenuEntry('Change Background Color',1)
    glutAddMenuEntry('Change Rectangle Color', 2)
    MySphereRadiusMenuID = glutCreateMenu(MySphereRadiusMenu)
    glutAddMenuEntry('0.3',3)
    glutAddMenuEntry('0.7',7)
    glutAddMenuEntry('1.0',10)
    MyTorusRadiusMenuID = glutCreateMenu(MyTorusRadiusMenu)
    glutAddMenuEntry('0.05',5)
    glutAddMenuEntry('0.025',25)
    glutAddMenuEntry('0.01',1)
    MyMainMenuID = glutCreateMenu(MyRectMenu)
    glutAddMenuEntry('Draw Rectangle',1)
    glutAddMenuEntry('Draw Solid Sphere',2)
    glutAddMenuEntry('Draw Soild Torus',3)
    glutAddSubMenu('Change Color',MyColorMenuID)
    glutAddSubMenu('Change Sphere Radius',MySphereRadiusMenuID)
    glutAddSubMenu('Change Torus Radius',MyTorusRadiusMenuID)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutDisplayFunc(MyDisplay)
    glutMouseFunc(MyMouseClick)
    glutMotionFunc(MyMouseMove)
    glutMainLoop()

if __name__ == '__main__':
    main()
