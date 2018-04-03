import os, sys
#Determines the system type
if sys.platform == "linux":
    cwd = os.getenv('PWD')
elif sys.platform == "win32":
    cwd = os.getcwd()