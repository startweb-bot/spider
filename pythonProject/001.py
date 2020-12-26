from appium import webdriver
import time

caseInfo={
    #测试平台
   'platformName':'Android',
    #测试平台的版本
    'platformVersion':'10.0.0',
    #设备名称:可以随便去写，但是不可以为空但是ios设备名称必须要填写正确
    'deviceName':'AKC0218907001642',
    #app包名
    'appPackage':'com.ss.android.ugc.aweme',
    #应用名称，界面名称
    'appActivity':'.app.splash.SplashActivity',
    'noReset':True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caseInfo)
# time.sleep(3)
# driver.quit()
