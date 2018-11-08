# coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import tools

desired_caps = {
                'platformName': 'Android',
                'deviceName': 'G2W7N15304007116',
                'platformVersion': '6.0',
                # apk包名
                'appPackage': 'com.baidu.searchbox.lite',
                # apk的launcherActivity
                'appActivity': 'com.baidu.searchbox.SplashActivity',
                # 'unicodeKeyboard': True,#使用UNICODE编码方式发送字符串
                # 'resetKeyboard': True#隐藏键盘
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print("opened")
time.sleep(15)
print("sleep end")
#tools.swipeDown(driver,3000)
print(u"下滑刷新")
#time.sleep(5)
ReadCound = 1 #记录自动阅读的次数
for i in range(55):
    time.sleep(1)
    tools.swipeUp(driver,3000)
    time.sleep(1)
    print(u"向下滑动3秒")
    driver.find_elements_by_class_name("android.widget.RelativeLayout")[0].click()
    time.sleep(8)
    if(not(tools.isFind_byName(driver,u"关注"))):
        time.sleep(6)
        driver.back()
        print(u"点击的是视频，没有页面跳转，结束本次循环,返回首页！")
        continue #跳出本次循环
    print("the %d times Read" %ReadCound)#python 中打印带格式的参数时，字符串与说明之间不用逗号隔开，注意！！
    #print(u"点击了第一个内容")#前面加U中文就不会乱码，否则打印出来的中文是乱码
    time.sleep(6)
    print(u"等待6秒钟")
    for i in range(12):
        tools.swipeUp(driver,800)
        time.sleep(2)
        print(u"下滑后，等待2秒钟")
    time.sleep(3)
    driver.back()
    print(u"返回首页")
    time.sleep(1)
    tools.swipeUp(driver,4000)
    print(u"向下滑动8秒")
    ReadCound = ReadCound + 1