from time import sleep
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv




class TruepeopleSpider(scrapy.Spider):
    name = 'truePeople'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.truepeoplesearch.com',
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

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            for row in rows:
              
                if row[1] != '':
                      area_codes.append(row[0])
        
        

    
        
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36t")

        driver = webdriver.Chrome(chrome_options=opts, executable_path="C:/webDrivers/chromedriver.exe")
         
        
        for name in names:
            driver.get(f"https://www.truepeoplesearch.com/details?name={name}&rid=0x0")
            # sleep(10)
            # searchBar = driver.find_element_by_xpath("//input[@class='input-n form-control typeahead-name form-control-lg border-right-0 rounded-right-0']")
            # searchBar.send_keys(name)
          

            # searchBar.send_keys(Keys.ENTER)
            # sleep(20)
           
            # btn = driver.find_element_by_xpath(
            #     "//a[@class='btn btn-success btn-lg detail-link shadow-form shadow-button']")
            # if btn:
            # btn.click()

        

            sleep(10)
            nums = []
            for phoneNum in driver.find_elements_by_xpath("//a[contains(@href, 'phoneno')]"):
                nums.append(phoneNum.text)


            yield{
                                    'Name': name,
                                    'PhoneNumbers' : nums
                                    
                        }
            sleep(15)

            # htmlMarkup = Selector(text=driver.page_source)
            # links = htmlMarkup.xpath("//div[@class='resultextrasurl']/a")
            # for link in links:
            #     yield {
            #         'url': link.xpath(".//@href").get()
            #     }

        driver.save_screenshot("afterafterSearch.png")
