#find the rare characters in text2.txt
fIn = open('text2.txt', 'r')
charList = []
for line in fIn:
	for char in line:
		if(char not in charList):
			charList.extend(char)
			charList.append(1)
		else:
			index = charList.index(char)
			numChars = charList[index+1]
			numChars += 1
			charList[index+1] = numChars
numItems = len(charList);

fOut = open('testing.txt', 'w')

for i in range(0, numItems - 1, 2):
	print(charList[i], charList[i+1])
	s = (charList[i], charList[i+1])
	string = str(s)
	fOut.write(string)

fIn.close
fOut.close
