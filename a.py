import whois
import sys
import json

print ("whois program \n")

url_domain=sys.argv[1] #input url 
url_data=whois.whois(str(url_domain)) #conver url

f=open('whois.txt','w') #store result in file
f.write(str(url_data)) 
f.close()

print("complete program \n")
