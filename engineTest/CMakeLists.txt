cmake_minimum_required(VERSION 3.31)
project(engineTest)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)

set(CMAKE_FOLDER "googletest")

FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG        v1.16.0
)

FetchContent_MakeAvailable(googletest)

set(CMAKE_FOLDER "")

enable_testing()

add_subdirectory("${CMAKE_CURRENT_SOURCE_DIR}/../engine" "${CMAKE_CURRENT_SOURCE_DIR}/../engine/build")

file(GLOB_RECURSE SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.hpp" "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")
add_executable(${PROJECT_NAME} ${SOURCES})

target_link_libraries(${PROJECT_NAME} PRIVATE gtest gtest_main engine)

include(GoogleTest)
gtest_discover_tests(${PROJECT_NAME})
