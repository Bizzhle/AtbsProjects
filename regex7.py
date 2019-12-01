# Complex Regexes

import re

''' with VERBOSE you can spread the regular expression which are hard to 
read over multiple lines with comments 
'''
phoneRegex = re.compile(r'''(
    (\d{3}|\)                       # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)?                      # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
)''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL and re.VERBOSE

