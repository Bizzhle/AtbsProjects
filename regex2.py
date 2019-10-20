# Pattern Matching with regular expressions
# groupin with parentheses

import re

# phonenumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phonenumRegex.search('My number is 455-555-9109')
phonenumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phonenumRegex.search('My number is (455) 555-9109.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups()) # retrieves all groups at once and returns a tuple
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
print()

# Matching Multiple Groups with the Pipe
# The character | is called  a pipe, used to match one of many expressions

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo2 = heroRegex.search('Tina Fey and Batman.')

print(mo1.group())
print(mo2.group())
print()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1)) # returns just the part of tthe matched text
print()

# Optional Matching with the Question Mark
batRegex1 = re.compile(r'Bat(wo|ant)?man')
mo4 = batRegex1.search('The Adventures of Batman')
mo5 = batRegex1.search('The Adventures of Batwoman')
mo6 = batRegex1.search('The Adventures of Batantman')
print(mo4.group())
print(mo5.group())
print(mo6.group())
print()
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo7 = phoneRegex.search('My number is 415-555-4242')
mo8 = phoneRegex.search('My number is 555-4242')
print(mo7.group())
print(mo8.group())
print()

# Matching Zero or More with the Star
batRegex2 = re.compile(r'Bat(wo)*man')
mo9 = batRegex2.search('The Adventures of Batwowowowowoman')
print(mo9.group())
m10 = batRegex2.search('The Adventures of Batwoman')
print(m10.group())
m11 = batRegex2.search('The Adventures of Batman')
print(m11.group())
# The group that precedes the star can occur any number of times,
# can be completely absent or repeated over again.

