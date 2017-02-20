#!/bin/bash

virtualenv ./virtualenv
source ./virtualenv/bin/activate

pip install setuptools
pip install -r ./requirements.python.txt