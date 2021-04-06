import os
import shutil


file_res_mutant_line = ""

def _MutantLine(wait_fault_num, list_nonfault_line, list_fault_line, list_mutant_line):
    if wait_fault_num == 0:
        str_mutant_line = ",".join(list_mutant_line)
        global file_res_mutant_line
        file_res_mutant_line = file_res_mutant_line + str_mutant_line + '\n'
        return

    if wait_fault_num == 2:
        for fault_line in list_fault_line:
            if str(fault_line) in list_mutant_line:
                return
            list_mutant_line_copy = list_mutant_line.copy()
            list_mutant_line_copy.append(str(fault_line))
            _MutantLine(wait_fault_num-1, list_nonfault_line, list_fault_line, list_mutant_line_copy)
    else:
        for non_fault_line in list_nonfault_line:
            if str(non_fault_line) in list_mutant_line:
                return
            list_mutant_line_copy = list_mutant_line.copy()
            list_mutant_line_copy.append(str(non_fault_line))
            _MutantLine(wait_fault_num - 1, list_nonfault_line, list_fault_line, list_mutant_line_copy)


def recordMutantLine(list_file_res_mutant_line, fault_num, list_fault_line, list_nonfault_line):
    list_file_res_mutant_line.append([])
    _MutantLine(fault_num, list_nonfault_line, list_fault_line, [])
    global file_res_mutant_line
    list_file_res_mutant_line[0] = file_res_mutant_line
    file_res_mutant_line = ""

if __name__ == "__main__":

    # 1.read the file of "./output/Fault_Record.txt", record all of the fault lines,
    # and record all of the non-fault lines index.
    with open("./output/Fault_Record.txt", 'r') as f:
        str_Fault_Record = f.read()
    f.close()
    list_fault_line = []
    list_fault_line_temp = str_Fault_Record.split("Line ")[1:]
    for fault_line_temp in list_fault_line_temp:
        list_fault_line.append(int(fault_line_temp.split(": ")[0]))
    # print(list_fault_line)

    with open("./output/suspicious_first_order.txt", 'r') as f:
        str_suspicious = f.read().split("Sus_Ochiai:")[0]
    f.close()
    list_nonfault_line = []
    list_nonfault_line_temp = str_suspicious.split("(")[1:]
    for nonfault_line_temp in list_nonfault_line_temp:
        line_index = int(nonfault_line_temp.split(",")[0])
        if line_index not in list_fault_line and line_index not in list_nonfault_line:
            list_nonfault_line.append(line_index)
    # print(list_nonfault_line)


    # 2.generate the record of mutant lines as "mutant_line.txt".
    list_file_res_mutant_line = []
    fault_num = 2
    recordMutantLine(list_file_res_mutant_line, fault_num, list_fault_line, list_nonfault_line)

    # for file_res_mutant_line in list_file_res_mutant_line:
    #     print(file_res_mutant_line)

    with open("./_between_worst_ideal_mutant_set/res_mutant_line.txt", 'w') as f:
        f.write(list_file_res_mutant_line[0])
    f.close()
