#!/bin/bash

# TODO: change node name/number, and corresponding parts of string.
# 4 becomes 6
sudo python run.py --node R4 --cmd "pgrep -f [z]ebra-R4 | xargs kill -9"
sudo python run.py --node R4 --cmd "pgrep -f [b]gpd-R4 | xargs kill -9"
