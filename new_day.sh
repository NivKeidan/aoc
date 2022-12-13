#!/bin/bash

day_num=$1
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
mkdir -p $1
pushd $1
cp $SCRIPT_DIR/base1.py 1.py
touch inp1
popd
code -g $1/inp1 ./
