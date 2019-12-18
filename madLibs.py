#! python3
# madLibs.py reads in text files and lets the user add their own text

import re, os

# open file where text is stored
madLibs = open('C:\\Users\\Dusty\\Desktop\\AtbsProjects\\MADLIBS.txt', 'r')
# read file content
madLibsContent = madLibs.read()
madLibs.close()
print(madLibsContent)

# do a regex of words you want to search for 
regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

for i in regex.findall(madLibsContent):
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))
            inp_text = input('Enter the substitute for %s: ' %j)
            madLibsContent = reg.sub(inp_text, madLibsContent, 1)

print(madLibsContent)

# madLibs = open('C:\\Users\\Dusty\\Desktop\\AtbsProjects\\MADLIBSANS.txt', 'w')
madLibs = open('madlibs_ans', 'w')
madLibs.write(madLibsContent)
madLibs.close
