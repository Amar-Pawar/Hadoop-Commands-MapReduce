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

from operator import itemgetter 
import sys

# keep a map of the sum of gold for countries
total_count = {}

for line in sys.stdin:
    line = line.strip()
    country, count = line.split('\t',1)
    try:
        count = int(count)
        total_count[country] = total_count.get(country, 0) + count
    except ValueError:
        # ignore lines where the count is not a number
        pass

# sort the medal list in decending order
sort_by_total_gold = sorted(total_count.items(), key=itemgetter(1), reverse=True)

# output to STDOUT
for country, count_gold in sort_by_total_gold:
    print ('%s\t%s'% (country, count_gold))