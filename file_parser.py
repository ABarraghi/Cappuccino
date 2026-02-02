# file_parser.py
# Given an input Espresso-minized truth table, construct the following structures:
# - List of all output signals
# - Dictionary of output signal to phase type and list of products
# - List of product terms and their binary values
# - List of all input signals

from wire_list import WireList

wire_list = WireList()

class FileParser:

    def __init__(self, pla_file_path):
        self.inputs = []
        self.outputs = []
        self.signal_idx = 0 #signifies starting index of non-state signals

        with open(pla_file_path, 'r') as file:
            for line in file:
                token_list = line.split()
                
                if token_list[0] == ".ilb":
                    self.inputs = token_list[1:]

                if token_list[0] == ".ob":
                    for signal in token_list[1:]:
                        signal_dict = {
                                "signal": signal,
                                "phase_type": 1,
                                "products": []
                        }
                        self.outputs.append(signal_dict)
                        if "next" in signal: #state signal detected
                            self.signal_idx += 1
                            wire_list.add_wire(name=signal)

                if token_list[0] == "#.phase":
                    counter = 0
                    for phase_bit in token_list[1]:
                        if phase_bit == "0":
                            self.outputs[counter]["phase_type"] = 0
                        counter += 1

                if token_list[0][0] in ("0","1","-"):
                    counter = 0
                    for output_bit in token_list[1]:
                        if output_bit == "1":
                            self.outputs[counter]["products"].append(token_list[0])
                        counter += 1

