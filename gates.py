# gates.py
# Define logic gate behavior in an Object-Oriented fashion

class Gate:
    def to_verilog_string(self):
        return "Base Gate class method reached"

class Buffer(Gate):
    def (self, in_wire, out_wire):
        self.in_wire = in_wire
        self.out_wire = out_wire

    def to_verilog_string(self):
        return f"assign {out_wire} = {in_wire}"

class Inv(Gate):
    def __init__(self, in_wire, out_wire):
        self.in_wire = in_wire
        self.out_wire = out_wire
        
    def to_verilog_string(self):
        return f"inv1$(.out({out_wire}), .in({in_wire}));\n"

class Xor(Gate):
    def __init__(self, in_wire_0, in_wire_1, out_wire):
        self.in_wire_0 = in_wire_0
        self.in_wire_1 = in_wire_1
        self.out_wire = out_wire
        
    def to_verilog_string(self):
        return f"xor2$(.out({out_wire}), .in0({in_wire_0}), .in1({in_wire_1}));\n"

class Xnor(Gate):
    def __init__(self, in_wire_0, in_wire_1, out_wire):
        self.in_wire_0 = in_wire_0
        self.in_wire_1 = in_wire_1
        self.out_wire = out_wire
        
    def to_verilog_string(self):
        return f"xnor2$(.out({out_wire}), .in0({in_wire_0}), .in1({in_wire_1}));\n"

#Assume that NAND and NOR gates have less than or equal to 4 inputs
class Nand(Gate):
    def __init__(self, out_wire, **in_wires):
        self.in_wires = in_wires
        self.out_wire = out_wire
        self.in_len = len(in_wires)
        
    def to_verilog_string(self):
        match(in_len):
            case 2:
                return f"nand2$(.out({out_wire}), .in0({in_wires[in_wire_0]}), .in1({in_wires[in_wire_1]}));\n"
            case 3:
                return f"nand3$(.out({out_wire}), .in0({in_wires[in_wire_0]}), .in1({in_wires[in_wire_1]}), .in2({in_wires[in_wire_2]}));\n"
            case 4:
                return f"nand4$(.out({out_wire}), .in0({in_wires[in_wire_0]}), .in1({in_wires[in_wire_1]}), .in2({in_wires[in_wire_2]}), .in3({in_wires[in_wire_3]}));\n" 
 
class Nor(Gate):
    def __init__(self, out_wire, **in_wires):
        self.in_wires = in_wires
        self.out_wire = out_wire
        self.in_len = len(in_wires)
        
    def to_verilog_string(self):
        match(in_len):
            case 2:
                return f"nor2$(.out({out_wire}), .in0({in_wires[in_wire_0]}), .in1({in_wires[in_wire_1]}));\n"
            case 3:
                return f"nor3$(.out({out_wire}), .in0({in_wires[in_wire_0]}), .in1({in_wires[in_wire_1]}), .in2({in_wires[in_wire_2]}));\n"
            case 4:
                return f"nor4$(.out({out_wire}), .in0({in_wires[in_wire_0]}), .in1({in_wires[in_wire_1]}), .in2({in_wires[in_wire_2]}), .in3({in_wires[in_wire_3]}));\n" 
 



    

