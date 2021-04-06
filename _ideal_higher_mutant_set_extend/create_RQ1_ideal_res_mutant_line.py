
if __name__ == "__main__":

    with open("./output/Fault_Record.txt", 'r') as f:
        str_Fault_Record = f.read()
    f.close()
    list_fault_line = []
    list_fault_line_temp = str_Fault_Record.split("Line ")[1:]
    for fault_line_temp in list_fault_line_temp:
        list_fault_line.append(fault_line_temp.split(": ")[0])

    with open("./_RQ1_mutant_set/mutant_set_ideal/res_mutant_line.txt", 'w') as f:
        for fault_line in list_fault_line:
            f.write(fault_line)
            f.write('\n')
    f.close()
