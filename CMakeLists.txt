cmake_minimum_required(VERSION 3.16)

project(dbc LANGUAGES C)

add_library(dbc STATIC src/r3.c src/tcs.c)
target_include_directories(dbc PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
