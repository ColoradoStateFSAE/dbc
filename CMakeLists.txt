cmake_minimum_required(VERSION 3.16)

project(dbc LANGUAGES C)

add_library(
    dbc STATIC
    src/haltech/haltech.c
    src/tcs/tcs.c
    src/swc/swc.c
    src/display/display.c
)

target_include_directories(dbc PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
