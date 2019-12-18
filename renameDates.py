#! python3
# Rename files with American date format

import os, shutil, re

# create a regex that matches files with the american date format
datePattern = re.compile(r"""^(.*?) # match all text before the date
    ((0|1)?\d)                      # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # match all the text after the date
    """, re.VERBOSE)

# Loop over the files in the directory.
for amerFilename in os.listdir('C:\\Users\\Dusty\\Desktop'):
    mo = datePattern.search(amerFilename)

    # Skip files without date.
    if mo == None:
        print('No file with american style names')
        continue 
    
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # form the european style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # get full, absolute paths.
    absWorkingDir = os.path.abspath('C:\\Users\\Dusty\\Desktop\\pythonbooks')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename)   # uncomment after testing


