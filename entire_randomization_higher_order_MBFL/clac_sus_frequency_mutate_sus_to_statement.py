#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import math
import os
import sys


def Jaccard(Akf, Anf, Akp):
    if (Akf + Anf + Akp) == 0:
        return 0
    return Akf / (Akf + Anf + Akp)


def Ochiai(Akf, Anf, Akp):
    if (Akf + Anf) * (Akf + Akp) == 0:
        return 0
    return Akf / math.sqrt((Akf + Anf) * (Akf + Akp))


def Op2(Akf, Akp, Anp):
    return Akf - Akp / (Akp + Anp + 1)


def Tarantula(Akf, Anf, Akp, Anp):
    if (Akf + Akp) == 0:
        return 0
    if ((Akf + Anf) != 0) and ((Akp + Anp) == 0):
        return 1

    return (Akf / (Akf + Anf)) / ((Akf / (Akf + Anf)) + (Akp / (Akp + Anp)))


def Dstar3(Akf, Akp, Anf):
    if (Akp + Anf) == 0:
        return sys.float_info.max
    return math.pow(Akf, 3) / (Akp + Anf)


def CreateAllMutantSuspicious():
    str_res_vector = ""  # 记录res_vector.in文件的内容（被测程序运行结果正误向量）
    list_all_execute_mutant = []  # 记录编译成功变异体的信息

    with open("./output/res_vector.in", 'r') as f:
        str_res_vector = f.readline()
        str_res_vector = str_res_vector.split('\n')[0]
    f.close()

    with open("./_entire_randomization_higher_order_mutant_set/all_execute_mutant.txt", 'r') as f:
        list_all_execute_mutant = f.read().split('\n')[0:-1]
    f.close()

    list_sus_Jaccard = []
    list_sus_Ochiai = []
    list_sus_Op2 = []
    list_sus_Tarantula = []
    list_sus_Dstar3 = []

    with open("./_entire_randomization_higher_order_mutant_set/res_fault_version.in", "r") as f_fault:
        list_fault_version = f_fault.readlines()
    f_fault.close()

    line_index = 0
    for str_fault_version_line in list_fault_version:
        str_fault_version_line = str_fault_version_line.rstrip("\n")
        Anp = 0
        Anf = 0
        Akf = 0
        Akp = 0
        for i in range(len(str_fault_version_line)):
            if str_res_vector[i] == '0':
                if str_fault_version_line[i] == '0':
                    Anp += 1
                else:
                    Akp += 1
            else:
                if str_fault_version_line[i] == '0':
                    Anf += 1
                else:
                    Akf += 1

        list_sus_Jaccard.append("Jaccard_Sus: " + str(Jaccard(Akf, Anf, Akp)) + "   "
                                + " Anp:" + str(Anp) + " Anf:" + str(Anf) + " Akp:" + str(Akp) + " Akf:" + str(Akf) + "   "
                                + list_all_execute_mutant[line_index])
        list_sus_Ochiai.append("Ochiai_Sus: " + str(Ochiai(Akf, Anf, Akp)) + "   "
                               + " Anp:" + str(Anp) + " Anf:" + str(Anf) + " Akp:" + str(Akp) + " Akf:" + str(Akf) + "   "
                               + list_all_execute_mutant[line_index])
        list_sus_Op2.append("Op2_Sus: " + str(Op2(Akf, Akp, Anp)) + "   "
                            + " Anp:" + str(Anp) + " Anf:" + str(Anf) + " Akp:" + str(Akp) + " Akf:" + str(Akf) + "   "
                            + list_all_execute_mutant[line_index])
        list_sus_Tarantula.append("Tarantula_Sus: " + str(Tarantula(Akf, Anf, Akp, Anp)) + "   "
                                  + " Anp:" + str(Anp) + " Anf:" + str(Anf) + " Akp:" + str(Akp) + " Akf:" + str(Akf) + "   "
                                  + list_all_execute_mutant[line_index])
        list_sus_Dstar3.append("Dstar3_Sus: " + str(Dstar3(Akf, Akp, Anf)) + "   "
                               + " Anp:" + str(Anp) + " Anf:" + str(Anf) + " Akp:" + str(Akp) + " Akf:" + str(Akf) + "   "
                               + list_all_execute_mutant[line_index])
        line_index += 1


    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Jaccard.txt", 'w') as f:
        str_sus_Jaccard = "\n".join(list_sus_Jaccard)
        f.write(str_sus_Jaccard)
    f.close()
    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Ochiai.txt", 'w') as f:
        str_sus_Ochiai = "\n".join(list_sus_Ochiai)
        f.write(str_sus_Ochiai)
    f.close()
    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Op2.txt", 'w') as f:
        str_sus_Op2 = "\n".join(list_sus_Op2)
        f.write(str_sus_Op2)
    f.close()
    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Tarantula.txt", 'w') as f:
        str_sus_Tarantula = "\n".join(list_sus_Tarantula)
        f.write(str_sus_Tarantula)
    f.close()
    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Dstar3.txt", 'w') as f:
        str_sus_Dstar3 = "\n".join(list_sus_Dstar3)
        f.write(str_sus_Dstar3)
    f.close()


