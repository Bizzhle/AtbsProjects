# Finding matching patterns or text with regular expressions.

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneNumRegex = re.compile(r'\d\d\d \d\d\d \d\d\d\d')
mo = phoneNumRegex.search('My number is 415 555 4242. wrk: 212-515-0000')
print('Phone number found: ' + mo.group())