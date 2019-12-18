#! python3

# regexSearch.py - to search for user supplied regular expression

import re

# open all  files in a folder.
file = open('C:\\Users\\Dusty\\Desktop\\AtbsProjects\\capitalsquiz1.txt', 'r')
content = file.read()
file.close()


# user input
search_str = input('Enter the string you are searching for: \n')

#creater regexAu
regex = re.compile(r'.*%s.*' % search_str)

# if regex.search(content) is None:
#     print('No matches')
# else:
#    print(regex.findall(content))

for i in regex.findall(content):
    i = 0
    print('%s is found %s times' %(search_str,  (i + 1)))