if __name__ == "__main__":

    # CreateAllMutantSuspicious()  # 创建所有变异体怀疑度列表

    # statistical Jaccard suspicious ranking table ============================================================
    dict_sus_Jaccard = {}

    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Jaccard.txt", 'r') as f:
        list_sus_Jaccard = f.read().split('\n')
    f.close()

    for sus_Jaccard_line in list_sus_Jaccard:
        suspicious_now = float(sus_Jaccard_line.split("_Sus: ")[1].split("    Anp:")[0])
        list_source_line = sus_Jaccard_line.split("line: ")[1:]
        for source_line_index in range(len(list_source_line)):
            list_source_line[source_line_index] = int(list_source_line[source_line_index].split("   index:")[0])

        for source_line in list_source_line:
            if dict_sus_Jaccard.get(source_line) == None:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Jaccard[source_line] = [item_suspicious, item_frequency]
            if dict_sus_Jaccard[source_line][0] < suspicious_now:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Jaccard[source_line] = [item_suspicious, item_frequency]
            elif dict_sus_Jaccard[source_line][0] == suspicious_now:
                dict_sus_Jaccard[source_line][1] += 1

    Sus_Jaccard = sorted(dict_sus_Jaccard.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    # for item in Sus_Jaccard:
    #     print(item)

    # statistical Ochiai suspicious ranking table ============================================================
    dict_sus_Ochiai = {}

    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Ochiai.txt", 'r') as f:
        list_sus_Ochiai = f.read().split('\n')
    f.close()

    for sus_Ochiai_line in list_sus_Ochiai:
        suspicious_now = float(sus_Ochiai_line.split("_Sus: ")[1].split("    Anp:")[0])
        list_source_line = sus_Ochiai_line.split("line: ")[1:]
        for source_line_index in range(len(list_source_line)):
            list_source_line[source_line_index] = int(list_source_line[source_line_index].split("   index:")[0])

        for source_line in list_source_line:
            if dict_sus_Ochiai.get(source_line) == None:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Ochiai[source_line] = [item_suspicious, item_frequency]
            if dict_sus_Ochiai[source_line][0] < suspicious_now:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Ochiai[source_line] = [item_suspicious, item_frequency]
            elif dict_sus_Ochiai[source_line][0] == suspicious_now:
                dict_sus_Ochiai[source_line][1] += 1

    Sus_Ochiai = sorted(dict_sus_Ochiai.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

    # statistical Op2 suspicious ranking table ============================================================
    dict_sus_Op2 = {}

    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Op2.txt", 'r') as f:
        list_sus_Op2 = f.read().split('\n')
    f.close()

    for sus_Op2_line in list_sus_Op2:
        suspicious_now = float(sus_Op2_line.split("_Sus: ")[1].split("    Anp:")[0])
        list_source_line = sus_Op2_line.split("line: ")[1:]
        for source_line_index in range(len(list_source_line)):
            list_source_line[source_line_index] = int(list_source_line[source_line_index].split("   index:")[0])

        for source_line in list_source_line:
            if dict_sus_Op2.get(source_line) == None:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Op2[source_line] = [item_suspicious, item_frequency]
            if dict_sus_Op2[source_line][0] < suspicious_now:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Op2[source_line] = [item_suspicious, item_frequency]
            elif dict_sus_Op2[source_line][0] == suspicious_now:
                dict_sus_Op2[source_line][1] += 1

    Sus_Op2 = sorted(dict_sus_Op2.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

    # statistical Tarantula suspicious ranking table ============================================================
    dict_sus_Tarantula = {}

    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Tarantula.txt", 'r') as f:
        list_sus_Tarantula = f.read().split('\n')
    f.close()

    for sus_Tarantula_line in list_sus_Tarantula:
        suspicious_now = float(sus_Tarantula_line.split("_Sus: ")[1].split("    Anp:")[0])
        list_source_line = sus_Tarantula_line.split("line: ")[1:]
        for source_line_index in range(len(list_source_line)):
            list_source_line[source_line_index] = int(list_source_line[source_line_index].split("   index:")[0])

        for source_line in list_source_line:
            if dict_sus_Tarantula.get(source_line) == None:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Tarantula[source_line] = [item_suspicious, item_frequency]
            if dict_sus_Tarantula[source_line][0] < suspicious_now:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Tarantula[source_line] = [item_suspicious, item_frequency]
            elif dict_sus_Tarantula[source_line][0] == suspicious_now:
                dict_sus_Tarantula[source_line][1] += 1

    Sus_Tarantula = sorted(dict_sus_Tarantula.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

    # statistical Dstar3 suspicious ranking table ============================================================
    dict_sus_Dstar3 = {}

    with open("./_entire_randomization_higher_order_mutant_set/suspicious_Dstar3.txt", 'r') as f:
        list_sus_Dstar3 = f.read().split('\n')
    f.close()

    for sus_Dstar3_line in list_sus_Dstar3:
        suspicious_now = float(sus_Dstar3_line.split("_Sus: ")[1].split("    Anp:")[0])
        list_source_line = sus_Dstar3_line.split("line: ")[1:]
        for source_line_index in range(len(list_source_line)):
            list_source_line[source_line_index] = int(list_source_line[source_line_index].split("   index:")[0])

        for source_line in list_source_line:
            if dict_sus_Dstar3.get(source_line) == None:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Dstar3[source_line] = [item_suspicious, item_frequency]
            if dict_sus_Dstar3[source_line][0] < suspicious_now:
                item_suspicious = suspicious_now
                item_frequency = 1
                dict_sus_Dstar3[source_line] = [item_suspicious, item_frequency]
            elif dict_sus_Dstar3[source_line][0] == suspicious_now:
                dict_sus_Dstar3[source_line][1] += 1

    Sus_Dstar3 = sorted(dict_sus_Dstar3.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

    # output the result of mutants' suspicious.
    with open("./_entire_randomization_higher_order_mutant_set/suspicious_set_frequency.txt", 'w') as f:
        f.write("")
        f.writelines("Sus_Jaccard:\n")
        for Sus_Jaccard_item in Sus_Jaccard:
            f.writelines(str(Sus_Jaccard_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Ochiai:\n")
        for Sus_Ochiai_item in Sus_Ochiai:
            f.writelines(str(Sus_Ochiai_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Op2:\n")
        for Sus_Op2_item in Sus_Op2:
            f.writelines(str(Sus_Op2_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Tarantula:\n")
        for Sus_Tarantula_item in Sus_Tarantula:
            f.writelines(str(Sus_Tarantula_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Dstar3:\n")
        for Sus_Dstar3_item in Sus_Dstar3:
            f.writelines(str(Sus_Dstar3_item) + '\n')
        f.writelines("\n")

    f.close()
