#!/usr/bin/env bash

set -e -x

python3 bin/get_submodules.py
python3 bin/make_favicons.py
python3 bin/get_schedules.py
python3 bin/get_setup.py
