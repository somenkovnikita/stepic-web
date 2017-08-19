#!/bin/bash

target_directories=(
    'public/img' 
    'public/css' 
    'public/js' 
    'uploads' 
    'etc')

for directory in ${target_directories[@]} 
do
    mkdir -p $directory
done
