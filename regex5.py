# Character Classes
# Character classes are nice for shortening regular expressions

import re

# The wildcard character (.) - matches any character except a new line

atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo1)
print()

# MAtching everything with Dot-Star(.*) - 
# The star means 'zero or more of the preceeding character.'
# This will match anything and everything

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo2 = nameRegex.search('First Name: Paul Last Name: Egbo')
print(mo2.group(1))
print(mo2.group(2))
print()

nongreedyRegex = re.compile(r'<.*?>')
mo3 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo3.group())

greedyRegex = re.compile(r'<.*>')
mo4 = greedyRegex.search('<To serve man> for dinner.>')
print(mo4.group())
print()

# Matching Newlines with the Dot Character
# This is done by passing re.DOTALL as the second argument to re.compile

noNewlineRegex = re.compile('.*')
mo5 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo5)

newlineRegex = re.compile(r'.*', re.DOTALL)
mo6 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo6)

