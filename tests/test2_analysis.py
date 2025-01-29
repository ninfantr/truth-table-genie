import os,sys
import platform

print(f"PLATFORM : {platform.platform()}")
if platform.platform() == "Linux":
    print("running in EC_LINUX")
    import UsrIntel.R1
elif platform.platform() == "Windows":
    print("running in WINDOWS")
sys.path.append("../src/")

from val_ai import ttg

import os, sys
sys.path.append("../src/")

from val_ai import ttg

ttg.analysis_elab("files/dataset.xlsx")