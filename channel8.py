#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mail import send_email

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
from mail import send_email
import time
import datetime
from time import gmtime, strftime
from random import randint

import logging
logging.basicConfig(filename='channel8.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# ------------------------ 需要改的地方 ------------------------
# 8通道用户名密码
username = "oglops@gmail.com"
password = "fuckme@1123"
# 用于接收通知的email
notify_email = 'dmapo@qq.com'
# 几小时检查一次
check_interval = 12
# 随机加减几小时
rand_offset = 2
# 几折就发email提醒
discount_target = 80
# ---------------------------------------------------------------

channel8_url = "https://cityofhenderson.corporateperks.com/login"
lenovo_url = "https://shop.lenovo.com/perksoffer/us/en/landingpage/promotions/weekly-sale/thinkpad-laptops/"
passcode = "FLEN*2V"
t450s_url = "http://shop.lenovo.com/perksoffer/us/en/laptops/thinkpad/t-series/t450s/?__followRobots=true"


def check_test(driver=None):
    try:
        if driver is None:
            driver = webdriver.Firefox()

        driver.implicitly_wait(10)
        driver.get(channel8_url)

        # sign in channel 8
        try:
            fake_username = driver.find_elements_by_css_selector(
                "#fakeUsername")[0]
            fake_pwd = driver.find_elements_by_css_selector("#fakePassword")[0]
            fake_username.send_keys(username)
            fake_pwd.send_keys(password)
            driver.find_elements_by_css_selector(".signinImage")[0].click()
        except Exception as e:
            pass
            # print 'some error when logging in to channel 8',e

        driver.get(lenovo_url)
        wait = WebDriverWait(driver, 10)

        # enter passcode
        try:
            passcode_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="passcode"]')))
            passcode_input.send_keys(passcode)
            driver.find_elements_by_css_selector(".fbox")[0].click()
        except Exception as e:
            # print 'some error when logging in to channel 8',e
            pass

        # check t450s price
        driver.get(t450s_url)
        web_price = driver.find_elements_by_css_selector(
            ".webprice.pricingSummary-priceList-value")[0].text
        final_price = driver.find_elements_by_css_selector(
            ".aftercoupon.pricingSummary-details-final-price")[0].text

        web_price = float(web_price.split('$')[1])
        final_price = float(final_price.split('$')[1])

        print web_price, final_price

        discount = final_price / web_price * 100

        discount_percent = ("{0:.0f}%".format(discount))
        print discount_percent

        # send email if target discount is found
        if discount < discount_target:
            print 'yeah! Discount found!'
            logging.warning('good discount found %s' % discount_percent)
            send_email(notify_email, u'good t450s discount found %s！买买买！' %
                       discount_percent, u"钱包君在哭泣")
        else:
            logging.warning('current discount %s' % discount_percent)

    finally:
        # driver.close()
        pass


if __name__ == "__main__":

    driver = None
    once = False
    if len(sys.argv) == 2 and sys.argv[1] == '--once':
        once = True

    while True:
        try:
            now = datetime.datetime.now()
            print 'check ->', now.time().isoformat().split('.')[0], "%s/%s/%s" % (now.day, now.month, now.year)
            if driver is None:
                driver = webdriver.Firefox()
            check_test(driver)

        except Exception as e:
            print 'some error', e
        sleep_hours = randint(
            check_interval-rand_offset, check_interval+rand_offset)
        print 'sleep', sleep_hours, 'hrs'
        # time.sleep(sleep_hours*3600)
        if once:
            driver.close()
            break
        time.sleep(sleep_hours*2)
