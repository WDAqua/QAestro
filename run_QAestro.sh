#!/bin/bash

ts=$(date +%s%N)
# Generate mappings
./mcdsat_endec.py -a generate -i $1 -m mappings.tmp

# Encode views and query files for execution with mcdsat
./mcdsat_endec.py -a encode -i $1 -m mappings.tmp -o $1_mcdsat.tmp
./mcdsat_endec.py -a encode -i $2 -m mappings.tmp -o $2_mcdsat.tmp

# Execute mcdsat
./mcdsat/mcdsat RW $1_mcdsat.tmp $2_mcdsat.tmp > output_mcdsat.tmp

# Decode output from mcdsat
./mcdsat_endec.py -a decode -i output_mcdsat.tmp -m mappings.tmp -o $3
tt=$((($(date +%s%N) - $ts)/1000000))
echo $tt >> $3
cat $3

# Remove all generated files
rm mappings.tmp output_mcdsat.tmp $1_mcdsat.tmp $2_mcdsat.tmp
