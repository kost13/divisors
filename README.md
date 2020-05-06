# divisors
A simple program displaying divisors of the given number. Implemented as a web app using Django, C++, JavaScript.

## build and run
C++ needs python to build *divisors* python module. Paths to python can be set in *build_cpp.sh* script. If no paths are provided, the default - found by cmake find_package() - are used.

To start a server run *run.sh* script. It will build the c++ library, start the server and open a web browser.

## tests
To test the application run *run_tests.sh*
