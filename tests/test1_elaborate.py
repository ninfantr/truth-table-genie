#!/usr/intel/bin/python3.6.3a
import UsrIntel.R1
import os, sys
sys.path.append("../src/")

from val_ai import ttg
#generate output_file
ttg.elaborate("files/dataset.xlsx")
ttg.elaborate("files/dataset.xlsx", sheet_name="Sheet2", output_file="output/dataset_enum.xlsx", support_enum=True)