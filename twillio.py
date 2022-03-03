import csv
from time import sleep

from twilio.rest import Client

# this is the file to electricans I made
filename = "C:/Users/zacha/Life360Adventure/Copy of Certified Electrician List - CA - Master.csv"

rows = []
names = []
oldNumbers = []
# there are the zipcodes within 50 miles of sanjose
zipcodes = [91205,  91204, 90041, 90065, 90027, 90068, 90046, 90028, 90038, 90020,  90210, 90019, 90031, 90032, 91201, 91202,
91505, 91506, 91601, 91607, 91208, 91504, 91605, 91607, 91352, 91214,  91011, 91020, 90068, 90027, 90039, 91345,91311, 91342, 91040,91042
,91326, 91344, 91331, 91387, 91042, 91350, 91354, 93563, 91330, 91343, 91311, 91335, 91411, 91401,91364, 91367, 91356, 91436, 91602]
oldZipcodes = [94027, 94025, 94301, 94303, 94305, 94306, 94305, 94043, 9041, 9040, 94024, 94022, 95014, 94087, 95014, 95129, 95041,
            94087, 94085, 94085, 94089, 95002, 95134, 95131, 95110, 95126, 95128, 95008, 95130, 95125, 95136, 95122, 95116, 95133, 95131,
            92079, 92009, 92078, 92069, 92067, 92024, 92011, 92008, 92010, 92084, 92026, 92025, 92029, 92081, 92083, 92091, 92127, 92027]

# reading csv file
client = Client('Hidden',
                                'Hidden')
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        rows.append(row)

    # get total number of rows
    for row in rows:
        # ensure row is not header and if so sees if zip code matches requirements
        if row[2] != 'ZIP_CODE' and int(row[2]) in oldZipcodes:
            phoneNumberString = row[4]
            # takes all the phone numbers and seperates them into an array
            phoneNums = phoneNumberString.split(',')
            # goes throguh every phone number for that person
            for number in phoneNums:
                oldNumbers.append(number)

    
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    index = 0
    # get total number of rows
    for row in rows:
        # ensure row is not header and if so sees if zip code matches requirements
        if row[2] != 'ZIP_CODE' and int(row[2]) in zipcodes:
            index += 1
            nameOfPerson = row[0].split(' ')
            # this is the name of user First Last
            # name = nameOfPerson[1] + ' ' + nameOfPerson[0]
            name = nameOfPerson[1]
            phoneNumberString = row[4]
            # takes all the phone numbers and seperates them into an array
            phoneNums = phoneNumberString.split(',')
            # goes throguh every phone number for that person
            for number in phoneNums:
                if number not in oldNumbers:
                     #this is done incase two people have same number that number is not spammed
                    oldNumbers.append(number)
                    # this remvoes the comma at the end of the name so it looks more real
                    name = name.replace(',', '').lower()
                    # this is the message that will be sent including there name
                    sendText = f"Hello {name} I'm a recruiter with SunPower Solar. We are currently looking for Certified Journeyman Electricians to join our team! We are offering TOP dollar for this role including a $5K sign on bonus. Would you be interested? Reply Yes or No and a recruiter will contact you shortly."
                    # gets rid of formating from number (702) 553-7534
                    number = number.replace(
                        '(', '').replace(')', '').replace('-', '')
                    number = '+1' + number
                    
                    if(len(number) == 12):
                        try: 
                            print(index)
                            print(number)
                            print(name)
                            message = client.messages.create(
                            to=number,
                            from_='+14087062750',
                            body=f"Hello {name.capitalize()} I'm a recruiter with SunPower Solar. We are currently looking for Certified Journeyman Electricians to join our team! We are offering TOP dollar for this role including a $5K sign on bonus. Would you be interested? Reply Yes or No and a recruiter will contact you shortly."
                            )
                            sleep(5)
                           
                            
                        except:
                            print('error')
                            print(number)
                            print(f"Hello {name.capitalize()} I'm a recruiter with SunPower Solar. We are currently looking for Certified Journeyman Electricians to join our team! We are offering TOP dollar for this role including a $5K sign on bonus. Would you be interested? Reply Yes or No and a recruiter will contact you shortly.")
                            print(index)
    print(len())
    
    # starts istances (sid, token)

    # print(message.sid)
