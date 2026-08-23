# 02. sys.path, PYTHONPATH and PATH
# Run: python 02_sys_path_and_pythonpath.py
# Also try: PYTHONPATH=/tmp python 02_sys_path_and_pythonpath.py



import os
import sys



# PYTHONPATH — extra directories the INTERPRETER searches for imports
print("PYTHONPATH =", os.environ.get("PYTHONPATH", "<unset>"))



# sys.path is the effective search path; entry 0 is the script's directory
for i, entry in enumerate(sys.path[:5]):
    print(i, entry or "<cwd>")



# PATH — directories the SHELL searches for executables
print("PATH entries:", len(os.environ.get("PATH", "").split(os.pathsep)))



# adding a directory at runtime affects imports immediately (per process)
sys.path.insert(0, "/path/to/code")
print(sys.path[0])
sys.path.pop(0)



# or persistently in the shell: export PYTHONPATH="/Users/my_user/code"



# where a module actually came from
import json

print(json.__name__, json.__file__)
print(sys.modules["json"] is json)



# an import is cached in sys.modules — re-importing does not re-execute
import json as json_again

print(json_again is json)
print("total modules loaded:", len(sys.modules))



# importlib.reload forces re-execution (mostly a REPL/dev tool)
import importlib
import importlib.util

print(importlib.reload(json) is json)



# find a module without importing it
spec = importlib.util.find_spec("json")
print(spec.name, spec.origin.endswith("json/__init__.py"))



# Practice
# Q1. Run this file with PYTHONPATH=/tmp and find /tmp in sys.path.
# Q2. Why is sys.path[0] different for `python file.py` and `python -m module`?
# Q3. What happens if you name a local file json.py and import json?
