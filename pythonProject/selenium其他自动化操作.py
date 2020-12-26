from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='chromedriver')

bro.get('https://weibo.com/')

username = bro.find_element_by_id('loginname')
password = bro.find_element_by_name('password')

