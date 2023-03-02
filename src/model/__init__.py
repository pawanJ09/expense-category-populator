import os
import sys
import inspect


curr_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(curr_dir)
# Setting src module on the system path
sys.path.insert(0, parent_dir)