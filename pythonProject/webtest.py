from selenium import webdriver
from time import sleep
#打开谷歌驱动和谷歌浏览器
driver=webdriver.Chrome(r'E:\chromedriver.exe')
driver.get('https://www.zhipin.com/')
sleep(3)
#得到下拉框
driver.find_element_by_class_name('label-text').click()
#得到技术  然后点击
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/form/div[4]/div/div/ul[1]/li[3]').click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/form/div[4]/div/div/ul[2]/li[3]').click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/form/div[4]/div/div/ul[3]/li[2]').click()
#driver.find_element_by_class_name('selected').click()
#driver.find_element_by_id('100000').click()
sleep(3)
ele=driver.find_element_by_name('query')
ele.send_keys('自动化测试工程师')
sleep(3)
driver.find_element_by_class_name('btn').click()
sleep(2)
# phone=driver.find_element_by_name('phone')
# phone.send_keys('18112984529')

pass


