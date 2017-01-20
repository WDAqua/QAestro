#!/usr/bin/python

import sys, os


directory = 'qa/output'
outputf = 'qa/stats.txt'

lines = ['query,rw,encode,filter,decode']
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.txt'):
            rw = 0
            ofile = open(os.path.join(subdir, file),'r')
            for line in ofile:
                if line.startswith('q'):
                    rw += 1
                if line.startswith('[Done]'):
                    words = line.split()
            queryname = file.replace('output_query_', 'Q').replace('.txt', '')
            lines.append(queryname + ',' + str(rw) + ',' + str(words[1]) + ',' + str(words[2]) + ',' + str(words[3]))
            ofile.close()

with open(outputf, 'aw') as file:
    for line in lines:
        file.write(line + '\n')
    file.close()
