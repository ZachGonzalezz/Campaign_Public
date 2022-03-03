import csv
filename = "C:/Users/zacha/Life360Adventure/out.csv"


# initializing the titles and rows list
rows = []
names = []
newNames = []


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
        newNames.append(row[0])

index = 0

for name in names:
    newNames.remove(name)
    index += 1
    if index == 30:
        break

wtr = csv.writer(open ('test.csv', 'w'), delimiter=',', lineterminator='\n')
for x in newNames : 
    wtr.writerow ([x])