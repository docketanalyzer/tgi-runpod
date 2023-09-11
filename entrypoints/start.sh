#!/bin/bash
nohup text-generation-launcher > tgi.out &
python handler.py

