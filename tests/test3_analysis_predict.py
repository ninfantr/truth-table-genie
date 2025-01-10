#!/usr/intel/bin/python3.6.3a
import UsrIntel.R1

import os, sys
sys.path.append("../src/")

from val_ai import ttg

ttg.analysis_elab("files/dataset.xlsx", do_predict_misses=True)