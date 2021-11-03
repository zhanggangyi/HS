import pyautogui
import time
from goto import *
#保护措施，避免失控
pyautogui.FAILSAFE = False
#为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
pyautogui.PAUSE = 0.4
rounds = 1
TOTAL_ROUND = 4
merc_list = ['Cairne','Malfurion','Anduin']
merc_attack = {'Millhouse','Dawngrasp','Krush'} #0无目标攻击 1有目标攻击
raid = '1-2'
region = 'barren'
time.sleep(10) #炉石就绪

def wait_until(image,mode,cof = 0.5): #0什么也不做 1出现了就点 3 不出现时一直点
    counter = 0
    while (1):
        loc = pyautogui.locateCenterOnScreen(image, confidence=cof)
        if (loc == None and counter != 30):
            time.sleep(1)
            if mode == 3:
                pyautogui.click()
            counter = counter+1
        elif counter == 30:
            restart()
        else:
            if mode == 1:
                pyautogui.moveTo(x=loc.x, y=loc.y, tween=pyautogui.linear)
                pyautogui.click()
            break
def attack():
    im = pyautogui.screenshot()
    for i in range(500,1000):
        rgb1 = im.getpixel((i,291))
        rgb2 = im.getpixel((i+1,291))
        if abs(rgb1[0]-rgb2[0])+abs(rgb1[1]-rgb2[1])+abs(rgb1[2]-rgb2[2]) >100:
            first_target = (i+50,291)
            break

    for i in merc_list:
        loc = pyautogui.locateCenterOnScreen('./merc_battle/'+i+'.png', confidence=0.7, region=(0, 540, 1920, 540))
        if loc==None:
            continue
        pyautogui.moveTo(x=loc.x, y=loc.y, tween=pyautogui.linear)
        pyautogui.click()

        pyautogui.moveTo(x=779, y=482, tween=pyautogui.linear)
        pyautogui.click()

        if i not in merc_attack:
            pyautogui.moveTo(x=first_target[0], y=first_target[1], tween=pyautogui.linear)
            pyautogui.click()

        pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
        pyautogui.click()


def battle(mode = 0):
    flag = True
    wait_until('yidengchang.png',0)
    #登场1573 479
    pyautogui.moveTo(x=1573, y=479, tween=pyautogui.linear)
    pyautogui.click()
    pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)

    while flag:
        wait_until('jiuxu.png',0)
        time.sleep(1)
        pyautogui.moveTo(x=100, y=100,tween=pyautogui.linear)
        pyautogui.click()

        #攻击
        attack()
        #就绪

        pyautogui.moveTo(x=1573, y=479, tween=pyautogui.linear)
        pyautogui.click()
        pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)

        while 1:
            loc1 = pyautogui.locateCenterOnScreen('win.png', confidence=0.5)
            loc2 = pyautogui.locateCenterOnScreen('jiuxu.png', confidence=0.5)
            loc3 = pyautogui.locateCenterOnScreen('yidengchang.png', confidence=0.5)
            loc4 = pyautogui.locateCenterOnScreen('loss.png', confidence=0.5)
            if (loc1 != None):
                pyautogui.click()
                flag = False
                break
            elif (loc2 != None):
                break
            elif(loc3 != None):
                pyautogui.moveTo(x=loc3.x, y=loc3.y, tween=pyautogui.linear)
                pyautogui.click()
                pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
            elif (loc4 != None):
                pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
                wait_until(region+'.png',cof = 0.5,mode = 3)
                with_goto(main())
            else:
                time.sleep(1)

    # 等一会(动画）
    if mode == 0:
        pyautogui.click()
        pyautogui.click()
        wait_until('baozang.png',3)

        # 1146 493 选宝藏
        pyautogui.moveTo(x=1146, y=493, tween=pyautogui.linear)
        pyautogui.click()
        # 1149 856 确定宝藏
        pyautogui.moveTo(x=1149, y=856, tween=pyautogui.linear)
        pyautogui.click()
        wait_until('chakanduiwu.png',0)
        time.sleep(1)


