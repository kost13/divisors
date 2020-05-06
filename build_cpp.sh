#!/bin/bash

#if empty default python is used
PYTHON_INCLUDE_PATH="/home/lukasz/miniconda3/envs/django_env/include/python3.6m"
PYTHON_LIB_PATH="/home/lukasz/miniconda3/envs/django_env/lib/libpython3.6m.so"

mkdir -p build && cd build
if [ -z "$PYTHON_INCLUDE_PATH" ] || [ -z "$PYTHON_LIB_PATH" ] ; then
    echo "a"
    cmake ../cpp/
else
    echo "b"
    cmake ../cpp/ -DPYTHON_INCLUDE_DIRS=${PYTHON_INCLUDE_PATH} -DPYTHON_LIBRARIES=${PYTHON_LIB_PATH}
fi

cmake --build .
cp libdivisors.so ../bin/divisors.so
cd ..
rm -rf build


