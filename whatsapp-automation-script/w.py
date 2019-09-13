#!/usr/bin/env python
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
input("Enter any key after scanning.")

def myfunc():
    name = input("Enter the name : ")
    msg = input("Enter msg : ")
    c = int(input("Number of msgs : "))
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(c):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)

def exit():
    driver.quit()
    global c
    c=0

switch = {'1':myfunc,'2':exit}
c=1

while (c==1):
    argument = input("Press 1 for sending msg and Press 2 to exit : ")
    switch[argument]()
