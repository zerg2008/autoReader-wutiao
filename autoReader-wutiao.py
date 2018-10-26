# coding=utf-8
from appium import webdriver
import time
desired_caps = {
                'platformName': 'Android',
                'deviceName': 'G2W7N15304007116',
                'platformVersion': '6.0',
                # apk包名
                'appPackage': 'com.kingnet.fiveline',
                # apk的launcherActivity
                'appActivity': 'com.kingnet.fiveline.ui.welcome.WelcomeActivity',
                'unicodeKeyboard': True,#使用UNICODE编码方式发送字符串
                'resetKeyboard': True#隐藏键盘
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
# 屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
# 屏幕向左滑动
def swipLeft(t):
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    driver.swipe(x1, y1, x2, y1, t)
# 屏幕向右滑动
def swipRight(t):
    l = getSize()
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2, y1, t)
#元素查找
def isFind(c):
    if driver.find_elements_by_id(c) == []:
        print(u"未找到元素")
        return  True
    else:
        print(u"找到元素")
        return False
print("opened")
time.sleep(25)
print("sleep end")
swipeDown(3000)
print(u"下滑刷新")
time.sleep(5)
ReadCound = 1 #记录自动阅读的次数
for i in range(21):
    time.sleep(1)
    swipeUp(3000)
    time.sleep(1)
    print(u"向下滑动6秒")
    driver.find_elements_by_class_name("android.view.ViewGroup")[0].click()
    time.sleep(2)
    if(isFind("com.kingnet.fiveline:id/ivAttendance")):
        print(u"点击的是视频，没有页面跳转，结束本次循环！")
        continue #跳出本次循环
    print(u"第%d此阅读",ReadCound)
    #print(u"点击了第一个内容")#前面加U中文就不会乱码，否则打印出来的中文是乱码
    time.sleep(6)
    print(u"等待6秒钟")
    count = 0
    while(isFind("com.kingnet.fiveline:id/mLayoutOperatePraise")):
        swipeUp(1000)
        time.sleep(2)
        print(u"下滑后，等待2秒钟")
        count = count+1
        if(count>25):
            break
        print(count)
    time.sleep(3)
    if(count<26):
        driver.find_element_by_id("com.kingnet.fiveline:id/mLayoutOperatePraise").click()
        time.sleep(1)
    driver.find_element_by_id("com.kingnet.fiveline:id/mTextCommentAction").click()
    #time.sleep(1)
    if(not(isFind('com.kingnet.fiveline:id/mEditCommentInput'))):
        searchInputBox = driver.find_element_by_id('com.kingnet.fiveline:id/mEditCommentInput')
        if (count < 6):
            searchInputBox.send_keys(u"真的是好内容啊！")
        elif((count>=6)and(count<14)):
            searchInputBox.send_keys(u"还不错哦！")
        else:
            searchInputBox.send_keys(u"嗯，我不太喜欢！")
        time.sleep(1)
        driver.find_element_by_id("com.kingnet.fiveline:id/mTextCommentAction").click()
        time.sleep(1)
        print(u"评论完毕")
    driver.back()
    print(u"返回首页")
    time.sleep(1)
    swipeUp(8000)
    print(u"向下滑动8秒")
    ReadCound = ReadCound + 1
