import os
import shutil
import random
import numpy as np
import math
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


if __name__ == "__main__":

    with open("./output/suspicious_first_order.txt", 'r') as f:
        str_suspicious = f.read().split("Sus_Ochiai:")[0]
    f.close()
    list_source_line = []
    list_source_line_txt = str_suspicious.split("(")[1:]
    for source_line_txt in list_source_line_txt:
        source_line = int(source_line_txt.split(",")[0])
        source_suspicious = float(source_line_txt.split(",")[1].split(")")[0])
        if source_suspicious < 0:
            continue
        list_source_line.append([source_line, source_suspicious, -1, -1])

    now_rank = 1
    for source_line_index in range(len(list_source_line)):
        if source_line_index == 0:
            list_source_line[source_line_index][2] = now_rank
            now_rank += 1
        elif list_source_line[source_line_index][1] == list_source_line[source_line_index-1][1]:
            list_source_line[source_line_index][2] = list_source_line[source_line_index-1][2]
            now_rank += 1
        else:
            list_source_line[source_line_index][2] = now_rank
            now_rank += 1

    for source_line_index in range(len(list_source_line)):
        list_source_line[source_line_index][3] = now_rank - list_source_line[source_line_index][2]

    # for source_line in list_source_line:
    #     print(source_line)

    # 2.generate the record of mutant lines as "mutant_line.txt".
    with open("./_MBFL_randomization_higher_order_mutant_set/res_mutant_line.txt", 'w') as f:
        f.write("")
    f.close()

    with open("./output/res_record.txt", 'r') as f:
        list_res_record = f.readlines()
    f.close()
    # print(len(list_res_record))

    min_order_num = parserCommad().min_order_num
    max_order_num = parserCommad().max_order_num
    f = open("./_MBFL_randomization_higher_order_mutant_set/res_mutant_line.txt", 'a')
    for mutant_line_num in range(min_order_num, max_order_num+1):    # Select between the min_order_numnd-order to max_order_numth-order mutants.
        list_choice_line_index = []  # list of choice line index.
        now_choice_index = 0  # number of current selections.
        mutant_num_every_order = len(list_res_record) * 50  # len(list_res_record) * 1
        mutation_source_num = mutant_num_every_order * mutant_line_num
        list_mutation_source_num = []
        sum_mutation_source_num = 0
        for source_line in list_source_line:
            list_mutation_source_num.append([source_line[0], source_line[3] * mutant_line_num, 0.0])
            sum_mutation_source_num += (source_line[3] * mutant_line_num)
        multiple = math.ceil(mutation_source_num / sum_mutation_source_num)
        sum_mutation_source_num = 0
        for mutation_source_num_index in range(len(list_mutation_source_num)):
            list_mutation_source_num[mutation_source_num_index][1] *= multiple
            sum_mutation_source_num += list_mutation_source_num[mutation_source_num_index][1]

        for i in range(mutant_num_every_order):
            list_randomization_rate = []
            list_randomization_source_line_index = []
            # ==========Exclude situations where candidate statements are insufficient========================
            for mutation_source_num_index in range(len(list_mutation_source_num)):
                if list_mutation_source_num[mutation_source_num_index][1] == 0:
                    list_mutation_source_num[mutation_source_num_index][1] += 1
                    sum_mutation_source_num += 1
            # =================================================================================================
            for mutation_source_num_index in range(len(list_mutation_source_num)):
                list_mutation_source_num[mutation_source_num_index][2] = list_mutation_source_num[mutation_source_num_index][1] / sum_mutation_source_num
                list_randomization_rate.append(list_mutation_source_num[mutation_source_num_index][2])
                list_randomization_source_line_index.append(list_mutation_source_num[mutation_source_num_index][0])

            np.random.seed(random.randint(0, 999999))
            p = np.array(list_randomization_rate)

            if mutant_line_num > len(list_randomization_rate):
                mutant_line_num = len(list_randomization_rate)

            list_choice_line_index = []
            now_choice_index = 0
            while now_choice_index < mutant_line_num:
                choice_line_index = np.random.choice(list_randomization_source_line_index, p=p.ravel())
                if choice_line_index in list_choice_line_index:
                    continue
                list_choice_line_index.append(int(choice_line_index))
                for mutation_source_num_index in range(len(list_mutation_source_num)):
                    if int(choice_line_index) == int(list_mutation_source_num[mutation_source_num_index][0]):
                        list_mutation_source_num[mutation_source_num_index][1] -= 1
                        sum_mutation_source_num -= 1
                        break
                now_choice_index += 1
            list_choice_line_index.sort()
            for choice_line_index in range(len(list_choice_line_index)):
                list_choice_line_index[choice_line_index] = str(list_choice_line_index[choice_line_index])
            f.write(",".join(list_choice_line_index))
            if i != mutant_num_every_order - 1 or mutant_line_num != max_order_num:
                f.write("\n")

    f.close()

