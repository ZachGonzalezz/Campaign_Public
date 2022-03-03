from time import sleep
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
import re

import csv


class TwitterSpider(scrapy.Spider):
    name = 'twitter'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://twitter.com/Dr_JLJohnson/followers',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        
        driver = response.meta['driver']
        sleep(20)
        # driver.get('https://twitter.com/Dr_JLJohnson/followers')
        # follwersBtn = driver.find_element_by_xpath("//a[contains(@href, 'followers')]")
        # follwersBtn.click()
        # search_input = driver.find_elements_by_xpath(
        #     "//input[@class='gLFyf gsfi']")
        # sleep(30)
        for number in range(1, 10000000):
            sleep(2)
            driver.execute_script("window.scrollTo(0, 10000);")

        
 
