import os
import sys
import time
import urllib.request
import urllib.parse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

series = input("Enter sereis url bit: ")
ch_s = input("Enter start chapter num: ")
start_url = input("Enter start url: ")

driver = webdriver.Firefox()
chapter = int(ch_s)
current_dir = "C:\\Users\\Alexander\\Documents\\Manga\\"+str(series)+"\\"+str(series)+" " + str(ch_s)
try:
    os.makedirs(current_dir)
except:
    pass
driver.get(str(start_url))
time.sleep(10)
img_num = 1
while(1):
    #try:
    #time.sleep(10)
    link = driver.find_element_by_id("imgCurrent")
    #except:
        #link = driver.find_element_by_id("btnNext")

    temp_x = driver.current_url.split('?')[0]
    temp_y = start_url.split('?')[0]
    if temp_x != temp_y:
    #if driver.current_url.find(chapter) == -1:
        #chapter = "Chapter-"+str(int(chapter.split("-")[1])+1) #Update this line to handle 0xx and 00x chapters
        start_url = driver.current_url
        img_num = 1
        chapter += 1
        current_dir = "C:\\Users\\Alexander\\Documents\\Manga\\"+series+"\\"+series+" " + str(chapter)
        os.makedirs(current_dir)
    
    url = link.get_attribute("src")
    url_temp = urllib.parse.unquote(url)
    url_s = url.find("&url=")
    url = url[url_s+5:]
    url = urllib.parse.unquote(url)
    if not url.startswith("http"):
        url = "http" + url

    try:
        urllib.request.urlretrieve(url, current_dir+"\\page_"+str(img_num)+".jpg")
    except:
        urllib.request.urlretrieve(url_temp, current_dir+"\\page_"+str(img_num)+".jpg")    

    #link.click()
    #link.send_keys(Keys.ARROW_RIGHT)
    #driver.send_keys(Keys.ARROW_RIGHT)
    driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
    
    #driver.get("http://kissmanga.com/Content/images/next.png")
    time.sleep(10)
    
    img_num += 1
