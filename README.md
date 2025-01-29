# val-ai

VAL_AI is a python package developed to employ the AI in the design and validation. 
The VAL_AI has support following modules:

1. **TTG - truth table genie** - operates on logic truth table represented in xlsx format and extracts insightful information from it.

- It handles dont care condition in the truth table. Represented as 'X' in the excel. 
- It can elaborate the truth table combination and identifies the duplicates & misses (duplicates - same logic values but overlapping output , misses - undefined logic values )
- Trains AI/ML models on the valid combination
- Provides user suggestion for the missing combination in truth table
- Generates the truth table template for specified dimension



# Usage

Recommended version: python 3.6.3a

Supported in Linux

```
python parser/ttg_parser.py -i <excel_file>


optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input filepath
  -s SHEET, --sheet SHEET
                        input sheetname
  -o OUTPUT, --output OUTPUT
                        output directory
  -m {decision_tree,neural_network,random_forest}, --model {decision_tree,neural_network,random_forest}
                        select ML/DL model. Options:
                        decision_tree,neural_network,random_forest
  -elaborate            Perform only elab to expand the dont care condition
  -analysis             Perform complete analysis of Truth Table
  -sort                 Sorted output xlsx, csv. Easy for comparsion
  -template TEMPLATE    Generate template of n dimension

```

Output files :

1. dataset_elab.csv - Elaborated view of the given truth table after resolving the dont care conditions
1. dataset_analysis.xlsx - Extracted Information after analyzing truth table and identifies the misses & duplicates in the design. Contains sheets elab_no_duplicates, duplicates, misses.
1. decision_tree_<timestamp>.jpg
1. model_decision_tree_<col_name>.pkl
1. report_decision_tree_<col_name>.txt
1. dataset_predict_all.csv
1. dataset_predict_on_miss.csv


