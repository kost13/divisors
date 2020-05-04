cmake_minimum_required(VERSION 3.0)

project(divisors)

add_library(${PROJECT_NAME} SHARED divisors.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC ${Boost_INCLUDE_DIRS})
target_include_directories(${PROJECT_NAME} PUBLIC "/home/lukasz/miniconda3/include/python3.7m")


