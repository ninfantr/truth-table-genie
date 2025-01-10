import argparse
import pandas as pd
import numpy as np

import itertools

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

def generate_all_combination(Features, dict_valid_values=None,output_file=None,extra_cols=[]):
    if dict_valid_values is None:
        dict_valid_values = {}
        for  f in Features:
            dict_valid_values[f] = [0,1]
    
    #enable_populate default values
    for feature in Features:
        if feature not in dict_valid_values.keys():
            dict_valid_values[feature] = [0,1]


    option_space = []
    for featurs, valid_values in dict_valid_values.items():
        option_space.append(valid_values)
    
    lst = list(itertools.product(*option_space))

    df = pd.DataFrame.from_records(lst, columns = Features)
    if extra_cols:
        for col in extra_cols:
            df[col] = ""
    
    if output_file:
        df.to_excel(output_file,index=False)
    return df

# for test_name,flag_scheme in test_flag_scheme.items():
#     # Step 1: generate option space
#     option_space = []
#     for key, options in flag_scheme.items():
#         possible_flag_options = product([key],options) # returns a cartesian product
#         possible_flag_options = [f"{k}:{v}" for k,v in possible_flag_options ]      
#         #print(list(possible_flag_options))
#         option_space.append(possible_flag_options)

#     #Step 2: generate all possible scenario
#     idx = 0
#     scenarios = []
#     for idx,event in enumerate(product(*option_space)):
#         # print(i)
#         # print(check_if_valid_scenario(event))
#         if check_if_valid_scenario(event):
#             print(event)
#             scenarios.append(event)
#         else:
#             # print(event)
#             pass
#             # #EARLY KILL
#             # if idx == 20:
#             #     break
#         # print("----------------------")
#     cross_scenarios.extend(scenarios)
