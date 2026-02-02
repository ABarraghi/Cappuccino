#Top-level driver script for the Cappuccino circuit generator

from gates import Gate, Buffer, Inv, Xor, Xnor, Nand, Nor, Dff 
from wire_list import WireList
from file_parser import FileParser

def main():
    #Define gate instances
    gate_test = Gate()
    buffer_test = Buffer(in_wire="in", out_wire="out")
    inv_test = Inv(in_wire="in", out_wire="out")
    xor_test = Xor(in_wire_0="in0", in_wire_1="in1", out_wire="out")
    xnor_test = Xnor(in_wire_0="in0", in_wire_1="in1", out_wire="out")
    nand2_test = Nand(in_wire_0="in0", in_wire_1="in1", out_wire="out")
    nand3_test = Nand(in_wire_0="in0", in_wire_1="in1", in_wire_2="in2", out_wire="out")
    nand4_test = Nand(in_wire_0="in0", in_wire_1="in1", in_wire_2="in2", in_wire_3="in3", out_wire="out")
    nor2_test = Nor(in_wire_0="in0", in_wire_1="in1", out_wire="out")
    nor3_test = Nor(in_wire_0="in0", in_wire_1="in1", in_wire_2="in2", out_wire="out")
    nor4_test = Nor(in_wire_0="in0", in_wire_1="in1", in_wire_2="in2", in_wire_3="in3", out_wire="out")
    dff_test = Dff(in_wire="in",out_wire="out");
    
    #Define and populate wire list, test peek function, access static wires array
    wire_list = WireList()
    wire_list.add_wire(name="S0")
    wire_list.add_wire(name="nextS0")
    wire_list.add_wire()
    print(wire_list.peek())
    print(wire_list.wires)
    wire_list_2 = WireList()
    print(wire_list_2.wires)


    #Test the verilog generator methods
    print(gate_test)
    print(buffer_test)
    print(inv_test)
    print(xor_test)
    print(xnor_test)
    print(nand2_test)
    print(nand3_test)
    print(nand4_test)
    print(nor2_test)
    print(nor3_test)
    print(nor4_test)
    print(dff_test)
    print(wire_list)
    print(wire_list_2)

    #Test the File Parser
    file_parser = FileParser(pla_file_path="esp_comb_out.pla")
    print(file_parser.inputs)
    print(file_parser.outputs)
    print(wire_list)
    file_parser = FileParser(pla_file_path="esp_statemachine.pla")
    print(file_parser.inputs)
    print(file_parser.outputs)
    print(wire_list)

if __name__ == "__main__":
    main()

