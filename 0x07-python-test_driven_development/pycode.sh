#!/bin/bash
shopt -s nullglob
files=( *.py)
if [ ${#files[@]} -eq 0 ]; then
echo "No .py files found"
else
for file in "${files[@]}"; do
pycodestyle "$file"
done
fi
