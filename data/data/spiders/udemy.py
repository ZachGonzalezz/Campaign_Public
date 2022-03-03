from time import sleep
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
import re
from selenium.common.exceptions import NoSuchElementException
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy_cloudflare_middleware.middlewares import CloudFlareMiddleware
import undetected_chromedriver as uc

class UdemySpider(scrapy.Spider):
    name = 'udemy'
    # allowed_domains = ['www.udemy.com']
    # start_urls = ['http://www.udemy.com/']

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.google.com/',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )
    def parse(self, response):
        opts = Options()
        opts.add_argument("start-maximized")
        opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")

        driver = webdriver.Chrome(chrome_options=opts)
        # driver = response.meta['driver']
        driver.get('https://www.udemy.com/')
        sleep(2)
        textField = driver.find_element_by_xpath("//input[@placeholder='Search for anything']")
         # database is searched by last name only so we send it a last name
        textField.send_keys('programming')
        sleep(3)
            # press enter a wait for results to load
        textField.send_keys(Keys.ENTER)
        sleep(90)



        courseUrls = []

        coursesOnCurrentPage = driver.find_elements_by_xpath("//a[contains(@href, 'course/')]")

        for course in coursesOnCurrentPage:
            courseUrls.append(course.get_attribute('href'))

        print(courseUrls)

