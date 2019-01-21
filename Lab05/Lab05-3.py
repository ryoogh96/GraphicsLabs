from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

Ld = [1,1,1,1] # 광원 확산반사
Ls = [1,1,1,1] # 광원 경면반사 
Lp = [1,1,5,1] # 광원의 위치 
Md = [1,0,0,1] # 확산반사 입사광 색깔
Ms = [1,1,1,1] # 경면반사 입사광 색깔
shininess = [127.0] # 광원의 빛의 세기 

t = 0
spotlightAngle = 5.0

def LightSet():
    # 광원 설정 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, Ld) # 0번 광원 확산반사 특성 할당
    glLightfv(GL_LIGHT0, GL_SPECULAR, Ls) #spotlight setting
    glLightf (GL_LIGHT0, GL_SPOT_CUTOFF, 10.0) # 조명각 설정 각도 변경 
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0,0,-1]) # 방향 설정
    glLightf (GL_LIGHT0, GL_SPOT_EXPONENT, 3.0) # 승수 설정

    # 질감 설정
    glMaterialfv(GL_FRONT, GL_DIFFUSE, Md) # 확산반사 입사광 조명 설정
    glMaterialfv(GL_FRONT, GL_SPECULAR, Ms) # 경면반사 입사광 조명 설정 
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess) # 빛의세기 조명 설정 

def  LightPosition(t):

    global spotlightAngle

    if math.sin(t) > 0:
        spotlightAngle += 0.1
    else:
        spotlightAngle -= 0.1

    
    Lp[0] = 3.0*math.sin(t)
    Lp[1] = 3.0*math.cos(t)
    glLightf (GL_LIGHT0, GL_SPOT_CUTOFF, spotlightAngle) # spotlight 각도 실시간 변경
    glLightfv(GL_LIGHT0, GL_POSITION, Lp) # 0번 광원 위치 설정
    


def glInit():
    glClearColor(0,0,0.5,1)
    glEnable(GL_LIGHTING) # 조명 활성화
    glEnable(GL_LIGHT0) # 0번 광원 활성화
    glEnable(GL_DEPTH_TEST) # 물체 깊이 활성화 
    LightSet()




    

def disp() :
    global t, spotlightAngle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # CAMERA setting
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() #gluPerspective(60, 1.0, 0.1, 1000)
    glOrtho(-6,6,-6,6, -100,100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,10, 0,0,0, 0,1,0)
    #gluLookAt(0,10,0, 0,0,0, 0,0,1)
    t+= 0.01
    LightPosition(t) # OBJECTS
    # 화면상에 점 그려주는거 
    for x in range(-10, 11) :
        for y in range(-10, 11) :
            glPushMatrix()
            glTranslatef(x/2.0, y/2.0, 0)
            #glutSolidSphere(0.5, 20,20)
            glutSolidSphere(0.2, 20,20)
            glPopMatrix()

    glFlush()

def main():
    # windowing
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_RGB)
    glutInitWindowSize(512,512)
    glutInitWindowPosition(50,50)
    glutCreateWindow(b'Spot Lights')

    # initialization
    glInit()

    glutDisplayFunc(disp)
    glutIdleFunc(disp)

    # enter main loop
    glutMainLoop()

if __name__ == "__main__":
    main()




