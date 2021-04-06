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

    list_file_res_mutant_line = []
    list_line = []
    list_line.extend(list_fault_line)
    list_line.extend(list_nonfault_line)


    # 2.generate the record of mutant lines as "mutant_line.txt".

    with open("./_line_balancing_randomization_higher_order_mutant_set/res_mutant_line.txt", 'w') as f:
        f.write("")
    f.close()

    table_random_line_index = []
    list_random_line_index = []

    # init list_random_line_index
    list_random_line_index = list_line
    mutant_line_num = len(list_random_line_index)
    for i in range(mutant_line_num):
        line_index = list_random_line_index[i]
        table_random_line_index.append([i, line_index])

    np.random.seed(random.randint(0, 999999))
    initial_random_rate = 1.0 / mutant_line_num
    list_random_rate = [initial_random_rate for i in range(mutant_line_num)]
    p = np.array(list_random_rate)

    with open("./output/res_record.txt", 'r') as f:
        list_res_record = f.readlines()
    f.close()
    # print(len(list_res_record))

    min_order_num = parserCommad().min_order_num
    max_order_num = parserCommad().max_order_num
    f = open("./_line_balancing_randomization_higher_order_mutant_set/res_mutant_line.txt", 'a')
    mutant_program_num_every_order = len(list_res_record)
    for mutant_num in range(min_order_num, max_order_num+1):     # Select between the min_order_numnd-order to max_order_numth-order mutants.
        for i in range(mutant_program_num_every_order):
            if mutant_num > len(list_random_rate):
                mutant_num = len(list_random_rate)

            list_choice_line_index = []  # list of choice line index.
            now_choice_index = 0  # number of current selections.

            p = np.array(list_random_rate)

            # select mutant_num index of mutant lines.
            while now_choice_index < mutant_num:
                choice_line_index = np.random.choice(list_random_line_index, p=p.ravel())
                if choice_line_index in list_choice_line_index:
                    continue
                list_choice_line_index.append(choice_line_index)
                now_choice_index += 1

            list_choice_line_index.sort()
            # print(list_choice_line_index, '\n')
            for item_index in range(len(list_choice_line_index)):
                list_choice_line_index[item_index] = str(list_choice_line_index[item_index])
            f.write(",".join(list_choice_line_index))
            if i != mutant_program_num_every_order - 1 or mutant_num != max_order_num:
                f.write("\n")

            if len(list_choice_line_index) < len(list_random_line_index):
                for line_index in list_choice_line_index:
                    for table_item in table_random_line_index:
                        if table_item[1] == int(line_index):
                            list_random_rate[table_item[0]] /= 2
                            break
                allocated_rate = 1.0
                for line_random_rate in list_random_rate:
                    allocated_rate = allocated_rate - line_random_rate
                allocated_rate_every_not_choice_line = allocated_rate / (len(list_random_line_index)-len(list_choice_line_index))
                for line_random_rate_index in range(len(list_random_line_index)):
                    if list_random_line_index[line_random_rate_index] not in list_choice_line_index:
                        list_random_rate[line_random_rate_index] = list_random_rate[line_random_rate_index] + allocated_rate_every_not_choice_line

            # control precision
            sum_p = sum(list_random_rate)
            # print(sum_p)
            for index in range(len(list_random_rate)):
                list_random_rate[index] /= sum_p
    f.close()

