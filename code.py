import csv

data = []

with open("dataset1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

headers = data[0]
#Selecting all rows starting from index number 1
planet_data = data[1:]

#Converting all the planet names into lower case
for i in planet_data:
    i[2] = i[2].lower()

#Sorting the data in alphabetical order
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("dataset2.csv","a+") as file:
    writer=csv.writer(file)
    writer.writerow(headers)
    writer.writerows(planet_data)

#Removing extra blank lines
with open("dataset2.csv") as input, open("dataset3.csv","w",newline="") as output:
    writer=csv.writer(output)
    for i in csv.reader(input):
        if any(field.strip() for field in i ):
            writer.writerow(i)