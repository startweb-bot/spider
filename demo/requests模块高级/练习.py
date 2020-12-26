
#使用selenium打开登陆页面
from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://kyfw.12306.cn/otn/login/init')
time.sleep(1)

#save_screenshot就是将当前页面进行截图且保存
bro.save_screenshot('aa.png')

# 确定验证码图片对应的左上角和右下角的坐标（裁剪的区域就确定）
code_img_ele = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
location = code_img_ele.location #验证码图片上的坐标x，y
print('location:',location)
size = (code_img_ele.size)
size = {'width': int(size['width'])*1.5, 'height': int(size['height'])*1.5}#验证码标签对应的长和宽
print('size:',size)
#左上角和右下角坐标
rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))

# rangle = (int(location['x'])*1.5, int(location['y'])*1.5, int(location['x'] + size['width'])*1.5, int(location['y'] + size['height'])*1.5)
#至此验证码图片区域就确定下来了

# # im = Image.open('./12306.jpg')
i = Image.open('./aa.png')
code_img_name ='./code.png'
#crop根据指定区域进行图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)