# Character Classes
# Character classes are nice for shortening regular expressions

import re

# Case-insensitive Matching
# pass re.I or re.IGNORECASE as second argument to re.compile() to make it case insensitive

robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop').group()
print(mo)
print()

# Substitutuing Strings with the sub() method

namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo1)
