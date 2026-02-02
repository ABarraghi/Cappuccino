# Cappuccino
cappuccino.py - A Python-based tool that converts Boolean-logic truth tables to structural Verilog. 

Arguments:

* "--out_file", "-o" -> the name of the output verilog file
* "--module_name", "-m" -> the name of the output verilog module
* "--in_table", "-i" -> the name of the input truth table file

Ensure that cappuccino.py has execute privilege (chmod +x cappuccino.py), and that the espresso.linux executable is in the same directory as the python scripts. 

The tool detects whether a given input file is combinational or a state machine based on the output wire naming, where next state wires begin with the term "next". 

The tool assumes at most 4 active signals to a given product, and at most 4 total products for each output signal.  
