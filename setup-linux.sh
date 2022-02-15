#!/bin/bash

mkdir output
mkdir plans
sudo apt update && sudo apt install -y python3 python3-pip pandoc
pip3 install -r ./requirements.txt