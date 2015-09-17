#!/usr/bin/env python2
 
import string
 
file_open = open('text3.txt', 'r')
file_data = file_open.read()
data = list(file_data)
 
characters = []
 
for i in range(len(data)):
    if data[i].isupper():
    	if (data[i-1].islower() and data[i+1].isupper()
        	and data[i+2].isupper() and data[i+3].islower()
        	and data[i+4].isupper() and data[i+5].isupper()
        	and data[i+6].isupper() and data[i+7].islower()):
 
        	characters.append(data[i+3])
 
print "".join(characters)
