#gate_tree.py
# IDEALLY - Based on a given product/sum, represent it as a priority queue of gates
# Ordered by delay

from gates import Gate, Nand, Nor, Buffer, Inv  
from wire_list import WireList

wire_list = WireList()

def flip_polarity(polarity):
    if polarity == "0":
        polarity = "1"
    elif polarity == "1":
        polarity == "0"
    elif polarity == 0:
        polarity = 1
    elif polarity == 1:
        polarity = 0

    return polarity


class GateNode:
    def __init__(self, phase_type, out_wire):
        self.phase_type = phase_type
        self.out_wire = out_wire
        self.num_inputs = 0
        
        self.gate = Nand(out_wire=self.out_wire) 
        if self.phase_type == 0:
            self.gate = Nor(out_wire=self.out_wire)

    def __str__(self):
        return str(self.gate)

    def add_input(self, in_wire):
        wire_key = f"in_wire_{self.num_inputs}"
        self.gate.in_wires[wire_key] = in_wire
        self.num_inputs += 1

class GateTree:
    def __init__(self, phase_type, products, input_wires, out_wire):
        self.gate_stack = []
        self.phase_type = phase_type
        self.products = products

        #if single multi-term product driving an output, flip phase and inputs before double negation
        sans_dont_cares = self.products[0].replace("-","")
        if len(self.products) == 1 and len(sans_dont_cares) > 1:
            self.phase_type = flip_polarity(self.phase_type)
            inv_term = ""

            for term in self.products[0]:
                inv_term += flip_polarity(term)

            self.products[0] = inv_term

        # first pass: compute logic for each product
        prod_idx = 0
        first_prod_out = []
        for product in self.products:
            term_idx = 0
            node_in_wires = []
            for term in product:
                if term == "1":
                    term = input_wires[term_idx]
                    self.gate_stack.append(Buffer(in_wire=input_wires[term_idx], out_wire=input_wires[term_idx]))
                    node_in_wires.append(term)
                elif term == "0":
                    wire_list.add_wire()
                    term = wire_list.peek()
                    self.gate_stack.append(Inv(in_wire=input_wires[term_idx], out_wire=term))
                    node_in_wires.append(term)
                term_idx += 1

            
            if len(node_in_wires) == 1: #if single input drives an output, connect wire directly
                top_gate = self.gate_stack[-1]
                if isinstance(top_gate, Inv):
                    wire_list.pop_wire()
                top_gate.out_wire=out_wire
                self.gate_stack[-1] = top_gate

            elif len(node_in_wires) > 1:
                prod_out = out_wire
                if len(self.products) > 1: #if single product drives output, connect node out directly to final output
                    wire_list.add_wire()
                    prod_out = wire_list.peek()
                
                prod_node = GateNode(phase_type=self.phase_type, out_wire=prod_out)
                
                for wire in node_in_wires:
                    prod_node.add_input(in_wire=wire)


                self.gate_stack.append(prod_node)
                first_prod_out.append(out_wire)


        #second pass, compute second level product logic - if more than one product exists
        if len(first_prod_out) > 1:
            out_prod_node = GateNode(phase_type=self.phase_type, out_wire=out_wire)
            for prod_wire in first_prod_out:
                out_prod_node.add_input(prod_wire)
            self.gate_stack.append(out_prod_node)

    def __str__(self):
        stack_str = ""
        for gate in self.gate_stack:
            stack_str += str(gate)
        return stack_str

    

