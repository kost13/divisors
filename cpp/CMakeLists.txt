cmake_minimum_required(VERSION 3.0)

project(divisors)

find_package(Boost COMPONENTS python36 REQUIRED)

set(CMAKE_CXX_STANDARD 11)

add_library(${PROJECT_NAME} SHARED divisors.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC ${Boost_INCLUDE_DIRS})
target_include_directories(${PROJECT_NAME} PUBLIC "/home/lukasz/miniconda3/envs/django_env/include/python3.6m")
target_link_libraries(${PROJECT_NAME} PUBLIC ${Boost_PYTHON36_LIBRARY})
target_link_libraries(${PROJECT_NAME} PUBLIC "/home/lukasz/miniconda3/envs/django_env/lib/libpython3.6m.so")


