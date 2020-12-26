from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://mail.qq.com/')

bro.switch_to.frame('login_frame')
sleep(3)
# a_tag = bro.find_element_by_id("uin_del")
# a_tag.click()
#
userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('3233877662')
sleep(1)
password_tag.send_keys('1234567890')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()

sleep(3)
#
# bro.quit()