def restart ():
    pyautogui.hotkey('alt','f4')
    flag = True
    #开游戏
    while(flag):
        loc1 = pyautogui.locateCenterOnScreen('heartstone.png',confidence = 0.5)
        loc2 = pyautogui.locateCenterOnScreen('battle.net.png', confidence=0.8)
        if(loc1 == None and loc2 == None):
            time.sleep(1)
        elif loc1 != None:
            while (1):
                loc = pyautogui.locateCenterOnScreen('enter.png', confidence=0.8)
                if(loc == None):
                    time.sleep(1)
                else:
                    pyautogui.moveTo(x=loc.x, y=loc.y, tween=pyautogui.linear)
                    pyautogui.click()
                    flag = False
                    break
        elif loc2 !=None:
            pyautogui.moveTo(x=loc2.x, y=loc2.y, tween=pyautogui.linear)
            pyautogui.click()
        else :
            time.sleep(1)

    wait_until('kaishi.png',0)
    pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
    pyautogui.click()
    pyautogui.moveTo(x=200, y=200,duration=30, tween=pyautogui.linear)
    loc = pyautogui.locateCenterOnScreen('jiuxu.png',confidence = 0.5)
    if loc != None:
        pyautogui.hotkey('esc')
        # 认输961 386
        pyautogui.moveTo(x=961, y=386, tween=pyautogui.linear)
        pyautogui.click()
        pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
        time.sleep(5)
        wait_until(region+'.png', 3)
        wait_until(raid+'.png', 1)
    else:
        pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
        pyautogui.click()
        wait_until('yongbing.png',1,cof = 0.8)
        time.sleep(8)
        loc = pyautogui.locateCenterOnScreen('chest2.png',confidence = 0.7)
        if loc !=None:
            pyautogui.moveTo(x=loc.x, y=loc.y, tween=pyautogui.linear)
            pyautogui.click()
            time.sleep(1)



            # 四个宝箱
            # 743 242
            pyautogui.moveTo(x=743, y=242, tween=pyautogui.linear)
            pyautogui.click()
            # 754 734
            pyautogui.moveTo(x=618, y=679, tween=pyautogui.linear)
            pyautogui.click()
            # 1349 759
            pyautogui.moveTo(x=1158, y=811, tween=pyautogui.linear)
            pyautogui.click()
            pyautogui.moveTo(x=1299, y=331, tween=pyautogui.linear)
            pyautogui.click()

            wait_until('finish.png',mode = 1)
            time.sleep(5)


        wait_until('lvxingdian.png', 1,cof = 0.7)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
        time.sleep(5)
        #判断
        loc = pyautogui.locateCenterOnScreen('choose.png')
        if loc == None:
            pyautogui.moveTo(x=200, y=200,duration = 5, tween=pyautogui.linear)
            loc = pyautogui.locateCenterOnScreen('baozang.png',confidence = 0.7)
            if loc !=None:
                pyautogui.moveTo(x=1146, y=493, tween=pyautogui.linear)
                pyautogui.click()
                # 1149 856 确定宝藏
                pyautogui.moveTo(x=1149, y=856, tween=pyautogui.linear)
                pyautogui.click()
                time.sleep(5)
            time.sleep(3)
            # 查看队伍775 993
            pyautogui.moveTo(x=775, y=993, tween=pyautogui.linear)
            pyautogui.click()
            # 放弃 1088 791
            time.sleep(1)
            pyautogui.moveTo(x=1088, y=791, tween=pyautogui.linear)
            pyautogui.click()
            # 确定放弃 821 604
            pyautogui.moveTo(x=821, y=604, tween=pyautogui.linear)
            pyautogui.click()

            pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
            wait_until(region+'.png', 3)
            wait_until(raid+'.png', mode=1, cof=0.8),
        else:
            pyautogui.moveTo(x=loc.x, y=loc.y, tween=pyautogui.linear)
            pyautogui.click()
            wait_until(raid+'.png',mode =1, cof = 0.8),
    with_goto(main())

