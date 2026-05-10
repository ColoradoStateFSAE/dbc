cmake_minimum_required(VERSION 3.16)

project(rrcan LANGUAGES C)

file(GLOB_RECURSE RRCAN_SOURCES CONFIGURE_DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR}/src/*.c
)

add_library(rrcan STATIC ${RRCAN_SOURCES})

target_include_directories(rrcan PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)
