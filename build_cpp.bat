@echo off

SETLOCAL

SET PYTHON_INCLUDE_DIRS="C:/Users/lkost/miniconda3/envs/django_env/include"
SET PYTHON_LIB_PATH="C:/Users/lkost/miniconda3/envs/django_env/libs/python38.lib"

SET Boost_INCLUDE_DIRS="C:/boost"                         
SET Boost_PYTHON36_LIBRARY="C:/boost/lib/libboost_python38-vc140-mt-x64-1_72.lib"          

SET GENERATOR_PLATFORM=x64

rmdir /s /q build
mkdir build
cd build
cmake -DCMAKE_GENERATOR_PLATFORM=%GENERATOR_PLATFORM% -DPYTHON_INCLUDE_DIRS=%PYTHON_INCLUDE_DIRS% -DPYTHON_LIBRARIES=%PYTHON_LIB_PATH% -DBoost_INCLUDE_DIRS=%Boost_INCLUDE_DIRS% -DBoost_PYTHON36_LIBRARY=%Boost_PYTHON36_LIBRARY% ../cpp/
cmake --build . --config Release
copy Release\divisors.dll ..\bin\divisors.pyd
cd ..
rmdir /s /q build

ENDLOCAL
