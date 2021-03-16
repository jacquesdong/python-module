cmake_minimum_required(VERSION 3.10)

project(spam VERSION 1.0 LANGUAGES C)

find_package (Python COMPONENTS Development REQUIRED)

Python_add_library(spam MODULE src/spammodule.c)

