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

    with open("./output/all_execute_mutant.txt", 'r') as f:
        list_all_execute_mutant = f.read().split('\n')[0:-1]
    f.close()

    list_sus_Jaccard = []
    list_sus_Ochiai = []
    list_sus_Op2 = []
    list_sus_Tarantula = []
    list_sus_Dstar3 = []

    with open("./output/res_fault_version.in", "r") as f:
        list_fault_version = f.readlines()
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

            with open("./output/suspicious_first_order_Jaccard.txt", 'w') as f:
                str_sus_Jaccard = "\n".join(list_sus_Jaccard)
                f.write(str_sus_Jaccard)
            f.close()
            with open("./output/suspicious_first_order_Ochiai.txt", 'w') as f:
                str_sus_Ochiai = "\n".join(list_sus_Ochiai)
                f.write(str_sus_Ochiai)
            f.close()
            with open("./output/suspicious_first_order_Op2.txt", 'w') as f:
                str_sus_Op2 = "\n".join(list_sus_Op2)
                f.write(str_sus_Op2)
            f.close()
            with open("./output/suspicious_first_order_Tarantula.txt", 'w') as f:
                str_sus_Tarantula = "\n".join(list_sus_Tarantula)
                f.write(str_sus_Tarantula)
            f.close()
            with open("./output/suspicious_first_order_Dstar3.txt", 'w') as f:
                str_sus_Dstar3 = "\n".join(list_sus_Dstar3)
                f.write(str_sus_Dstar3)
            f.close()

            line_index += 1
    f.close()


# 处理被测程序运行结果向量res_vector.in
if __name__ == "__main__":
    with open("./output/res_vector.in", "r") as f:
        r_vector = f.readline()
        r_vector = r_vector.split("\n")[0]
        # r_vector.rstrip("\n")
    f.close()
    # print(r_vector)
    # print(len(r_vector))

    execute_mutant = []
    with open("./output/res_execute_mutant.txt", "r") as f:
        res_execute_mutant = f.readlines()
        for mutant_index in res_execute_mutant:
            mutant_index = mutant_index.rstrip("\n")
            execute_mutant.append(mutant_index)
    f.close()
    # print(len(excute_mutant))
    # print(excute_mutant)

    record = []
    with open("./output/res_record.txt", "r") as f:
        lines = f.readlines()
        for i in execute_mutant:
            sub_str = lines[int(i) - 1]
            sub_str = sub_str.split("line: ")[1]
            sub_str = sub_str.split(" ")[0]
            record.append(int(sub_str))
    f.close()
    # print(len(record))
    # print(record)

    Sus_Jaccard = {}
    Sus_Ochiai = {}
    Sus_Op2 = {}
    Sus_Tarantula = {}
    Sus_Dstar3 = {}

    with open("./output/res_fault_version.in", "r") as f:
        fault_version = f.readlines()
        index = 0
        for fault in fault_version:
            fault = fault.rstrip("\n")
            Anp = 0
            Anf = 0
            Akf = 0
            Akp = 0
            for i in range(len(fault)):
                if r_vector[i] == '0':
                    if fault[i] == '0':
                        Anp += 1
                    else:
                        Akp += 1
                else:
                    if fault[i] == '0':
                        Anf += 1
                    else:
                        Akf += 1

            # print(Anf)
            # print(Anp)
            # print(Akf)
            # print(Akp)
            # print(Anp+Anf+Akf+Akp)
            # print(index,  "+++", record[index])

            if Sus_Jaccard.get(record[index]) == None:
                Sus_Jaccard[record[index]] = Jaccard(Akf, Anf, Akp)
            else:
                Sus_Jaccard[record[index]] = max(Sus_Jaccard[record[index]], Jaccard(Akf, Anf, Akp))

            if Sus_Ochiai.get(record[index]) == None:
                Sus_Ochiai[record[index]] = Ochiai(Akf, Anf, Akp)
            else:
                Sus_Ochiai[record[index]] = max(Sus_Ochiai[record[index]], Ochiai(Akf, Anf, Akp))

            if Sus_Op2.get(record[index]) == None:
                Sus_Op2[record[index]] = Op2(Akf, Akp, Anp)
            else:
                Sus_Op2[record[index]] = max(Sus_Op2[record[index]], Op2(Akf, Akp, Anp))

            if Sus_Tarantula.get(record[index]) == None:
                Sus_Tarantula[record[index]] = Tarantula(Akf, Anf, Akp, Anp)
            else:
                Sus_Tarantula[record[index]] = max(Sus_Tarantula[record[index]], Tarantula(Akf, Anf, Akp, Anp))

            if Sus_Dstar3.get(record[index]) == None:
                Sus_Dstar3[record[index]] = Dstar3(Akf, Akp, Anf)
            else:
                Sus_Dstar3[record[index]] = max(Sus_Dstar3[record[index]], Dstar3(Akf, Akp, Anf))

            index += 1
        # print(len(fault_version))
    f.close()

    # print(Sus_Jaccard)
    # print(Sus_Ochiai)
    # print(Sus_Op2)

    Sus_Jaccard = sorted(Sus_Jaccard.items(), key=operator.itemgetter(1), reverse=True)
    Sus_Ochiai = sorted(Sus_Ochiai.items(), key=operator.itemgetter(1), reverse=True)
    Sus_Op2 = sorted(Sus_Op2.items(), key=operator.itemgetter(1), reverse=True)
    Sus_Tarantula = sorted(Sus_Tarantula.items(), key=operator.itemgetter(1), reverse=True)
    Sus_Dstar3 = sorted(Sus_Dstar3.items(), key=operator.itemgetter(1), reverse=True)

    with open("./output/suspicious_first_order.txt", 'w') as f:
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

    CreateAllMutantSuspicious()  # 创建所有变异体怀疑度列表
