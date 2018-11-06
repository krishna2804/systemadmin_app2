#!/bin/bash
top -u $1 -bn 1 | grep "^ " | awk '{printf("%-8s\n", $10)}' >memory.txt

