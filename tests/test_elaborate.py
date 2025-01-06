import UsrIntel.R1
import os, sys
sys.path.append("../src/")
from digital_designer_genie import ttg
ttg.elaborate("files/dataset.xlsx", sheet_name="Sheet1", output_file="out/elaborated_1.xlsx")
ttg.elaborate("files/dataset.xlsx", sheet_name="Sheet2", output_file="out/elaborated_2.xlsx",support_enum=True)