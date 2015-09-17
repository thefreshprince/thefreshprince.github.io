#!/usr/bin/env python2
import urllib
import re
 
ending = "27709"
i = 0
 
while i == 0:
    pagesource = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + ending)
    text = pagesource.read()
    number = re.findall(r'\d+', text)
    ending = "".join(number)
    if ending == "":
    	print text
    	i = 1
    	print ending
