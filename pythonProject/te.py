from appium import webdriver
import os
import time
import base64

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'    #手机类型
desired_caps['platformVersion'] = '7.1.2'   #手机操作系统版本
desired_caps['deviceName'] = '127.0.0.1:62001'   #使用的手机或模拟器类型
desired_caps['appPackage'] = 'com.kugou.android'   # 使用的apk包名
desired_caps['appActivity'] = '.app.MediaActivity'              # 应用包名
desired_caps['noReset'] = 'True'

#声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#id、class、xpath


#点击WLAN
driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]").click()


# driver.find_element_by_id("com.android.settings:id/tile_item").click()

#返回
driver.find_element_by_class_name("android.widget.ImageButton").click()


#查找一组元素
driver.find_elements_by_class_name("android.widget.TextView")

#强制等待
time.sleep(4)


#显示等待
try:
    WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_xpath("//*[contains(@text, '设置')]"))
    print("找到了")
except:
    print("找不到超时了")

print(driver.find_elements_by_xpath("//*[contains(@text, '设置')]"))


#隐士等待,所有的操作页面默认等待3秒
driver.implicitly_wait(3)
print(driver.find_elements_by_xpath("//*[contains(@text, '设置')]"))


driver.close_app()
driver.quit()