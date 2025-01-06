import argparse
import pandas as pd
import numpy as np

from digital_designer_genie.ops.df_utils import *


###### SANITY CHECKS #################
def module_check():
    print("PASSED")
######################################

def elaborate(input_file,output_file,sheet_name="Sheet1",support_enum=False):
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    edit_df = df.copy()
    edit_df = fillX(edit_df,support_enum=support_enum)
    if output_file:
        edit_df.to_excel(output_file,sheet_name=sheet_name,index=False)
    return edit_df