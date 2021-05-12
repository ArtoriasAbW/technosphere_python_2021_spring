#!/bin/bash

wrk -c400 -t8 --latency --timeout 5s http://localhost:8000/ > dynamic_test.txt
