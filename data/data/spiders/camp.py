from time import sleep
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
import re
from selenium.common.exceptions import NoSuchElementException
import csv


class CampSpider(scrapy.Spider):
    name = 'camp'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://ethicsfiling.sc.gov/public/candidates-public-officials',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):

        filename = "C:/Users/zacha/Life360Adventure/data/data/spiders/Politican - Sheet1.csv"

    # initializing the titles and rows list
        rows = []
        fullName = []
        firstNames = []
        lastNames = []

    # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            for row in rows:
                fullName.append(row[0])
                firstNames.append(row[1])
                lastNames.append(row[2])

        driver = response.meta['driver']

        index = 0
        for name in firstNames:
            # for each name loads a new page so we can click the searchbar
            driver.get(
                "https://ethicsfiling.sc.gov/public/candidates-public-officials")
            # this is the search bar which we will input a name into
            search_input = driver.find_element_by_xpath(
                "//input")
            # database is searched by last name only so we send it a last name
            search_input.send_keys(lastNames[index])
            # press enter a wait for results to load
            search_input.send_keys(Keys.ENTER)
            sleep(1)

            isStillGoing = True
            # we use a while loop because their is multiple pages
            while(isStillGoing):
                # trys to find the name if not error is caught so program does not crash
                try:
                    dataFound = driver.find_element_by_xpath(
                        f"//a[contains(text(), '{lastNames[index]}, {firstNames[index]}')]")
                    # clicks on persons links they waits for it to load
                    urlToPage = dataFound.get_attribute('href')
                    driver.get(urlToPage)
                    sleep(1)

                    try:

                        # once loads will bring user to campaign disclosure reports section
                        # click on specific office like district 54
                       
                        btnUrl = driver.find_element_by_xpath(
                            "//a[@routerlink='./campaign-disclosure-reports']").get_attribute('href')
                        
                        driver.get(btnUrl)

                        sleep(5)
                        offices = driver.find_elements_by_xpath(
                            "//a[@routerlink='./reports']")

                        for officeUrl in offices:
                            # loads all the reports
                            driver.get(officeUrl.get_attribute('href'))
                            sleep(2)

                            # these are the hyperlinks to all the reports
                            urlsToReports = []
                            isMoreOffice = True
                            # loop through every report until there is not next button
                            while(isMoreOffice):
                                # this is all the reports like 2008 2009
                                details = driver.find_elements_by_xpath(
                                    "//a[@routerlink = '../report-detail']")
                                # len(details)
                                # print(details)
                                # sleep(12)
                                for office in details:
                                    urlToOffice = office.get_attribute('href')
                                    urlsToReports.append(urlToOffice)

                                try:
                                    nextButton = driver.find_element_by_xpath(
                                        "//a[@title='Go to the next page']")
                                    nextButton.click()
                                except:
                                    isMoreOffice = False
                                    print("no clickiable next")
                           
                    
                          
                            for specific in urlsToReports:
                                
                                try: 
                                    driver.get(specific)
                                    sleep(1)
                                except:
                                    print("Crash while loadnext page")
                                    print(specific)
                                    sleep(10)
                                

                                # clicks on contribution button
                                contributionBtn = driver.find_element_by_xpath(
                                    "//li[@id='k-tabstrip-tab-1']")
                                driver.execute_script(
                                    "arguments[0].click();", contributionBtn)
                                sleep(1)

                                try:
                                    rows = driver.find_elements_by_xpath("//tr")

                                    rowIndex = 1
                                    for row in rows:
                                        try :
                                            if len(rows) > 0 and rowIndex < len(rows):
                                                print(driver.find_element_by_xpath(f"//tr[{rowIndex}]/td[2]").text)
                                                yield{
                                                    "Politican": fullName[index],
                                                    "Donor": driver.find_element_by_xpath(f"//tr[{rowIndex}]/td[2]").text,
                                                    "Amount": driver.find_element_by_xpath(f"//tr[{rowIndex}]/td[3]").text,
                                                    "DateOfDonation": driver.find_element_by_xpath(f"//tr[{rowIndex}]/td[1]").text
                                                }
                                        except:
                                        

                                            print(rowIndex)
                                            print(driver.find_element_by_xpath(f"//tr[{rowIndex}]/td[2]").text)
                                            print('Error saving')
                                            sleep(20)
                                            
                                    
                                        rowIndex += 1
                                except:
                                    print("No rows found")
                                
                    except:
                        print(lastNames[index] + ' No Disclosure Button')
                        isStillGoing = False

                    # isStillGoing = False
                  # this stops from program looking for more
                except NoSuchElementException:
                    # if no user found on current page tries to look for button and go to the next page
                    try:
                        nextButton = driver.find_element_by_xpath(
                            "//a[@title='Go to the next page']")
                        try:
                            nextButton.click()
                        except:
                            print("not clickable")
                            isStillGoing = False
                    except NoSuchElementException:
                        isStillGoing = False
                        print('hi')

            index += 1

        driver.save_screenshot("afterafterSearch.png")
