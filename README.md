# val-ai

VAL_AI is a python package developed to employ the AI in the Digital Logical design and validation. 
The VAL_AI supports following modules:

1. **TTG - truth table genie** - operates on logic truth table which are represented in structural format (xlsx/xls/csv) and extracts insightful information from it.
 - Handles dont care condition in the truth table and resolve them. (Represented as 'X') 
 - Elaborate the truth table combination and identifies the duplicates & misses (duplicates - same logic values but overlapping output , misses - undefined logic values )
 - Trains AI/ML models on the valid combination
 - Provides user suggestion for the missing combination in truth table
 - Provide model explaniability in form of graphical representation and assist in the user decision

# Installation

* Recommended version: python 3.6.3a
* Supported in Linux/ Windows

## Windows 
1. Install python modules dependencies
```
python -m pip install -r requirements.txt
```

## Intel EC_Linux
```
No need to install. Run with python3.6.3a
```

# Example

To execute the tool

```
 python cmd_line/ttg_parser.py -i examples/sample.csv
```

To generate a template of csv. Use this command **python cmd_line/generate_template.py -n 10** 


# Getting Started

## Usage
```
$ python cmd_line/ttg_parser.py -h

usage: TTG_PARSER [-h] [-i INPUT] [-s SHEET] [-o OUTPUT]
                  [-model {decision_tree,neural_network,random_forest}]
                  [-elaborate] [-sort_x] [-sort_y]

Process logic truth table and extracts insightful information from it using
AI/ML

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input filepath (supports xlsx, xls, csv)
  -s SHEET, --sheet SHEET
                        input sheetname in case of xlsx/xls. Default: Sheet1
  -o OUTPUT, --output OUTPUT
                        output directory. Default: output
  -model {decision_tree,neural_network,random_forest}
                        select ML/DL model. Default: decision_tree . Available
                        Options: decision_tree,neural_network,random_forest
  -elaborate            Perform only elab to expand the dont care condition.
                        Default: False (analysis stage does elab explicitly)
  -sort_x               Sorted output along rows. Easy for comparsion.
                        Default: True
  -sort_y               Sorted output along columns Easy for comparsion.
                        Default: True

Let's get started
```
# Considerations

1. Input Files supports xlsx/csv/xls
2. cmd_line/ttg_parser.py can be ran at any place
3. The last column is considered as OUTPUT to predict based on other input columns
4. The cell must contains 1,0,X as valid input. Support for enum type will be provided in future
5. The tool suggests the decision based on the given valid combination which are not duplicates.
6. The output files are not sorted by default. Use need to provide -sort_x / -sort_y to do sorting
7. Default output files are stored in **output** folder and if folder exists, output_\* is created based on the available. Output folder path can be overridden by user in cmdline
8. Debug_ttg.log is generated in provided output folder which are used for debug purpose. Run the tool from write-disk permission folder.
9. In case of large number of column/ features, run -elaborate separately then provide the generated **_elab.csv**  to the tool analysis to save time
10. Decision tree model is selected as default model to predict, select -model to select other model. Note: support for other model are limited for time being
11. The val_ai is  also available as python module and need to be installed where as **ttg_parser.py** works as standalone . Note: use from **val_ai import ttg** to use as python library

## Output collaterals :
1. <input_file>_**elab.csv** - Elaborated view of the given truth table after resolving the dont care conditions
2. <input_file>_**elab_no_duplicates.csv** - Analysis view with valid combination in truth table
3. <input_file>_**duplicates.csv** - Analysis view containing overlapping logic or duplicate in truth table
4. <input_file>_**misses.csv** - Analysis view identifying the missing combination in the truth table
5. <input_file>_**predict_on_miss.csv** - Run prediction on the missing combination with trained model
6. <input_file>_**predict_all.csv** - Predicting all combination of input columns using the AI/ML model
7. debug_ttg.log - Debug prints from tool to root cause any script issue.

### Other
1. **decision_tree.jpg** - Graphical representation for decision tree if model is decision tree
2. **model_decision_tree**_<col_name>.pkl - saved model state
3. **report_decision_tree**_<col_name>.txt - Testing report information
4. For Random Forest/ Neural network, the graphical representation is not provided.

# FAQ
* **What command to use to open jpg image in linux?**
:  display *decision_tree.jpg*

* **What command to use to open excel in linux?**
: soffice *file_name*

* **How to see debug statement in the tool ?**
: debug_ttg.log is saved at execution folder. And [DONE] is displayed in case of successful execution

* **Tool is running for long time?**
: Elaborate consume more time while expanding large number of features in the truth table. Run -elaborate stage separate first then provide its output to the tool again to save time

* **Is there available template to test?**
: sample.csv is presented in examples/ folder. Use generate_template.py to generate a excel with n dimension. Command is **python cmd_line/generate_template.py -n 10**


# Known Bugs 
1. Decision_tree.jpg does not open in Windows.
2. Graphical Representation is not available for another model random_forest and neural network 
3. Support for enumeration based logic truth table is limited

# Support:
 * navin.infant.raj@intel.com
 * puneet.a.s.v@intel.com

