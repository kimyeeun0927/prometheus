'''
2491007 김예은

물방울 피하기 게임입니다!

일반 모드(노랑 상어)일때는 a/d로 옆으로 왔다갔다만 할 수 있고,
물방울에 하나 맞을 때마다 왼쪽 상단에 하트가 하나씩 차감되며
하트가 모두 차감되고 한 대 더 맞았을 때 게임이 종료됩니다.

치트 모드(파랑 상어)일때는 a/d로 옆으로 갈 수 있을 뿐더러 w/s로 앞뒤로 움직이는 기능이 추가됩니다.
물방울에 맞아도 하트가 닳지않고, 물방울이 역행합니다!

'''

import gui_core as gui
import random

w = gui.Window()

def initialize(timestamp):
    w.data.x = 350
    w.data.y = 520
    w.data.r = 0
    w.data.heart =3

    w.data.protagonist = w.newImage(w.data.x, w.data.y, 'shark_normal.png', 70, 70)
    
    w.data.width_image = 50
    w.data.filenames = ['drop1.png', 'drop2.png', 'drop3.png']
    w.data.objs = []
    w.data.life1 = w.newImage(10, 10, 'heart.png', 30, 30)
    w.data.life2 = w.newImage(50, 10, 'heart.png', 30, 30)
    w.data.life3 = w.newImage(90, 10, 'heart.png', 30, 30)
    w.data.life = [w.data.life1, w.data.life2, w.data.life3]
    
    
    for i in range(5):
        idx_filenames = random.randint(0,len(w.data.filenames)-1)
        pos_x = random.randint(0, 800 - w.data.width_image)
        pos_y = 0
        vel_y = random.random()*14 + 1

        global number
        number = w.newImage(pos_x, pos_y, w.data.filenames[idx_filenames], w.data.width_image, w.data.width_image)
        w.data.objs.append([number, pos_x, pos_y, vel_y])
            



def update(timestamp):
    if w.keys['r']:
        w.deleteObject(w.data.protagonist)
        w.data.protagonist = w.newImage(w.data.x, w.data.y, 'shart_power.png', 70, 70)
        w.data.r = 1

    if w.data.r ==1:
        if w.keys['w']:
            w.data.y -=7
        if w.keys['s']:
            w.data.y +=7
    if w.keys['a']:
        w.data.x -=7
    if w.keys['d']:
        w.data.x +=7

    w.moveObject(w.data.protagonist, w.data.x, w.data.y)

        
    if w.keys['Escape']:
        w.stop()
        return
    
    if w.data.r == 0:
        for obj in w.data.objs:
            obj[2] += obj[3]
            w.moveObject(obj[0], obj[1], obj[2])

            xp, yp = w.getPosition(w.data.protagonist)
            xd, yd = w.getPosition(obj[0])

            
            if (xp <= xd+50) and (xd <= xp+70) :
                if yp<= yd+60 <= yp+70:
                    w.data.heart -= 1
                    obj[2] = 800

                    if w.data.heart >= 0:
                        k = w.data.life[w.data.heart]
                        w.hideObject(k)

                
            if obj[2] >=600:
                obj[2] = 0
                obj[1] = random.randint(0, 800 - w.data.width_image)
                w.moveObject(obj[0], obj[1], obj[2])

            if w.data.heart == -1:
                w.stop()
                return

           
    if w.data.r == 1:
        for obj in w.data.objs:
            obj[2] -= obj[3]
            w.moveObject(obj[0], obj[1], obj[2])    

                
            if obj[2] <=0:
                obj[2] = 600
                obj[1] = random.randint(0, 800 - w.data.width_image)
                
       


w.initialize = initialize
w.update = update

w.start()
