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

from val_ai.ops.df_utils import *

generate_all_combination(["A","B","C"], {"A":["ON","OFF"], "B" : ["IDLE","ACTIVE"]},output_file="output/template.xlsx")