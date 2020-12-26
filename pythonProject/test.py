from appium import webdriver
import time
import xlwt
# 设置appium的配置

desired_caps = {}
desired_caps['platformName'] = 'Android'    #手机类型
desired_caps['platformVersion'] = '7.1.2'   #手机操作系统版本
desired_caps['deviceName'] = '127.0.0.1:62001'   #使用的手机或模拟器类型
desired_caps['appPackage'] = 'com.kugou.android'   # 使用的apk包名
desired_caps['appActivity'] = '.app.MediaActivity'              # 应用包名
desired_caps['noReset'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  #调用appium的驱动
time.sleep(1)
driver.find_element_by_id('com.kugou.android:layout/b').click()
time.sleep(1)
driver.find_element_by_id('com.kugou.android:id/hu1').click()
# print(ss.text)
time.sleep(2)
te = driver.find_elements_by_id('com.kugou.android:id/b2w')
time.sleep(2)
de = driver.find_elements_by_id('com.kugou.android:id/b2x')
names_list=[]
for j in de:
    names_list.append(j.text)



name_list=[]
for i in te:
    name_list.append(i.text)


book=xlwt.Workbook()
sh=book.add_sheet("统计")

row=0
clo=0
for name in name_list:
    #print(name)
    sh.write(row,clo,name)
    row +=1
clo1=1
row1=0
for name in names_list:
    #print(name)
    sh.write(row1,clo1,name)
    row1 +=1
book.save('E:\\w3.xls')
# sh.write(row,clo,name.text)
# print(te)
# name_list = []
# for i in te:
#     # print(i.text)
#     name_list.append(i.text)
#
# # print(name_list)
#
# if '灵猫传' in name_list:
#     print('通过')
#
# else:
#     print('不通过')


# ele=driver.find_elements_by_id('com.kugou.android:id/b2w')
# for i in ele:
#     print(i)

#ele[0].click()
#for i in ele:


# print(ele[0].text)
# for e in ele:
#     print(e.text)

# e=driver.find_element_by_xpath("//*[contains(@id='com.kugou.android:id/b2w')]")
# print(e)
# ele=driver.find_elements_by_id('com.kugou.android:id/a0k')
# print('内容是'+ele[0].text)

# for e in  ele:
#     print(e)

 # print(ele)
#print(ele[1].text)
#同城点击
#driver.find_element_by_id('com.ss.android.ugc.aweme:id/iny').click()

# s=driver.find_element_by_id('com.ss.android.ugc.aweme:id/f06').text
# print(s)
# while True:
#   #喜欢点击
#   driver.find_element_by_id('com.ss.android.ugc.aweme:id/bdo').click()
#   time.sleep(2)
#   driver.swipe(200,1300,200,300)

# 退出程序
