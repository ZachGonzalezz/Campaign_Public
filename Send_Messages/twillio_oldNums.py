import csv
import re
from time import sleep

from twilio.rest import Client

client = Client('Hidden',
                                'Hidden')

filename = "C:/Users/zacha/Life360Adventure/Send_Messages/numbers.csv"
rows = []
names = []
numbers = []
#old the numbers of the people we sent already to avoid sending same person two person (double charging us and annyoing them)
alreadySentNumber = []

#more accurate detects numbers
phoneRegex = re.compile(r'''(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?))(\d{3}(\s|-?))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?''', re.VERBOSE)

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        rows.append(row)

    for row in rows:
        numbers.append(row[2])
        names.append(row[0])

index = 0

for number in numbers:
  
    
    for groups in phoneRegex.findall(number):
        if number not in alreadySentNumber:
            # phoneNum = '-'.join([groups[1],
            #                     groups[3], groups[5]])
            # if groups[8] != '':
            #     phoneNum += ' x' + groups[8]
            alreadySentNumber.append(number)
            try:
            
                numberAdjusted = number.replace(
                            '(', '').replace(')', '').replace('-', '').replace(' ', '')
                numberAdjusted = '+1' + numberAdjusted
                
                message = client.messages.create(
                                to=numberAdjusted,
                                from_='+14087062750',
                                body=f"Hi {names[index]}, I'm a recruiter with Homeworks Energy. We've tried to reach you about a position but haven't been able to connect. Please let me know if you're interested in speaking. Reply Yes/No"
                                )
                print(numberAdjusted + ' goes with '+ names[index] + ' and sent!')
                print(f"Hi {names[index]}, I'm a recruiter with Homeworks Energy. We've tried to reach you about a position but haven't been able to connect. Please let me know if you're interested in speaking. Reply Yes/No")
                sleep(3)
            except: 
                print('ERROR' + numberAdjusted + ' goes with '+ names[index] + ' and NOT SENT!!!')
        else:
            print(names[index] + 'is a duplicate already sent the message')
    index += 1
