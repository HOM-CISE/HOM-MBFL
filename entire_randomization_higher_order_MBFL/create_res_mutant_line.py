import os
import shutil
import random
import numpy as np
import argparse


file_res_mutant_line = ""


def parserCommad():
    parser = argparse.ArgumentParser()

    parser.add_argument('--min_order_num', action='store',
                        dest='min_order_num',
                        type=int,
                        default=2,
                        help="The minimum order of a higher-order mutants.")

    parser.add_argument('--max_order_num', action='store',
                        dest='max_order_num',
                        type=int,
                        default=7,
                        help="The maximum order of a higher-order mutants.")

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results


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
    list_line = []
    list_line.extend(list_fault_line)
    list_line.extend(list_nonfault_line)

    with open("./_entire_randomization_higher_order_mutant_set/res_mutant_line.txt", 'w') as f:
        f.write("")
    f.close()

    with open("./output/res_record.txt", 'r') as f:
        list_res_record = f.readlines()
    f.close()
    # print(len(list_res_record))

    min_order_num = parserCommad().min_order_num
    max_order_num = parserCommad().max_order_num
    f = open("./_entire_randomization_higher_order_mutant_set/res_mutant_line.txt", 'a')
    for mutant_line_num in range(min_order_num, max_order_num+1):    # Select between the min_order_numnd-order to max_order_numth-order mutants.
        mutant_num_every_order = len(list_res_record) * 50    # len(list_res_record) * 1
        for mutant_index in range(mutant_num_every_order):
            if mutant_line_num > len(list_line):
                mutant_line_num = len(list_line)
            list_choice_line_index = []
            now_choice_index = 0
            while now_choice_index < mutant_line_num:
                choice_line_index = np.random.choice(list_line)
                if choice_line_index in list_choice_line_index:
                    continue
                list_choice_line_index.append(choice_line_index)
                now_choice_index += 1

            list_choice_line_index.sort()
            for item_index in range(len(list_choice_line_index)):
                list_choice_line_index[item_index] = str(list_choice_line_index[item_index])
            str_choice_line_index = ",".join(list_choice_line_index)
            f.write(str_choice_line_index)
            if mutant_index != mutant_num_every_order - 1 or mutant_line_num != max_order_num:
                f.write("\n")
    f.close()

