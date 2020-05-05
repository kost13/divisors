#!/bin/bash

mkdir -p build && cd build
cmake ../cpp/
cmake --build .
cp *.so ../bin/
cd ..
#rm -rf build


