cmake_minimum_required(VERSION 3.16)

project(dbc LANGUAGES C)

add_library(dbc STATIC src/haltech.c src/tcs.c src/display.c)
target_include_directories(dbc PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
