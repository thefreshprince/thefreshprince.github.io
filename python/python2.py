#K->M    O->Q    E->G
#Pattern: 2 letter difference. Change each character in string by adding 2 to them
import sys

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for x in string:
	if(x >= "a" and x <= "x"):
		y = ord(x)
		y += 2
		x = chr(y)

	elif (x == "y"):
		x = "a"

	elif (x == "z"):
		x = "b"

	sys.stdout.write(x)
print ""
