#!/usr/intel/bin/python3.6.3a
import UsrIntel.R1
import os, sys
sys.path.append("../src/")

import val_ai

from val_ai.ops.df_utils import *

generate_all_combination(["A","B","C"], {"A":["ON","OFF"], "B" : ["IDLE","ACTIVE"]},output_file="output/template.xlsx")