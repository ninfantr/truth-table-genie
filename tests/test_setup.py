import os,sys
import platform
import traceback

sys.stdout = open('debug.log', 'a')
sys.stderr = open('debug.log', 'a')


print(f"PLATFORM : {platform.platform()}")

if platform.platform() == "Linux":
    print("running in EC_LINUX")
    import UsrIntel.R1
elif platform.platform() == "Windows":
    print("running in WINDOWS")

sys.path.append("../src/")

print(traceback.format_exc())
raise Exception("CHECKING")

from val_ai import *

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

print("MODULED LOADED")
