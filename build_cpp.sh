#!/bin/bash

mkdir -p build && cd build
cmake ../cpp/
cmake --build .
cp libdivisors.so ../bin/divisors.so
cd ..
rm -rf build


