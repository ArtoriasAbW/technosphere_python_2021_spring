#!bin/bash

ab -n 50000 -c 10 http://localhost:8000/ > dynamic_test.txt
 
