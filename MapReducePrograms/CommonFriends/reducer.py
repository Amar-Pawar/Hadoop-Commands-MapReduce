'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-30
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-30
@Title : Mapper code to find common friends
/**********************************************************************************
'''
#!/usr/bin/env python3
  
from operator import itemgetter
import sys  
import ast

friend_data = {}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    word, count = line.split('\t')
    if word not in friend_data:
        friend_data[word] = []
    count = ast.literal_eval(count)

    friend_data[word].append(count)

for key in friend_data:
    if len(friend_data[key]) > 1:
        inter = list(set(friend_data[key][0]) & set(friend_data[key][1]))
        print('%s\t%s' % (key ,inter))
        