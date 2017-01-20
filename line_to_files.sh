#!/bin/bash

i=1
folder="qa/queries"
while IFS= read -r line; do
   if [ ! -z "$line" ]; then
      touch $folder/query_$i.txt
      echo $line >> $folder/query_$i.txt
      let "i+=1"
   fi
done <$1
