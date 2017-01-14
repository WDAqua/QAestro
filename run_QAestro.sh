#!/bin/bash

# Generate mappings
./mcdsat_endec.py -a generate -i $1 -m qa/mappings.tmp

# Encode views and query files for execution with mcdsat
./mcdsat_endec.py -a encode -i $1 -m qa/mappings.tmp -o $1_mcdsat.tmp
./mcdsat_endec.py -a encode -i $2 -m qa/mappings.tmp -o $2_mcdsat.tmp

# Execute mcdsat
./mcdsat/mcdsat RW $1_mcdsat.tmp $2_mcdsat.tmp > $3_mcdsat.tmp

# Decode output from mcdsat
./mcdsat_endec.py -a decode -i $3_mcdsat.tmp -m qa/mappings.tmp -o $3
cat $3

# Remove all generated files
rm qa/mappings.tmp $1_mcdsat.tmp $2_mcdsat.tmp $3_mcdsat.tmp
