import  pygame
import math

pygame.init()
win=pygame.display.set_mode((600, 600))
r=152685
run=True
bg=pygame.image.load('img/bg.jpg')
raket=pygame.image.load('img/raket.png')
start=pygame.image.load('img/start.png')
finish=pygame.image.load('img/mars.png')
bg=pygame.transform.scale(bg, (600,600))
raket=pygame.transform.scale(raket, (180,180))
start=pygame.transform.scale(start, (600,200))
finish=pygame.transform.scale(finish, (180, 180))
x=210
y=400
t=0
startb=True
finishb=False
v=[1000]
a=[100]
h=[1000]
m=[0]
u=100
vt=[1000]
mtop=30000
mob=6000
mt=[0]
m[0]=mtop+mob
mt[0]=m[0]
maxdmdt=300
dmdt=100

def accel(mt, dmdt, u):
    ans=dmdt*u/mt-3.721
    return ans
def verlet(dmdt, dt):
    global v, a, m ,h
    h.append(h[-1]+v[-1]*dt+0.5*a[-1]*(dt**0.5))
    a.append(accel(m[-1], dmdt, u))
    v.append(v[-1]+0.5*(a[-1]+a[-2])*dt)
    print('\n'+'Высота:' + str(h[len(h)-1]))
    print('Ускорение:' + str(abs(a[len(a) - 1])))
    print('Скорость:' + str(abs(v[len(v) - 1])))
def cialk(t):
    global vt, mt
    mt.append(m[0]-dmdt*t)
    vt.append(vt[0]-100*math.log(m[0]/mt[len(mt)-1])+3.721)
    print('Циолковский: '+ str(abs(vt[len(vt) - 1])))
def draw():
    win.blit(bg, (0,0))
    if startb:
        win.blit(start, (0, win.get_height()-200))
    if finishb:
        win.blit(finish, (210,90))
    win.blit(raket, (x,y))
    pygame.display.update()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dmdt += maxdmdt / 10
        # x+=10
    if keys[pygame.K_DOWN]:
        dmdt -= maxdmdt / 10
        # x-=10
    if y!=0 and y<=400:
        verlet(dmdt, 0.5)
        cialk(t)
    t+=0.5
    if(h[len(h)-1]>h[len(h)-2]):
        if y>=200:
            y-=1
        elif y<200 and h[len(h)-1]<132685:
            startb=False
        if h[len(h)-1]>=132685:
            finishb=True
            y-=1
        elif h[len(h)-1]==r:
            y=0
        if y<=180:
            y=0
    else:
        if y>=200:
            y+=1
        elif y<200 and h[len(h)-1]<132685:
            startb=False
        if h[len(h)-1]>=132685:
            finishb=True
            y+=1
        elif h[len(h)-1]==r:
            y=0
        if y<=180:
            y=0
    draw()

pygame.quit()