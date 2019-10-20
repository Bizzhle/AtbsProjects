# Pattern Matching with regular expressions


import re
# Matching Zero or More with the Star

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman') 
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman') # This wont match because 'wo' is missing
mo3 == None
print(mo3)
# The group preceding the + must appear atleast once.
print()

# Matching Specific Repetitions with Curly Brackets

haRegex = re.compile(r'(Ha){3}')
mo4 = haRegex.search('HaHaHa')
print(mo4.group())
mo5 = haRegex.search('Ha')
mo5 == None
print(mo5)
print()

# greedy and nongreedy matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo6 = greedyHaRegex.search('HaHaHaHaHaHa')
print(mo6.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo7 = nongreedyHaRegex.search('HaHaHaHaHaHa')
print(mo7.group())
# the question mark makes the program choose the smaller number
print()

# The findall() method
# This returns the strings of every match in the searched string
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.findall('cell: 415-555-4242 wrk: 212-515-0000')
print(mo)
