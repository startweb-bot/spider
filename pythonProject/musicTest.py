from selenium import webdriver
from time import sleep
driver=webdriver.Chrome(r'E:\chromedriver.exe')
#打开酷狗音乐
driver.get('https://www.zhipin.com/?ka=header-home')




# sleep(2)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/ul/li[2]/a').click()
# sleep(2)
# driver.find_element_by_id('geetVerifyBtn').click()
#
# driver.find_element_by_class_name('geetest_commit')

# sleep(2)
# driver.find_element_by_name('account').send_keys('18112984529')
# sleep(2)
# driver.find_element_by_name('password').send_keys('zheng001227')
# sleep(2)
# #driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/form/div[5]/div[1]/div/div[2]/div[1]/div[3]').click()
# #driver.find_element_by_class_name('geetest_radar_tip_content').click()
# driver.find_element_by_class_name('btn').click()
