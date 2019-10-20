# Character Classes
# Character classes are nice for shortening regular expressions
import re

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Emilia likes to eat and also likes to cry'))
print()

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Emilia likes to eat and also likes to cry'))

# The caret(^) and dollar sign characters
# ^ at the start of a regex used to indicate that a match must occur at the begining of the searched text.
# $ is used at end of regex to indicate the string must end with this regex pattern
# You can use both together to indicate that the entire string must match the regex

beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
print(mo1)
mo2 = beginsWithHello.search('He said hello.') == None
print(mo2)
print()

endsWithNumber = re.compile(r'\d$')
mo3 = endsWithNumber.search('Your number is 432')
print(mo3)
mo4 = endsWithNumber.search('Your number is two.') == None
print(mo4)
print()

wholeStringIsNum = re.compile(r'^\d+$')
mo5 = wholeStringIsNum.search('13234567890') 
print(mo5)
mo6 = wholeStringIsNum.search('12345gfgjgj67890') 
print(mo6)
mo7 = wholeStringIsNum.search('12 34567890')
print(mo7)