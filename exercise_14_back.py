from urllib.request import *


zip_url = 'http://www.uszip.com/zip/'
your_zip = input("Enter your zip code: ")
get_url = zip_url + str(your_zip)
conn = urlopen(get_url)

for line in conn.fp:
    if b'Population' in line:
        print(line)
    if b'Longitude' in line:
        print(line)
    if b'Latitude' in line:
        print(line)

conn.close()

#print("Your town's name is : ")
#print("Total population of this town is: ")



