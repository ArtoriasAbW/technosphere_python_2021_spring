#!bin/bash

ab -n 50000 -c 10 http://localhost/api > proxy_test.txt
 
