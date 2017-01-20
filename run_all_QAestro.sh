#!/bin/bash

# Batch QAestro for multiple queries
if [ ! -d "$3" ]; then
  mkdir $3
fi

for f in `ls $2`
do
  echo "Running query $f..."
  sh run_QAestro.sh $1 $2/$f $3/output_$f
done
