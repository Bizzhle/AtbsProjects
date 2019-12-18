#! python3

# os.walk function - walks  through the directory tree, touching every file as you go.

import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\Dusty\\Desktop\\AtbsProjects'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER  OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')