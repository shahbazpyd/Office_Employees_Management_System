#!/bin/bash

# Build the project
echo "Building the project..."
pip install -r requirements.txt

python3.9 office_emp_proj/manage.py collectstatic --noinput
echo "Build finished."
