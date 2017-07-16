import whois
import sys
import json

print ("whois program \n")

url_text=open('a.txt','r')
 
while True:
	line=url_text.readline()
	
	if not line:
		break
	
	line=line.strip("\n")
	print line
	
	url_data=whois.whois(str(line))

	print ("result: ",url_data)

f=open('whois.txt','w') #store result in file
f.write(str(url_data)) 
f.close()

print("complete program \n")
