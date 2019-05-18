from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import re

# Please change chrome driver location for your PC
driver = webdriver.Chrome('/Users/pc012/Documents/chromedriver')
driver.set_window_size(1440,900)
driver.get('http://www.lumine.ne.jp/ikebukuro/news/')
time.sleep(15)

plain_text = driver.page_source
soup = BeautifulSoup(plain_text, 'html.parser')

for a_tag in soup.find_all(['a'], attrs={'class': 'topics'}):
    text_div_tag = a_tag.find(['div'], attrs={'class': 'topicsInfo'})
    tmp = text_div_tag.text.split(" ",1)
    print (tmp[0])
    print (tmp[1])

    img_div_tag = a_tag.find('img', {'src':re.compile('.jpg')})
    print(img_div_tag['src']+'\n')
