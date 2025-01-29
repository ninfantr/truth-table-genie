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

#generate output_file
ttg.elaborate("files/dataset.xlsx")
ttg.elaborate("files/dataset.xlsx", sheet_name="Sheet2", output_file="output/dataset_enum.xlsx", support_enum=True)