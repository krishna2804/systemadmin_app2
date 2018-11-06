#!/bin/bash

awk -F: '($3 >=1000 && $3 <=1005) {printf "%s\n",$1}' /etc/passwd > users.txt
