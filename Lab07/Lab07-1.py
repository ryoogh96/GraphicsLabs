from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np
from PIL import Image

xRot = 0.0
yRot = 0.0
zRot = 0.0

def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data


def setTexture(Image) :
    imgW, imgH, myImage = loadImage(Image)
    #print(imgW, imgH, myImage)
    
    # texture image 생성
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 imgW, imgH, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, myImage)
    # texture 매핑 옵션 설정
    glTexParameterf(GL_TEXTURE_2D,
    GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D,
    GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D,
    GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D,
    GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    # 2d texture 매핑을 활성화
    glEnable(GL_TEXTURE_2D)


    
def myReshape(w, h) :
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspRatio = w / h
    gluPerspective(60, aspRatio, 0.1, 10)
    glViewport(0, 0, w, h)


def myDisplay():
    global xRot,yRot,zRot
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,3, 0,0,0, 0,1,0)

	# Keyboard Input Rotation
    glRotate(xRot,1.0,0.0,0.0)
    glRotate(yRot,0.0,1.0,0.0)
    glRotate(zRot,0.0,0.0,1.0)

    # 안쪽 뒷면
    setTexture("baboon.jpg")
    glBegin(GL_QUADS)
    glNormal3f(0.0, 0.0, 1.0);
    glTexCoord2f(0,0)
    glVertex3fv([-1, 1, 0])
    glTexCoord2f(0,1)
    glVertex3fv([-1,-1, 0])
    glTexCoord2f(1,1)
    glVertex3fv([ 1,-1, 0])
    glTexCoord2f(1,0)
    glVertex3fv([ 1, 1, 0])
    glEnd()
    
	# 바깥쪽 앞면
    setTexture("cat.jpg")
    glBegin(GL_QUADS)
    glNormal3f(0.0, 0.0, 1.0);
    glTexCoord2f(0,0)
    glVertex3fv([-1, 1, 1])
    glTexCoord2f(0,1)
    glVertex3fv([-1, -1, 1])
    glTexCoord2f(1,1)
    glVertex3fv([ 1, -1, 1])
    glTexCoord2f(1,0)
    glVertex3fv([ 1, 1, 1])
    glEnd()
    
	# 윗쪽 면
    setTexture("pnu01.jpg")
    glBegin(GL_QUADS)
    glNormal3f(0.0, 1.0, 0.0);
    glTexCoord2f(0,0)
    glVertex3fv([-1, 1, 1])
    glTexCoord2f(0,1)
    glVertex3fv([-1, 1, 0])
    glTexCoord2f(1,1)
    glVertex3fv([ 1, 1, 0])
    glTexCoord2f(1,0)
    glVertex3fv([ 1, 1, 1])
    glEnd()
    
	# 밑쪽 면
    setTexture("pnu02.jpg")
    glBegin(GL_QUADS)
    glNormal3f(0.0, 1.0, 0.0);
    glTexCoord2f(0,0)
    glVertex3fv([-1,-1, 1])
    glTexCoord2f(0,1)
    glVertex3fv([-1,-1, 0])
    glTexCoord2f(1,1)
    glVertex3fv([ 1,-1, 0])
    glTexCoord2f(1,0)
    glVertex3fv([ 1, -1, 1])
    glEnd()
    
	# 왼쪽 면
    setTexture("pnu03.jpg")
    glBegin(GL_QUADS)
    glNormal3f(1.0, 0.0, 0.0);
    glTexCoord2f(0,0)
    glVertex3fv([-1, 1, 0])
    glTexCoord2f(0,1)
    glVertex3fv([-1,-1, 0])
    glTexCoord2f(1,1)
    glVertex3fv([-1, -1, 1])
    glTexCoord2f(1,0)
    glVertex3fv([-1, 1, 1])
    glEnd()
    
	# 오른쪽 면
    setTexture("pnu04.jpg")
    glBegin(GL_QUADS)
    glNormal3f(1.0, 0.0, 0.0);
    glTexCoord2f(0,0)
    glVertex3fv([ 1, 1, 0])
    glTexCoord2f(0,1)
    glVertex3fv([ 1,-1, 0])
    glTexCoord2f(1,1)
    glVertex3fv([ 1, -1, 1])
    glTexCoord2f(1,0)
    glVertex3fv([ 1, 1, 1])
    glEnd()
    
    glFlush()
    return


def GLInit() :
    # clear color setting
    glClearColor(0, 0, 1, 1)
    glEnable(GL_DEPTH_TEST)
    
# key_up zoom in/ key_down zoom out
def move(key, x, y):

    global xRot,yRot,zRot
    
    if key == GLUT_KEY_UP:
        xRot += 5.0
        zRot += 5.0
        glutPostRedisplay()
        #lookatY -= 1.0
    elif key == GLUT_KEY_DOWN:
        xRot -= 5.0
        zRot -= 5.0
        glutPostRedisplay()
        #lookatY += 1.0
    elif key == GLUT_KEY_LEFT:
        yRot += 5.0
        glutPostRedisplay()
        #lookatX -= math.cos(10)
    elif key == GLUT_KEY_RIGHT:
        yRot -= 5.0
        glutPostRedisplay()
        #lookatX += math.cos(10)
    
def main(arg) :
    # opengl glut initialization
    glutInit(arg)
    # window setting
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Texture")
    GLInit()
    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    glutIdleFunc(myDisplay)
    glutSpecialFunc(move)
    glutMainLoop()

if __name__ == "__main__" :
    main(sys.argv)


