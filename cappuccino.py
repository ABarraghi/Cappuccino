#Top-level driver script for the Cappuccino circuit generator

from gates import Gate, Buffer, Inv, Xor, Xnor, Nand, Nor, Dff 

def main():
    #Define instances
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

    #Test the verilog generator methods
    print(gate_test.to_verilog_string())
    print(buffer_test.to_verilog_string())
    print(inv_test.to_verilog_string())
    print(xor_test.to_verilog_string())
    print(xnor_test.to_verilog_string())
    print(nand2_test.to_verilog_string())
    print(nand3_test.to_verilog_string())
    print(nand4_test.to_verilog_string())
    print(nor2_test.to_verilog_string())
    print(nor3_test.to_verilog_string())
    print(nor4_test.to_verilog_string())
    print(dff_test.to_verilog_string())

if __name__ == "__main__":
    main()

