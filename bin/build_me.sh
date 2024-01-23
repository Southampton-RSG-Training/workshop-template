echo 'Getting sub modules'
python3 bin/get_submodules.py

echo 'Making schedules'
python3 bin/get_schedules.py
echo 'Making setup'
python3 bin/get_setup.py
