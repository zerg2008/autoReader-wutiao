# coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

desired_caps = {
                'platformName': 'Android',
                'deviceName': 'G2W7N15304007116',
                'platformVersion': '6.0',
                # apk包名
                'appPackage': 'com.kingnet.fiveline',
                # apk的launcherActivity
                'appActivity': 'com.kingnet.fiveline.ui.welcome.WelcomeActivity',
                # 'unicodeKeyboard': True,#使用UNICODE编码方式发送字符串
                # 'resetKeyboard': True#隐藏键盘
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

def is_toast_exist(driver,toastmessage,timeout=30,poll_frequency=0.5):
        '''is toast exist, return True or False
        :Agrs:
         - driver - 传driver
         - toastmessage   - 页面上看到的toast消息文本内容
         - timeout - 最大超时时间，默认30s
         - poll_frequency  - 间隔查询时间，默认0.5s查询一次
        :Usage:
         is_toast_exist(driver, "toast消息的内容")
        '''
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % toastmessage)
            WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
            return True
        except:
            return False
#元素查找
def isFind_byName(c):
    if driver.find_elements_by_name(c) == []:
        print(u"未找到元素")
        return  False
    else:
        print(u"找到元素")
        return True
 #提供一个作者列表，如果文章的作者在列表中，则返回True
 #否则，返回False
def find_by_Auth(AuthList):
    result = False
    for Author in AuthList:
        if(isFind_byName(Author)):
            result = True
            break
    return result
print("opened")
time.sleep(25)
print("sleep end")
ReadCound = 1 #记录投票次数
driver.find_element_by_name(u"发现者").click()
print(u"进入发现者页面")
#点击发现者页面
time.sleep(2)
driver.find_element_by_name(u"发现内容").click()
print(u"进入内容投票页面")
#点击进入内容投票页面
time.sleep(2)
authorList = [u"人民网",u"36氪",u"小格说娱",u"科技早报",u"家乡体育",u"新华社",u"五条号",u"中国证券报",u"娱乐草莓",u"时刻体育"]
for i in range(50):
    print("the %d times finds" % ReadCound)
    time.sleep(5)
    if(find_by_Auth(authorList)):
        time.sleep(20)
        driver.find_element_by_name(u"发现者投票").click()
    # if(is_toast_exist(driver,u"审核内容")):
    #     print(u"可以投票了")
    #     driver.find_element_by_name(u"发现者投票").click()
    # else:
    #     print(u"没有找到")

    time.sleep(1)
    driver.find_element_by_name(u"换一篇").click()
    ReadCound = ReadCound + 1
