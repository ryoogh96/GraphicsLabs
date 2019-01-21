from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np


# Light Properties
Ld = [1,1,1,1]
Ls = [1,1,1,1]
Lp = [10,10,3,1]
# Material Properties
Md = [1,0,0,1]
Ms = [1,1,1,1]
shininess = [120]
t = 0

lookatX = 3
lookatY = 3
lookatZ = 3

# initialization
def GLinit() :
        glClearColor(0,0,0,0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, Ld)
        glLightfv(GL_LIGHT0, GL_SPECULAR, Ls)
        glLightf (GL_LIGHT0, GL_SPOT_CUTOFF, 30.0) # 조명각 설정 각도 변경
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0,0,-1]) # 방향 설정
        glLightf (GL_LIGHT0, GL_SPOT_EXPONENT, 3.0) # 승수 설정
        glMaterialfv(GL_FRONT, GL_DIFFUSE, Md)
        glMaterialfv(GL_FRONT, GL_SPECULAR, Ms)
        glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

        
# display callback
def display() :
        global t,lookatX,lookatY,lookatZ
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # CAMERA SETTING
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, 1.0, 0.1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(lookatX,lookatY,lookatZ, 0,0,0, 0,1,0)
        t += 0.01
        #Lp[0] = 3.0*math.sin(t)
        #Lp[1] = 3.0*math.cos(t)
        glLightfv(GL_LIGHT0, GL_POSITION,Lp)
        sqrt2 = math.sqrt(2.0)
        glBegin(GL_TRIANGLES)

        
        # triangle 1
        glColor3fv([1,0,0])
        p1 = np.array([ 1, 1, 1])
        p2 = np.array([ 0, 1, 0])
        p3 = np.array([ 0, 1, 1])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u,v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)


        # triangle 2
        glColor3fv([1,0,0])
        p1 = np.array([ 1, 1, 1])
        p2 = np.array([ 1, 1, 0])
        p3 = np.array([ 0, 1, 0])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        # triangle 3
        glColor3fv([1,0,0])
        p1 = np.array([ 1, 0, 1])
        p2 = np.array([ 0, 0, 0])
        p3 = np.array([ 0, 0, 1])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        # triangle 4
        glColor3fv([1,0,0])
        p1 = np.array([ 1, 0, 1])
        p2 = np.array([ 1, 0, 0])
        p3 = np.array([ 0, 0, 0])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        # triangle 5
        glColor3fv([1,1,0])
        p1 = np.array([ 1, 0, 1])
        p2 = np.array([ 1, 1, 1])
        p3 = np.array([ 0, 0, 1])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        # triangle 6
        glColor3fv([1,1,0])
        p1 = np.array([ 0, 0, 1])
        p2 = np.array([ 1, 1, 1])
        p3 = np.array([ 0, 1, 1])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)


        # triangle 7
        glColor3fv([1,1,1])
        p1 = np.array([ 0, 0, 0])
        p2 = np.array([ 0, 1, 0])
        p3 = np.array([ 1, 0, 0])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        # triangle 8
        glColor3fv([1,1,0])
        p1 = np.array([ 1, 0, 0])
        p2 = np.array([ 1, 1, 0])
        p3 = np.array([ 0, 1, 0])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)
        

        # triangle 9
        glColor3fv([1,1,1])
        p1 = np.array([ 1, 0, 0])
        p2 = np.array([ 1, 1, 0])
        p3 = np.array([ 1, 0, 1])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        # triangle 10
        glColor3fv([1,1,1])
        p1 = np.array([ 1, 0, 1])
        p2 = np.array([ 1, 1, 1])
        p3 = np.array([ 1, 1, 0])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        # triangle 11
        glColor3fv([1,1,1])
        p1 = np.array([ 0, 0, 1])
        p2 = np.array([ 0, 1, 1])
        p3 = np.array([ 0, 0, 0])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        # triangle 12
        glColor3fv([1,1,1])
        p1 = np.array([ 0, 0, 0])
        p2 = np.array([ 0, 1, 0])
        p3 = np.array([ 0, 1, 1])
        u = p2 - p1 # vector from p1 to p2
        v = p3 - p1 # vector from p1 to p3
        normal = np.cross(u, v)
        normal = normal / (np.linalg.norm(normal))
        glNormal3fv(normal)
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)

        glEnd()
        glFlush()
     
# key_up zoom in/ key_down zoom out
def move(key, x, y):

    global lookatX,lookatY,lookatZ
    
    if key == GLUT_KEY_UP:
        lookatY -= 1.0
    elif key == GLUT_KEY_DOWN:
        lookatY += 1.0
    elif key == GLUT_KEY_LEFT:
        lookatX -= math.cos(10)
    elif key == GLUT_KEY_RIGHT:
        lookatX += math.cos(10)
        


def main():
        # windowing
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH |GLUT_RGBA)
        glutInitWindowSize(600,600)
        glutInitWindowPosition(10,10)
        glutCreateWindow(b"Normal & Light on Triangles")
        GLinit()
        # register callbacks
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutSpecialFunc(move)
        # enter main-loop
        glutMainLoop()

if __name__ == "__main__":
    main()
    
