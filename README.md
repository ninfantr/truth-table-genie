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

# Usage

```
python cmd_line/ttg_parser.py 

usage: TTG [-h] [-i INPUT] [-s SHEET] [-o OUTPUT]
           [-model {decision_tree,neural_network,random_forest}] [-elaborate]
           [-analysis] [-sort_x] [-sort_y]

Process logic truth table and extracts insightful information from it using
AI/ML

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input filepath
  -s SHEET, --sheet SHEET
                        input sheetname. Default: Sheet1
  -o OUTPUT, --output OUTPUT
                        output directory. Default: output
  -model {decision_tree,neural_network,random_forest}
                        select ML/DL model. Default: decision_tree . Available
                        Options: decision_tree,neural_network,random_forest
  -elaborate            Perform only elab to expand the dont care condition
  -analysis             Perform complete analysis of Truth Table. Default:
                        True
  -sort_x               Sorted output along rows. Easy for comparsion
  -sort_y               Sorted output along columns Easy for comparsion

Let's get started
```

# Output collaterals :
1. <input_file>_**elab.csv** - Elaborated view of the given truth table after resolving the dont care conditions
2. <input_file>_**elab_no_duplicates.csv** - Analysis view with valid combination in truth table
3. <input_file>_**duplicates.csv** - Analysis view containing overlapping logic or duplicate in truth table
4. <input_file>_**misses.csv** - Analysis view identifying the missing combination in the truth table
5. <input_file>_**predict_on_miss.csv** - Run prediction on the missing combination with trained model
6. <input_file>_**predict_all.csv** - Predicting

## Other
1. **decision_tree.jpg** - Graphical representation for decision tree if model is decision tree
2. **model_decision_tree**_<col_name>.pkl - saved model state
3. **report_decision_tree**_<col_name>.txt - Testing report information
4. For Random Forest/ Neural network, the graphical representation is not provided.

# FAQ
1. How to open image in linux?
  ``` display decision_tree.jpg
  ```
2. How to open excel/ csv in linux?
  ``` soffice <file_name>
  ```

# Known Bugs 
1. Decision_tree.jpg does not open in Windows.
2. Graphical Representation is not available for another model random_forest and neural network 
3. Support for enumeration based logic truth table is limited

# Support:
Contact navin.infant.raj@intel.com for developing support


