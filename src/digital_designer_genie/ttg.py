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
    #populate dont care variables
    edit_df = fillX(edit_df,support_enum=support_enum)
    if output_file:
        edit_df.to_excel(output_file,sheet_name=sheet_name,index=False)
    return edit_df

def analysis_elab(input_file,sheet_name,output_file,subset=None,predict_miss=False,support_enum=False):
    elab_df = pd.read_excel(input_file, sheet_name=sheet_name)
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    elab_df.to_excel(writer,sheet_name="elab",index=False)

    #df sort
    df = elab_df.copy()
    if subset is None:
        #consider only last column as output
        features = list(elab_df.columns)[:-1]
    else:
        features = subset
    
    print(features)
    quit

    #assign logic_val
    if support_enum:
        #TODO
        def find_logic_val(row) : int(''.join(row.values.astype(str)),2)
    else:
        def find_logic_val(row) : int(''.join(row.values.astype(str)),2)
    
    df['_logic_index'] = df[features].apply(lambda row: find_logic_val(row) , axis=1)
    #df['combined'] = df[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
    df = df.sort_values(by=['_logic_index'])

    print("analysis_elab - finding DUPLICATES")
    #DUPLICATES
    #df['_logic_dup'] = df.duplicated(subset=features, keep=False )
    #df['_logic_dup'] = df.duplicated(keep=False)
    df = df.drop_duplicates() # drop duplicate with same targets
    df['_logic_dup'] = df.duplicated(subset=features, keep=False ) # identify duplicates with different targets
    
    # df[features].apply(lambda x : print(x))
    #print(df.head(10))
    
    elab_no_dup_df =df.copy()
    df["_logic_dup"].fillna(0,inplace=True)
    #elab_no_dup_df = elab_no_dup_df.fillna(0)
    elab_no_dup_df = df[df['_logic_dup']!=1]
    print(elab_no_dup_df)
    elab_no_dup_df = elab_no_dup_df.drop(['_logic_dup','_logic_index'],axis=1)     
    elab_no_dup_df.to_excel(writer,sheet_name="elab_no_duplicates",index=False)

    #MISSES
    df["_logic_miss"] = 0
    for i in range(2**len(features)):
        if i not in df['_logic_index'].values:
            new_row = {"_logic_miss": True, '_logic_index': i}
            lf = len(features)
            for feature,val in zip(features,format(i,f'0{lf}b')):
                new_row[feature] = val
            print("analysis_elab - found MISSES", i, new_row)
            df = df.append(new_row, ignore_index=True)
    df = df.sort_values(by=['_logic_index'])
    print(df.head(10))

    #dup
    df["_logic_miss"].fillna(0,inplace=True)
    df["_logic_dup"].fillna(0,inplace=True)

    dup_df =df.copy()
    #dup_df = dup_df.fillna(0)
    dup_df = df[df['_logic_dup']==1]
    print(dup_df.head(10))
    dup_df = dup_df.drop(['_logic_dup','_logic_index',"_logic_miss"],axis=1)     
    dup_df.to_excel(writer,sheet_name="duplicates",index=False)

    miss_df =df.copy()
    #miss_df = miss_df.fillna(0)
    miss_df = df[df['_logic_miss']==1]
    print(miss_df.head(10))
    miss_df = miss_df.drop(['_logic_dup','_logic_index',"_logic_miss"],axis=1)     
    miss_df.to_excel(writer,sheet_name="miss",index=False)

    if predict_miss:
        #TODO train and predict
        pass
    writer.save()
    print(f"{output_file} written succesfully")
