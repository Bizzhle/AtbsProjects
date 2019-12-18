#! python3 

# MultiClipBoard mcb.pyw - saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipbord to keyword 
#        py.exe mcb.pyw <keyword> - loads keyword to clipboard.
#        py.exe mcb.pyw list - load all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')       # The user uses shelve to save a new piece of clipboard text

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        mcbShelf.pop(sys.argv[2])

elif len(sys.argv) == 2:
    # List Keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()


