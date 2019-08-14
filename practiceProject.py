# practice project - Table printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def PrintTable(data):
    colWidths = [0] * len(data) # creates 3 lists based on the list length

    for i in range(len(data[0])): # finds a length of 4 items (aka rows)
        for j in range(len(data)): # finds a lenght of 3 items (aka colums)
            colWidths[j] = len(max(data[j], key=len)) # sets the column width to
            # the max length of an item in the list 
            a = data[j][i]
            print(a.rjust(colWidths[j]), end=" ")  # every time we print a column, we rjust it to the max width
           
        print('\n')

PrintTable(tableData)


