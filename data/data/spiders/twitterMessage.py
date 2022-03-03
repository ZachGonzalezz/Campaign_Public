from time import sleep
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
import re
from selenium.common.exceptions import NoSuchElementException
import csv


class TwitterMessage(scrapy.Spider):
    name = 'twittermsg'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://twitter.com/i/flow/login',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):

        filename = "C:/Users/zacha/Life360Adventure/out.csv"
       

    # initializing the titles and rows list
        rows = []
        names = []
  

    # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            for row in rows:
                names.append(row[0])
               
     
        #this is the login page we insert out email click enter and wait
        driver = response.meta['driver']
        # sleep(10)
        # search_input = driver.find_element_by_xpath(
        #     "//input")
          
        # search_input.send_keys('zacharygonzalez123456@gmail.com')
        
        # search_input.send_keys(Keys.ENTER)
        # sleep(10)

        # #this is password page we insert our password and click enter
        # search_input = driver.find_element_by_xpath(
        #     "//input")
        # search_input.send_keys('Zg030104!')
        
        # search_input.send_keys(Keys.ENTER)
        # sleep(5)

        # #load the twitter page messages
        # driver.get('https://twitter.com/messages/compose')

        # sleep(5)
        sleep(180)

        #go through every user and message them
        index = 0
        
        for name in names:
            try:
                matches = []
                #load messages and search for specific user
                driver.get("https://twitter.com/messages/compose")
                # if(index == 59):
                #     sleep(500)
                #     index = 0
                index += 1
                sleep(5)
                try :
                    search_input = driver.find_element_by_xpath(
                        "//input")
                        #adding @ breaks it for some weird reason
                    search_input.send_keys(
                        f"{name}")
                except:
                    print('Weird Error on ' + name)
                
                sleep(2)
                #if name appears click on first one else continue
                # path to find first person is //div/div/div/div/div/div/div/div/div/div/div/div/div/div[@class='css-1dbjc4n r-13awgt0']/div/div/div/form/div/div/div[2]
                try :
                    #finds user based on user name
                    first_box = driver.find_element_by_xpath(
                    "//div/div/div/div/div/div/div/div/div/div/div/div/div/div[@class='css-1dbjc4n r-13awgt0']/div/div/div/form/div/div/div[2]")
                    
                    first_box.click()

                    sleep(5)

                    next_button = driver.find_element_by_xpath("//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']")
                                                            # css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr
                    next_button.click()

                    sleep(5)
                    search_input = driver.find_element_by_xpath(
                    "//div[@aria-autocomplete='list']")
                    search_input.send_keys(
                    f"Hey! Thank you for being an early supporter of mine. As you probably know, this is an election year and I am up for re-election already. In 2020 you helped me make history in South Carolina District 80 or the #New80 as we call it, but due to redistricting and the new gerrymandered maps, we will have to make history again. We need all hands on deck as we are running against another incumbent.To keep our hopes alive for UBI, medicaid expansion and new voices  in South Carolina, a donation from you would be a huge assistance. Will you chip in $10, $25, or $50 to help make history a second time?     https://secure.actblue.com/donate/johnson-for-sc-80-1?fbclid=IwAR061X95Li4Cu7YngxA0mA0-3sOK9jtGWk6ZhCgdqZvjp75dZFjYBx2ZzgY")

                    sleep(2)
                    search_input.send_keys(Keys.ENTER)

                    sleep(5)

                    print(name + ' Message Sent')
                except NoSuchElementException:
                    print(name + ' No go')
            except:
                sleep(60)
                print('\n\n\n\n\n\n\n\n\n\n\n\n CRITCAL ERROR \n\n\n\n\n\n\n\n\n\n\n\n')
    

          
            

            

        driver.save_screenshot("afterafterSearch.png")
