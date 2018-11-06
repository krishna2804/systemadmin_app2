#!/bin/bash

top -bn 1 -o %MEM | head -n 12 | tail -n 5 | awk '{printf("%-8s,%-2s\n",$1,$4)}' > pid.csv
