#!/bin/bash

wrk -c400 -t8 --latency --timeout 5s http://localhost/ > static_test.txt
