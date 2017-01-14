#!/bin/bash

# Batch QAestro for multiple queries
for f in $2
do
  echo "Running query $f..."
  sh run_QAestro.sh $1 $f $3
done
