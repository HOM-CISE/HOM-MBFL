if __name__ == "__main__":

    # read the file of "./output/Fault_Record.txt", record all of the fault lines and mutate operator
    with open("./output/Fault_Record.txt", 'r') as f:
        str_Fault_Record = f.read()
    f.close()

    list_fault_line = []
    list_fault_line_original = []
    list_fault_line_fault = []
    list_fault_line_temp = str_Fault_Record.split("Line ")[1:]

    # print(list_fault_line_temp)

    for fault_line_temp in list_fault_line_temp:
        list_fault_line.append(int(fault_line_temp.split(": ")[0]))
        list_fault_line_original.append(fault_line_temp.split("Original: ")[1].split(" Fault:")[0])
        list_fault_line_fault.append(fault_line_temp.split("Fault: ")[1].strip())

    mutant_set_num = len(list_fault_line)

    # print(list_fault_line)
    # print(list_fault_line_original)
    # print(list_fault_line_fault)

    with open("./_RQ1_mutant_set/mutant_set_ideal/res_record.txt", 'w') as f:
        str_res_record = ""
        for fault_line, fault_line_original, fault_line_fault in zip(list_fault_line, list_fault_line_original, list_fault_line_fault):
            str_res_record = str_res_record + "   |||   "
            str_res_record = str_res_record + "line: " + str(fault_line) + "   "
            str_res_record = str_res_record + "index: " + str(0) + "   "
            str_res_record = str_res_record + "original: " + fault_line_fault + "   "
            str_res_record = str_res_record + "mutated: " + fault_line_original

        # print(str_res_record)
        f.write(str_res_record)

