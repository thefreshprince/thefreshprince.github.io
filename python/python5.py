import urllib
import urllib2
import re

##NOT FINISHED##

URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
newNum = "12345"
check = 0
#check to see if website still has a number, if so change url
while(check < 410):

	response = urllib2.urlopen(URL+newNum)

	#read the sentence on the website
	html = response.read()
	print "-------------------------------------------"
	print html
	print "-------------------------------------------"

	#get the current url
	oldURL = response.geturl()
	#print response.code
	#print oldURL

	newNum = re.findall("")

	oldNum = oldURL[-5:]
	#take off the old number and replace with new number
	newURL = oldURL.replace(oldNum, newNum)
	#print newURL

	#use the new url and repeat the process

	check += 1

response.close()
