# Character Classes
# Character classes are nice for shortening regular expressions

import re

#   Shorthand character class Represents
#   \d      Any numeric digit from 0 to 9.
#   \D      Any character that is not a numeric digit from 0 to 9
#   \w      Any letter, numeric digit, or the underscore characte(Think of this as matching “word” characters.)
#   \W      Any character that is not a letter, numeric digit, or thunderscore character.
#   \s      Any space, tab, or newline character. (Think of this amatching “space” characters.)
#   \S      Any character that is not a space, tab, or newline.


# Case-insensitive Matching
# pass re.I or re.IGNORECASE as second argument to re.compile() to make it case insensitive

xmasRegex = re.compile(r'\d+\s\w+')
no = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, p ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 patridge')
print(no)
print()

robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop').group()
print(mo)
print()

# Substitutuing Strings with the sub() method

namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo1)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo2 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Caroö that Agent Eve knew Agent Bob was a double Agent.')
print(mo2)




