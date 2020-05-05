#!/bin/bash

open_site()(
    # wait for the server to start
    sleep 2

    #open default django url
    xdg-open http://127.0.0.1:8000/
)

# compile c++
if [ ! -f "./bin/divisors.so" ]; then
    ./build_cpp.sh
fi

open_site &

#run django server
python ./manage.py runserver




