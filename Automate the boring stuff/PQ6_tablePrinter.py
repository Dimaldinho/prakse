tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidth = [0] * len(tableData)

    
    for row in range(len(tableData[0])):
        for column in range(len(tableData)):
            if len(tableData[column][row]) > colWidth[column]:
                colWidth[column] = len(tableData[column][row])
            
    print(colWidth)
    for row in range(len(tableData[0])):
        print()
        for column in range(len(tableData)):
            print(tableData[column][row].rjust(colWidth[column]) + ' ', end='')
  
            

printTable(tableData)