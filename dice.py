# Name: Tyler High
# Period 2
# Dice Rolling Simulator

import random

tS = 1

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

rolls = int(input("How many times do you want to roll?: "))
randNum = 0

while tS <= rolls:
	rR = random.randint(1,6)
	print("Roll number: " + str(tS))
	print("Result: " + str(rR))
	tS += 1

	if rR == 1:
		ones += 1

	elif rR == 2:
		twos += 1

	elif rR == 3:
		threes += 1

	elif rR == 4:
		fours += 1

	elif rR == 5:
		fives += 1

	elif rR == 6:
		sixes += 1

print("Total amount of rolls: " + str(rolls))

print("1s: " + str(ones))
print("2s: " + str(twos))
print("3s: " + str(threes))
print("4s: " + str(fours))
print("5s: " + str(fives))
print("6s: " + str(sixes))

percent1 = (ones / rolls) * 100
print("% of 1s: " + str(percent1) + "%")
percent2 = (twos / rolls) * 100
print("% of 2s: " + str(percent2) + "%")
percent3 = (threes / rolls) * 100
print("% of 3s: " + str(percent3) + "%")
percent4 = (fours / rolls) * 100
print("% of 4s: " + str(percent4) + "%")
percent5 = (fives / rolls) * 100
print("% of 5s: " + str(percent5) + "%")
percent6 = (sixes / rolls) * 100
print("% of 6s: " + str(percent6) + "%")