def round():
    # 1494 829 右下角蓝色选择按钮
    time.sleep(2)
    wait_until('start.png',mode = 1, cof = 0.7)
    pyautogui.click()
    battle()
    count = 2
    while(count != TOTAL_ROUND):
        # 507 504第一个位置
        pyautogui.moveTo(x=770, y=504, tween=pyautogui.linear)
        pyautogui.click()
        # 575 504
        pyautogui.moveTo(x=830, y=504, tween=pyautogui.linear)
        pyautogui.click()
        # 650 500
        pyautogui.moveTo(x=890, y=500, tween=pyautogui.linear)
        pyautogui.click()
        # 725 500
        pyautogui.moveTo(x=970, y=500, tween=pyautogui.linear)
        pyautogui.click()
        pyautogui.moveTo(x=1050, y=500, tween=pyautogui.linear)
        pyautogui.click()
        time.sleep(2)

        loc = pyautogui.locateCenterOnScreen('start.png',confidence = 0.7)
        loc1 = pyautogui.locateCenterOnScreen('blue_portal.png',confidence = 0.7)
        loc2 = pyautogui.locateCenterOnScreen('shenmiren.png',confidence = 0.7)
        if(loc != None):#战斗
            count = count + 1
            pyautogui.moveTo(x=1494, y=829, duration=2, tween=pyautogui.linear)
            pyautogui.click()
            battle()
        elif loc1 != None : #blue portal
            pyautogui.moveTo(x=1494, y=829, duration=2, tween=pyautogui.linear)
            pyautogui.click()
            count = TOTAL_ROUND
        elif loc2 != None : #神秘人
            count = count + 1
            pyautogui.moveTo(x=1494, y=829, duration=2, tween=pyautogui.linear)
            pyautogui.click()
            # 第一个627 430
            pyautogui.moveTo(x=627, y=430, tween=pyautogui.linear)
            pyautogui.click()
            #确定929 733
            pyautogui.moveTo(x=929, y=733, tween=pyautogui.linear)
            pyautogui.click()
        else:
            pyautogui.moveTo(x=1494, y=829, duration=2, tween=pyautogui.linear)
            pyautogui.click()
            pyautogui.click()
            count = count + 1
        pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
        pyautogui.click()
        time.sleep(5)
        wait_until('chakanduiwu.png',mode = 3)
        time.sleep(1)

    #boss战
    pyautogui.moveTo(x=1494, y=829, duration=2, tween=pyautogui.linear)
    pyautogui.click()
    battle(mode = 1)

#主程序

def main():
    while 1:
        pyautogui.moveTo(x=1494, y=829, tween=pyautogui.linear)
        pyautogui.click()

        #1411 899 第二次选择
        pyautogui.moveTo(x=1411, y=899,duration=1, tween=pyautogui.linear)
        pyautogui.click()

        pyautogui.moveTo(x=845, y=615,duration=1, tween=pyautogui.linear)
        pyautogui.click()

        round()

        pyautogui.moveTo(x=100, y=100, duration=1, tween=pyautogui.linear)
        wait_until('chest.png', 3)

        loc = pyautogui.locateCenterOnScreen('chest.png',confidence = 0.5)
        while loc != None:
            pyautogui.moveTo(x=loc.x,y=loc.y)
            pyautogui.click()
            loc = pyautogui.locateCenterOnScreen('chest.png', confidence=0.5)

        wait_until('finish.png',mode = 1)
        pyautogui.click()

        wait_until('confirm.png',mode = 1)

        pyautogui.moveTo(x=100, y=100, tween=pyautogui.linear)
        wait_until(region+'.png',mode = 3)


if __name__ == '__main__':
    main()

