#!/usr/intel/bin/python3.6.3a
import UsrIntel.R1
import os, sys
current_dir = os.path.dirname(__file__)
pkg_dir = os.path.join(current_dir,"..","src")
#print(f"importing {pkg_dir}")
sys.path.append(pkg_dir)


from val_ai import ttg

import argparse

parser = argparse.ArgumentParser(prog='TTG')
parser.add_argument('-template', help='Generate template of n dimension',type=int,default=5)
parser.add_argument('-o', '--output', help='output directory',default="output")

args = parser.parse_args()
#args.model = "decision_tree"


if args.template:
    col_names = [f"COL_{x}" for x in range(args.template)]
    ttg.generate_all_combination(col_names,output_file=f"{args.output}/template.xlsx",extra_cols=["OUT"])
    exit(0)

exit(0)

