from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math
import numpy as np
from PIL import Image

time = 0

nTex = 5
texArr = None

xRot = 0.0
yRot = 0.0
zRot = 0.0


def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data

def combineImgTexture(texArr):
    list_im = ['pnu01.jpg', 'pnu02.jpg', 'pnu03.jpg', 'pnu04.jpg']
    imgs    = [ Image.open(i) for i in list_im ]
    
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

    # save picture
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save( 'pnu4.jpg' )

    

    glBindTexture(GL_TEXTURE_2D, texArr[0])
    imgW, imgH, myImage = loadImage('pnu4.jpg')
    
    

    # texture image 생성q
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 imgW, imgH, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, myImage)

    # texture 매핑 옵션 설정
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_MIN_FILTER, GL_NEAREST)


def drawQuad(x,y,z, angle) :
    glPushMatrix()
    glTranslatef(x,y,z)
    glRotatef(angle, 0,0,1)
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3fv([-1, 1, 0])
    glTexCoord2f(0,1)
    glVertex3fv([-1,-1, 0])
    glTexCoord2f(1,1)
    glVertex3fv([ 1,-1, 0])
    glTexCoord2f(1,0)
    glVertex3fv([ 1, 1, 0])
    glEnd()
    glPopMatrix()

def myReshape(w, h) :
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspRatio = w / h
    gluPerspective(60, aspRatio, 0.1, 10)
    glViewport(0, 0, w, h)



def myDisplay():
    global time, texArr

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,5, 0,0,0, 0,1,0)

    # Keyboard Input Rotation
    glRotate(xRot,1.0,0.0,0.0)
    glRotate(yRot,0.0,1.0,0.0)
    glRotate(zRot,0.0,0.0,1.0)

    
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    glTexGenf(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGenf(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glPushMatrix()
    glutSolidSphere(0.7,32,32)
    glPopMatrix()

    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)

    glFlush()

    return

def GLInit() :
    global nTex, texArr

    texArr = glGenTextures(nTex)
    # clear color setting
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    combineImgTexture(texArr)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_TEXTURE_2D)

# key_up zoom in/ key_down zoom out
def move(key, x, y):

    global xRot,yRot,zRot
    
    if key == GLUT_KEY_UP:
        xRot += 5.0
        zRot += 5.0
        glutPostRedisplay()
    elif key == GLUT_KEY_DOWN:
        xRot -= 5.0
        zRot -= 5.0
        glutPostRedisplay()
    elif key == GLUT_KEY_LEFT:
        yRot += 5.0
        glutPostRedisplay()
    elif key == GLUT_KEY_RIGHT:
        yRot -= 5.0
        glutPostRedisplay()
        
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
