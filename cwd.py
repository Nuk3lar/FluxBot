import os, sys
if sys.platform == "linux":
    cwd = os.getenv('PWD')
elif sys.platform == "win32":
    cwd = os.getcwd()