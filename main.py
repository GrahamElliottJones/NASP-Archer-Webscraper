import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input("enter a url: ")

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)
soup = BeautifulSoup(html, "html.parser")

output = os.linesep.join([s for s in soup.get_text().splitlines() if s])
output_list = output.splitlines()

final_list = []

for i in output_list:
    if (i == " "or i ==""):
        output_list.remove(i)
    else:
        final_list.append(i.lstrip().rstrip())

#removes junk data from the start of the website
for i in range(29):
    final_list.remove(final_list[0])

#removes two site links from the data.
final_list.remove(final_list[2])
final_list.remove(final_list[2])

#removes junk data from the end of the website
for i in range(18):
    temp = len(final_list)-1
    final_list.remove(final_list[temp])


name = final_list[0]
final_list.remove(name)
print(final_list)

#list order
#1. school [0]
#2. date of tournament [1]
#3. name of tournament [2]
#4. state of school [3]
#5. score [4]
#6. division ranking header (High school boys, etc...) [5]
#7. division ranking placement (11 out of 1125, etc...) [6]
#8. grade ranking (11th grade Boys Rank) [7]
#9. grade ranking placement (same idea as before) [8]
#10. Overall ranking (overall boys or overall girls) [9]
#11. overall ranking placement (same as before) [10]
#end of sequence

#mod 11?
