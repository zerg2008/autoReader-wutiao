# coding=utf-8

# 获得机器屏幕大小x,y
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
# 屏幕向上滑动
def swipeUp(driver,t):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
# 屏幕向下滑动
def swipeDown(driver,t):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
# 屏幕向左滑动
def swipLeft(driver,t):
    l = getSize(driver)
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    driver.swipe(x1, y1, x2, y1, t)
# 屏幕向右滑动
def swipRight(driver,t):
    l = getSize(driver)
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2, y1, t)

#元素查找
def isFind_byName(driver,c):
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
#元素查找
def isFind(driver,c):
    if driver.find_elements_by_id(c) == []:
        print(u"未找到元素")
        return  True
    else:
        print(u"找到元素")
        return False