#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import math
import os
import sys


def Jaccard(fail_s, pass_s, totalPass):
    if (totalPass + pass_s) == 0:
        return sys.float_info.max
    return fail_s / (totalPass + pass_s)


def Ochiai(fail_s, pass_s, totalFail):
    if totalFail * (fail_s + pass_s) == 0:
        return 0
    return fail_s / math.sqrt(totalFail * (fail_s + pass_s))


def Op2(fail_s, pass_s, totalPass):
    return fail_s - pass_s / (totalPass + 1)


def Tarantula(fail_s, pass_s, totalFail, totalPass):
    if totalFail == 0:
        return 0
    if totalPass == 0:
        return 1
    if fail_s / totalFail == 0:
        return 0
    if pass_s / totalPass == 0:
        return 1

    return (fail_s/totalFail) / (fail_s/totalFail + pass_s/totalPass)


def Dstar3(fail_s, pass_s, totalFail):
    if (pass_s + (totalFail - fail_s)) == 0:
        return sys.float_info.max
    return math.pow(fail_s, 3) / (pass_s + (totalFail - fail_s))


# 处理被测程序运行结果向量res_vector.in
if __name__ == "__main__":
    with open("./output/res_vector.in", "r") as f:
        str_vector = f.readline()
        str_vector = str_vector.split("\n")[0]
    f.close()
    # print(str_vector)
    # print(len(str_vector))
    totalPass = 0
    totalFail = 0
    for item in str_vector:
        if item == '0':
            totalPass += 1
        if item == '1':
            totalFail += 1
    # print(totalPass)
    # print(totalFail)

    dict_sus_Jaccard = {}
    dict_sus_Ochiai = {}
    dict_sus_Op2 = {}
    dict_sus_Tarantula = {}
    dict_sus_Dstar3 = {}

    with open("./output/res_cov_matrix.in", "r") as f:
        list_cov_matrix = f.readlines()
    f.close()
    # print(len(list_cov_matrix))
    # print(len(list_cov_matrix[0]))


    dict_line_pass_record = {}
    dict_line_fail_record = {}
    for line_index in range(len(list_cov_matrix[0])):
        dict_line_pass_record[line_index+1] = 0
        dict_line_fail_record[line_index+1] = 0

    for test_case_index in range(len(list_cov_matrix)):
        for line_index in range(len(list_cov_matrix[test_case_index])):
            if list_cov_matrix[test_case_index][line_index] == '1' and str_vector[test_case_index] == '0':
                dict_line_pass_record[line_index+1] += 1
            if list_cov_matrix[test_case_index][line_index] == '1' and str_vector[test_case_index] == '1':
                dict_line_fail_record[line_index+1] += 1
    # print(dict_line_pass_record)
    # print(dict_line_fail_record)

    for line_index in range(len(list_cov_matrix[0])):
        if dict_sus_Jaccard.get(line_index+1) == None:
            dict_sus_Jaccard[line_index+1] \
                = Jaccard(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalPass)
        else:
            dict_sus_Jaccard[line_index+1] \
                = max(dict_sus_Jaccard[line_index+1],
                      Jaccard(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalPass))

        if dict_sus_Ochiai.get(line_index+1) == None:
            dict_sus_Ochiai[line_index+1] \
                = Ochiai(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalFail)
        else:
            dict_sus_Ochiai[line_index+1] \
                = max(dict_sus_Ochiai[line_index+1],
                      Ochiai(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalFail))

        if dict_sus_Op2.get(line_index+1) == None:
            dict_sus_Op2[line_index+1] \
                = Op2(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalPass)
        else:
            dict_sus_Op2[line_index+1] \
                = max(dict_sus_Op2[line_index+1],
                      Op2(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalPass))

        if dict_sus_Tarantula.get(line_index+1) == None:
            dict_sus_Tarantula[line_index+1] \
                = Tarantula(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalFail, totalPass)
        else:
            dict_sus_Tarantula[line_index+1] \
                = max(dict_sus_Tarantula[line_index+1],
                      Tarantula(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalFail, totalPass))

        if dict_sus_Dstar3.get(line_index+1) == None:
            dict_sus_Dstar3[line_index+1] \
                = Dstar3(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalFail)
        else:
            dict_sus_Dstar3[line_index+1] \
                = max(dict_sus_Dstar3[line_index+1],
                      Dstar3(dict_line_fail_record[line_index+1], dict_line_pass_record[line_index+1], totalFail))

    # clean all the non-covered source statement line
    for line_index in range(len(list_cov_matrix[0])):
        if dict_line_fail_record[line_index+1] == 0:
            del dict_sus_Jaccard[line_index+1]
            del dict_sus_Ochiai[line_index+1]
            del dict_sus_Op2[line_index+1]
            del dict_sus_Tarantula[line_index+1]
            del dict_sus_Dstar3[line_index+1]

    dict_sus_Jaccard = sorted(dict_sus_Jaccard.items(), key=operator.itemgetter(1), reverse=True)
    dict_sus_Ochiai = sorted(dict_sus_Ochiai.items(), key=operator.itemgetter(1), reverse=True)
    dict_sus_Op2 = sorted(dict_sus_Op2.items(), key=operator.itemgetter(1), reverse=True)
    dict_sus_Tarantula = sorted(dict_sus_Tarantula.items(), key=operator.itemgetter(1), reverse=True)
    dict_sus_Dstar3 = sorted(dict_sus_Dstar3.items(), key=operator.itemgetter(1), reverse=True)
    # print(dict_sus_Jaccard)
    # print(dict_sus_Ochiai)
    # print(dict_sus_Op2)



    with open("./output/suspicious_SBFL.txt", 'w') as f:
        f.write("")
        f.writelines("Sus_Jaccard:\n")
        for Sus_Jaccard_item in dict_sus_Jaccard:
            f.writelines(str(Sus_Jaccard_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Ochiai:\n")
        for Sus_Ochiai_item in dict_sus_Ochiai:
            f.writelines(str(Sus_Ochiai_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Op2:\n")
        for Sus_Op2_item in dict_sus_Op2:
            f.writelines(str(Sus_Op2_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Tarantula:\n")
        for Sus_Tarantula_item in dict_sus_Tarantula:
            f.writelines(str(Sus_Tarantula_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Dstar3:\n")
        for Sus_Dstar3_item in dict_sus_Dstar3:
            f.writelines(str(Sus_Dstar3_item) + '\n')
        f.writelines("\n")
