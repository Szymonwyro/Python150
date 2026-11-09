#!/usr/bin/env bash
# Usage: ./run.sh 01-arrays-hashing/001_two_sum.cpp
set -e
mkdir -p build
out="build/$(basename "${1%.cpp}")"
g++ -std=c++20 -O2 -Wall -Wextra -fsanitize=address,undefined -g "$1" -o "$out"
"./$out"
