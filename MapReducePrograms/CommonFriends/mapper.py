'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-30
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-30
@Title : Mapper code to find common friends
/**********************************************************************************
'''#!/usr/bin/env python3
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys
  
# reading entire line from STDIN (standard input)
friend_key = []
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(":")

    # a = b c d f
    # a map with every friend  ab ac ad af = b c d f
    # [a , [b c d f]]
    final_friend_list = []
    
    for i in words:
        friend_list = i.split()
        final_friend_list.append(friend_list) # [[a], [b,c,d,f]]
        
    for i in final_friend_list[1]:
        for j in final_friend_list[0]:
            if [j,i] in friend_key:
                final_text = j+i
            elif [i,j] in friend_key:
                final_text = i+j
            else:
                friend_key.append([j,i])  #ab
                final_text = j+i
            
            #print(final_text," ", final_friend_list[1])
            print('%s\t%s' % (final_text, final_friend_list[1]))
            