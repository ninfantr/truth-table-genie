import argparse
import pandas as pd
import numpy as np

def fillX(df,nFeatures=-1,support_enum=False):
    edit_df = df.copy()
    if nFeatures == -1: 
        # always consider last column as output
        nFeatures = len(edit_df.columns) -1
    
    for idx_col in range(nFeatures):
        col_name = edit_df.columns[idx_col]
        print(f"debug-fillX - Running col {idx_col} - {col_name}")
        if "X" not in edit_df[col_name].values:
            continue
        transform_idx = []
        enum_states = list(edit_df[col_name].unique())
        if "X" in enum_states:
            enum_states.remove("X")
        print(f"debug-fillX - VALUES {enum_states}")
        for idx_row ,row in edit_df.iterrows():
            val = edit_df.iat[idx_row,idx_col]
            print(f"debug-fillX -   running row {idx_row} - {val}")
            if isinstance(val,str) and val.strip().upper() == "X":
                print(f"debug-fillX -     transform row {idx_row} , {col_name} = {val}   ")
                if support_enum:
                    for state in enum_states:
                        new_row_x = row.copy()
                        new_row_x[idx_col] = state
                        edit_df = edit_df.append(new_row_x,ignore_index=True)
                else:
                    #normal binary operation
                    new_row_0 = row.copy()
                    new_row_1 = row.copy()
                    new_row_0[idx_col] = 0
                    new_row_1[idx_col] = 1
                    edit_df = edit_df.append(new_row_0,ignore_index=True)
                    edit_df = edit_df.append(new_row_1,ignore_index=True)
                #drop these rows
                transform_idx.append(idx_row)
        
        print(f"debug-fillX -    dropping row {transform_idx}")
        #removing the transofrmed idx
        for drop_idx_row in transform_idx:
            # if idx_col == 2:
            #     print("debug-fillX  ---------->", drop_idx_row)
            #     print(edit_df)
            #     print("debug-fillX  ----------*")
            edit_df.drop(index=drop_idx_row,inplace = True)
        #rebasing after removing all
        edit_df.reset_index(drop=True,inplace=True)
            
    return edit_df

