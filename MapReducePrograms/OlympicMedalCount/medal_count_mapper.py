'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-27
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-27
@Title : Reducer code for counting gold medal for each country from given dataset
/**********************************************************************************
'''
#!/usr/bin/env python3
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys
  
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    columns = line.split(',')
    
    if len(columns) == 12:
        try:
            count_gold = int(columns[8])
            print ('%s\t%s' % (columns[2], count_gold))
        except ValueError:
            pass
