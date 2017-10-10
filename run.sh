#!/bin/bash
find . -name "*.pyc" -exec rm -rf {} \;
clear
cd server
python -m server
