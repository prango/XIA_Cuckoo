#! /bin/sh

COUNT=1000000

echo "Running the test for $COUNT elements"
./cuckoo_hash 0 $COUNT
