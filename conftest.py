import os
import sys

# determine root project
project_root = os.path.dirname(os.path.abspath(__file__))

# dir path
codes_path = os.path.join(project_root, 'codes')

# add to sys.path
sys.path.append(codes_path)
