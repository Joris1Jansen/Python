numDays = int(input('How many days would you like to enter? '))
total = 0
tempList = []

for i in range(numDays):
    nextDay = int(input("Day " + str(i+1) +  "'s temp:"))
    tempList.append(nextDay)
    total += tempList[i]

avg = round(total/numDays)
print("Avg = " + str(avg))

above = 0
for i in tempList:
    if i > avg:
        above += 1
print("There are " + str(above) + " days hotter dan average")