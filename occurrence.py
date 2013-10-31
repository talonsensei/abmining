#!/usr/bin/python
__author__ = 'Csaba Kiss'
__email__ = 'csakis[at]lanl[dot]gov'
import sys

"""This file counts the occurrences of CDR3s in a dataset. It needs the binned CDR3 file and puts out the occurrence file
that contains the number of occurrences of CDR3s."""

if len(sys.argv) < 2:
  bin_in = raw_input('Please input the binned CDR3 file name: ')
else:
  bin_in = sys.argv[1]
file_in = open(bin_in, 'rU')  # get the file output by cdr3_binning
file_out = bin_in + '.occurences' #set the output file name
count_dict = {} # the dictionary contains the count pairs
line_count = 0
for line in file_in.readlines():
  value_list = line.split(',') #split the count values and the unique sequence
  cdr3_count = int(value_list[1])
  if cdr3_count in count_dict:
count_dict[cdr3_count] += 1
else:
count_dict[cdr3_count] = 1

line_count += 1
file_in.close()
f_out = open(file_out, 'w')
for cdr3_count, occurrence in sorted(count_dict.items()):
  f_out.write('%i, %i\n' % (cdr3_count, occurrence))
f_out.close()

