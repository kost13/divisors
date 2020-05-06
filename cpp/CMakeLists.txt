cmake_minimum_required(VERSION 3.0)

project(divisors)

find_package(Boost COMPONENTS python36 REQUIRED)

if(NOT DEFINED PYTHON_LIBRARIES OR NOT DEFINED PYTHON_INCLUDE_DIRS)
    message(WARNING "No python paths defined, searching for default")
    find_package(PythonLibs REQUIRED)
endif()

set(CMAKE_CXX_STANDARD 11)

add_library(${PROJECT_NAME} SHARED divisors.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} PUBLIC ${Boost_PYTHON36_LIBRARY} ${PYTHON_LIBRARIES})


