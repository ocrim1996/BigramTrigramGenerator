cmake_minimum_required(VERSION 3.15)
project(ParallelCppBigramTrigramGenerator)

set(CMAKE_CXX_STANDARD 14)

add_executable(ParallelCppBigramTrigramGenerator main.cpp LinesExtractor.cpp LinesExtractor.h)