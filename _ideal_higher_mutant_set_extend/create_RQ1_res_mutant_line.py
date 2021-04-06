import os
import shutil


file_res_mutant_line = ""

def _MutantLine(wait_fault_num, list_fault_line, list_mutant_line):
    if wait_fault_num == 0:
        str_mutant_line = ",".join(list_mutant_line)
        global file_res_mutant_line
        file_res_mutant_line = file_res_mutant_line + str_mutant_line + '\n'
        return

    for fault_line in list_fault_line:
        if fault_line in list_mutant_line:
            return
        list_mutant_line_copy = list_mutant_line.copy()
        list_mutant_line_copy.append(fault_line)
        _MutantLine(wait_fault_num-1, list_fault_line, list_mutant_line_copy)



def recordMutantLine(list_file_res_mutant_line, fault_num, list_fault_line):
    list_file_res_mutant_line.append([])
    _MutantLine(fault_num, list_fault_line, [])
    global file_res_mutant_line
    list_file_res_mutant_line[fault_num-1] = file_res_mutant_line
    file_res_mutant_line = ""

if __name__ == "__main__":

    # 1.read the file of "./output/Fault_Record.txt", record all of the fault lines.
    with open("./output/Fault_Record.txt", 'r') as f:
        str_Fault_Record = f.read()
    f.close()
    list_fault_line = []
    list_fault_line_temp = str_Fault_Record.split("Line ")[1:]
    for fault_line_temp in list_fault_line_temp:
        list_fault_line.append(fault_line_temp.split(": ")[0])

    # print(list_fault_line)


    # 2.generate the record of each set of mutant lines as "mutant_line.txt".
    list_file_res_mutant_line = []
    for fault_num in range(1, len(list_fault_line)+1):
        recordMutantLine(list_file_res_mutant_line, fault_num, list_fault_line)

    # for file_res_mutant_line in list_file_res_mutant_line:
    #     print(file_res_mutant_line)

    os.mkdir("./_RQ1_mutant_set")
    for dir_index in range(len(list_file_res_mutant_line)):
        os.mkdir("./_RQ1_mutant_set/mutant_set_" + str(dir_index+1))
        with open("./_RQ1_mutant_set/mutant_set_" + str(dir_index+1) + "/res_mutant_line.txt", 'w') as f:
            f.write(list_file_res_mutant_line[dir_index])
        f.close()
