#!/usr/intel/bin/python3.6.3a
import UsrIntel.R1
import os, sys, time
current_dir = os.path.dirname(__file__)
pkg_dir = os.path.join(current_dir,"..","src")
#print(f"importing {pkg_dir}")
sys.path.append(pkg_dir)

import warnings
warnings.filterwarnings('ignore')

from val_ai import ttg

import argparse

#redirecting logs to debug.log
error_occured = False
sys.stdout = open('debug_ttg.log', 'a')
sys.stderr = open('debug_ttg.log', 'a')

print("="*5 + f" EXECUTION RUN {time.strftime('%Y-%m-%d %H:%M:%S')} " + "="*5+ "\n")

available_models = ["decision_tree","neural_network","random_forest"]

parser = argparse.ArgumentParser(prog='TTG')
parser.add_argument('-i', '--input', help='input filepath')
parser.add_argument('-s', '--sheet', help='input sheetname',default="Sheet1")
parser.add_argument('-o', '--output', help='output directory',default="output")
parser.add_argument('-m', '--model', help='select ML/DL model. Options: '+ ",".join(available_models) , choices=available_models, default="decision_tree")
#stages
parser.add_argument('-elaborate', help='Perform only elab to expand the dont care condition',action='store_true',default=False)
parser.add_argument('-analysis', help='Perform complete analysis of Truth Table',action='store_true',default=True)
parser.add_argument('-sort_x', help='Sorted output xlsx, csv. Easy for comparsion',action='store_true',default=False)
parser.add_argument('-sort_y', help='Sorted output xlsx, csv. Easy for comparsion',action='store_true',default=False)
#parser.add_argument('-template', help='Generate template of n dimension',type=int,default=0)

args = parser.parse_args()

#args.model = "decision_tree"

if args.output == "output":
    output_dir = args.output
    i = 1
    while True:
        if os.path.exists(output_dir):
            #print(f"searching.......{i}")
            output_dir = f"output_{i}"
            i +=1
        else:
            break
    args.output = output_dir

args.sort = ( args.sort_x , args.sort_y )

try:
    # if args.template:
    #     col_names = [f"COL_{x}" for x in range(args.template)]
    #     ttg.generate_all_combination(col_names,output_file=f"{args.output}/template.xlsx",extra_cols=["OUT"])
    #     exit(0)

    if args.input is None:
        raise Exception(f"Please provide input xlsx path using -i or --input option.")

    if args.elaborate:
        ttg.elaborate(args.input,sheet_name=args.sheet,output_dir=args.output,sort=args.sort)

    if args.analysis:
        ttg.analysis_elab(args.input,sheet_name=args.sheet,output_dir=args.output,do_predict_misses=True,do_elab=True,model = args.model,sort=args.sort)

except Exception as e:
    print(traceback.format_exc())
    print(e)    
    error_occured = True

#Restoring the stdout, stderr
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

if error_occured:
    print("\n[ERROR] : Something went wrong. Please check debug.log")
    exit(15)
else:
    print(f"\n[DONE] : {args.output}/ is generated")
    exit(0)