fIN = open('text3.txt', 'r')
for line in fIN:
	lineLength = len(line)
	for i in range(0, lineLength-9):
		substring = line[i:i+9]
		if(substring[0] >= 'a' and substring[4] >= 'a' and substring[8] >= 'a' and substring[1] <= 'Z' and substring[2] <= 'Z' and substring[3] <= 'Z' and substring[5] <= 'Z' and substring[6] <= 'Z' and substring[7] <= 'Z'):
			print(substring[4], end='')
