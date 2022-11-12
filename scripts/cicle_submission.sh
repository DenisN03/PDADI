#!/bin/bash

for i in {80..87..1}
do
  echo "Generate submission with $i confidence"
  sed -i -r "s/conf = .*/conf = $i/g" /app/src/submission.py
  python3 /app/src/submission.py
done
