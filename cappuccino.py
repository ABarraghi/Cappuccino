#Top-level driver script for the Cappuccino circuit generator

from gates import Gate, Buffer, Inv, Xor, Xnor, Nand, Nor, Dff 
from wire_list import WireList
from file_parser import FileParser
from gate_tree import GateTree, GateNode

import argparse
import os

parser = argparse.ArgumentParser(description="The Cappuccino structural verilog generator.")
parser.add_argument("--out_file", "-o")
parser.add_argument("--module_name", "-m")
parser.add_argument("--in_table", "-i")

args = parser.parse_args()

def main():

    wire_list = WireList()

    os.system(f"./espresso.linux -Dso_both {args.in_table} > esp_out.pla")

    file_parser = FileParser(pla_file_path="esp_out.pla")

    module_sig = f"module {args.module_name}("
    in_str = "input"
    out_str = "output"
    
    signal_idx = file_parser.signal_idx

    while signal_idx < len(file_parser.inputs):
        in_str += f" {file_parser.inputs[signal_idx]},"
        signal_idx += 1

    signal_idx = file_parser.signal_idx

    while signal_idx < len(file_parser.outputs):
        out_str += f" {file_parser.outputs[signal_idx]['signal']}"
        if signal_idx < (len(file_parser.outputs)-1):
            out_str += ","
        else:
            out_str += ");\n\n"

        signal_idx += 1

    if file_parser.signal_idx > 0:
        in_str += " clk, set, res,"
    in_str += "\n"

    module_sig = module_sig + in_str + out_str
        
    tree_list = []
    for term in file_parser.outputs:
        gate_tree = GateTree(phase_type=term["phase_type"], products=term["products"], input_wires=file_parser.inputs, out_wire=term["signal"])
        tree_list.append(gate_tree)
    
    with open(args.out_file, "w", encoding="utf-8") as f:
        f.write(module_sig)
        f.write(str(wire_list))
        for tree in tree_list:
            f.write(str(tree))
        
        f.write("\n")

        state_idx = 0
        while state_idx < file_parser.signal_idx:
            in_signal = file_parser.inputs[state_idx]
            out_signal = file_parser.outputs[state_idx]['signal']
            cur_dff = Dff(in_wire=out_signal,out_wire=in_signal);
            f.write(str(cur_dff))
            state_idx += 1

        f.write("\n")

        f.write("endmodule")


if __name__ == "__main__":
    main()

