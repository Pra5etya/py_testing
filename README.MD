# Setup

```
py -m venv "environment_name"
pip install pytest Flask
```

## Folder Structure

o) Make dir tests/ and add file .py for test \
o) Make dir for test codes \
o) Run code bellow: 

```
# run this code
py -m pytest test/ -v

# or add file path for pytest
> conftest.py
```
o) conftest.py: 

```
import os
import sys

# determine root project
project_root = os.path.dirname(os.path.abspath(__file__))

# dir path
codes_path = os.path.join(project_root, 'dir names')

# add to sys.path
sys.path.append(codes_path)
```

o) Run code normally: 

```
pytest tests/ -v
```

## Use on Web Development (Flask)

o) run flask \
o) run pytest 