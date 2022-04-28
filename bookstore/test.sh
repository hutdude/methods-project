#!/bin/bash

for py_file in $(find ../bookstore -name *.py)
do
    python $py_file
done