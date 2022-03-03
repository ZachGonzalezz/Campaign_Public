from time import sleep
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
import re

import csv


class GoogleSearchSpider(scrapy.Spider):
    name = 'googleSearch'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):

        filename = "C:/Users/zacha/Life360Adventure/data/data/spiders/mainList.csv"
        filenameAreaCode = "C:/Users/zacha/Life360Adventure/data/data/spiders/areaCodes.csv"

    # initializing the titles and rows list
        rows = []
        names = []
        area_codes = []

    # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            for row in rows:
                nameOfPerson = row[0].split(' ')
                names.append(nameOfPerson[1] + ' ' + nameOfPerson[0])
                # if row[1] != '':
                #     area_codes.append(row[1])
        with open(filenameAreaCode, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            rows.clear()

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            for row in rows:

                if row[1] != '':
                    area_codes.append(row[1])

        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath(
            "//input[@id='search_form_input_homepage']")

        phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)
        index = 0;
        for name in names:
            matches = []
            driver.get("https://duckduckgo.com")
            if(index == 59):
                sleep(500)
                index = 0
            index += 1
            sleep(5)
            search_input = driver.find_element_by_xpath(
                "//input[@id='search_form_input_homepage']")
            search_input.send_keys(
                f"site:https://www.truepeoplesearch.com/ \"{name}\"")
            driver.save_screenshot("after.png")

            search_input.send_keys(Keys.ENTER)
            sleep(5)
            driver.save_screenshot("afterSearch.png")
            # for number in range(1, 3):
            #     if len(driver.find_elements_by_xpath("//a[@class='result--morebtn btn btn--full']")) > 0:

            #         driver.find_element_by_xpath(
            #             "//a[@class='result--morebtn btn btn--full']").click()
            #         sleep(1.5)
            #     index = 0
            
            for areaCode in area_codes:
                    for phonenumber in driver.find_elements_by_xpath(f"//*[contains(text(), {areaCode})]"):
                        for groups in phoneRegex.findall(phonenumber.text):
                            
                            phoneNum = '-'.join([groups[1],
                                                groups[3], groups[5]])
                            if groups[8] != '':
                                phoneNum += ' x' + groups[8]
                            matches.append(phoneNum)
            res = []
            for i in matches:
                 if i not in res:
                    res.append(i)
            yield{
                "Name" : name,
                "Numbers" : res
            }

            

        driver.save_screenshot("afterafterSearch.png")
