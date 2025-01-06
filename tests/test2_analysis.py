import UsrIntel.R1

import os, sys
sys.path.append("../src/")

from digital_designer_genie import ttg

ttg.analysis_elab("out/elaborated_1.xlsx",sheet_name="Sheet1",output_file="out/analysis_elab_1.xlsx")