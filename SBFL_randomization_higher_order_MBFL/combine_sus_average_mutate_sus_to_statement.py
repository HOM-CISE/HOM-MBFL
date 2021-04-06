import os
import operator


if __name__ == "__main__":

    with open("./output/suspicious_first_order.txt", 'r') as f_sus_first_order:
        str_sus_first_order = f_sus_first_order.read()
    f_sus_first_order.close()

    list_sus_first_order = str_sus_first_order.split('\n')

    list_Jaccard_sus_first_order \
        = list_sus_first_order[list_sus_first_order.index("Sus_Jaccard:"):list_sus_first_order.index("Sus_Ochiai:")][1:-1]

    list_Ochiai_sus_first_order \
        = list_sus_first_order[list_sus_first_order.index("Sus_Ochiai:"):list_sus_first_order.index("Sus_Op2:")][1:-1]

    list_Op2_sus_first_order\
        = list_sus_first_order[list_sus_first_order.index("Sus_Op2:"):list_sus_first_order.index("Sus_Tarantula:")][1:-1]

    list_Tarantula_sus_first_order \
        = list_sus_first_order[list_sus_first_order.index("Sus_Tarantula:"):list_sus_first_order.index("Sus_Dstar3:")][1:-1]

    list_Dstar3_sus_first_order \
        = list_sus_first_order[list_sus_first_order.index("Sus_Dstar3:"):][1:-2]

    #================================= suspicious_Jaccard_first_order ==================================================
    dict_sus_Jaccard_first_order = {}
    for Jaccard_sus_first_order_line in list_Jaccard_sus_first_order:
        mutant_line = int(Jaccard_sus_first_order_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Jaccard_sus_first_order_line.split(', ')[1].split(')')[0])
        dict_sus_Jaccard_first_order[mutant_line] = sus_mutant_line

    #================================= suspicious_Ochiai_first_order ==================================================
    dict_sus_Ochiai_first_order = {}
    for Ochiai_sus_first_order_line in list_Ochiai_sus_first_order:
        mutant_line = int(Ochiai_sus_first_order_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Ochiai_sus_first_order_line.split(', ')[1].split(')')[0])
        dict_sus_Ochiai_first_order[mutant_line] = sus_mutant_line

    #================================= suspicious_Op2_first_order ==================================================
    dict_sus_Op2_first_order = {}
    for Op2_sus_first_order_line in list_Op2_sus_first_order:
        mutant_line = int(Op2_sus_first_order_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Op2_sus_first_order_line.split(', ')[1].split(')')[0])
        dict_sus_Op2_first_order[mutant_line] = sus_mutant_line

    #================================= suspicious_Tarantula_first_order ==================================================
    dict_sus_Tarantula_first_order = {}
    for Tarantula_sus_first_order_line in list_Tarantula_sus_first_order:
        mutant_line = int(Tarantula_sus_first_order_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Tarantula_sus_first_order_line.split(', ')[1].split(')')[0])
        dict_sus_Tarantula_first_order[mutant_line] = sus_mutant_line

    #================================= suspicious_Dstar3_first_order ==================================================
    dict_sus_Dstar3_first_order = {}
    for Dstar3_sus_first_order_line in list_Dstar3_sus_first_order:
        mutant_line = int(Dstar3_sus_first_order_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Dstar3_sus_first_order_line.split(', ')[1].split(')')[0])
        dict_sus_Dstar3_first_order[mutant_line] = sus_mutant_line

    path_suspicious_set = "./_SBFL_randomization_higher_order_mutant_set/suspicious_set_average.txt"
    path_suspicious_combine = "./_SBFL_randomization_higher_order_mutant_set/suspicious_combine_average.txt"

    with open(path_suspicious_set, 'r') as f_sus_set:
        str_suspicious_set = f_sus_set.read()
    f_sus_set.close()

    list_suspicious_set = str_suspicious_set.split('\n')
    list_Jaccard_sus_set \
        = list_suspicious_set[list_suspicious_set.index("Sus_Jaccard:"):list_suspicious_set.index("Sus_Ochiai:")][1:-1]
    list_Ochiai_sus_set \
        = list_suspicious_set[list_suspicious_set.index("Sus_Ochiai:"):list_suspicious_set.index("Sus_Op2:")][1:-1]
    list_Op2_sus_set \
        = list_suspicious_set[list_suspicious_set.index("Sus_Op2:"):list_suspicious_set.index("Sus_Tarantula:")][1:-1]
    list_Tarantula_sus_set \
        = list_suspicious_set[list_suspicious_set.index("Sus_Tarantula:"):list_suspicious_set.index("Sus_Dstar3:")][1:-1]
    list_Dstar3_sus_set \
        = list_suspicious_set[list_suspicious_set.index("Sus_Dstar3:"):][1:-2]

    # ================================= suspicious_Jaccard_set ==================================================
    dict_sus_Jaccard_set = {}
    for Jaccard_sus_set_line in list_Jaccard_sus_set:
        mutant_line = int(Jaccard_sus_set_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Jaccard_sus_set_line.split(', ')[1].split(')')[0])
        dict_sus_Jaccard_set[mutant_line] = sus_mutant_line

    # ================================= suspicious_Ochiai_set ==================================================
    dict_sus_Ochiai_set = {}
    for Ochiai_sus_set_line in list_Ochiai_sus_set:
        mutant_line = int(Ochiai_sus_set_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Ochiai_sus_set_line.split(', ')[1].split(')')[0])
        dict_sus_Ochiai_set[mutant_line] = sus_mutant_line

    # ================================= suspicious_Op2_set ==================================================
    dict_sus_Op2_set = {}
    for Op2_sus_set_line in list_Op2_sus_set:
        mutant_line = int(Op2_sus_set_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Op2_sus_set_line.split(', ')[1].split(')')[0])
        dict_sus_Op2_set[mutant_line] = sus_mutant_line

    # ================================= suspicious_Tarantula_set ==================================================
    dict_sus_Tarantula_set = {}
    for Tarantula_sus_set_line in list_Tarantula_sus_set:
        mutant_line = int(Tarantula_sus_set_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Tarantula_sus_set_line.split(', ')[1].split(')')[0])
        dict_sus_Tarantula_set[mutant_line] = sus_mutant_line

    # ================================= suspicious_Dstar3_set ==================================================
    dict_sus_Dstar3_set = {}
    for Dstar3_sus_set_line in list_Dstar3_sus_set:
        mutant_line = int(Dstar3_sus_set_line.split('(')[1].split(',')[0])
        sus_mutant_line = float(Dstar3_sus_set_line.split(', ')[1].split(')')[0])
        dict_sus_Dstar3_set[mutant_line] = sus_mutant_line

    # print(dict_sus_Dstar3_set)

    dict_sus_Jaccard_combine = dict_sus_Jaccard_first_order.copy()
    dict_sus_Ochiai_combine = dict_sus_Ochiai_first_order.copy()
    dict_sus_Op2_combine = dict_sus_Op2_first_order.copy()
    dict_sus_Tarantula_combine = dict_sus_Tarantula_first_order.copy()
    dict_sus_Dstar3_combine = dict_sus_Dstar3_first_order.copy()

    for mutant_line in dict_sus_Jaccard_set.keys():
        dict_sus_Jaccard_combine[mutant_line] = max(dict_sus_Jaccard_first_order[mutant_line], dict_sus_Jaccard_set[mutant_line])
    for mutant_line in dict_sus_Ochiai_set:
        dict_sus_Ochiai_combine[mutant_line] = max(dict_sus_Ochiai_first_order[mutant_line], dict_sus_Ochiai_set[mutant_line])
    for mutant_line in dict_sus_Op2_set:
        dict_sus_Op2_combine[mutant_line] = max(dict_sus_Op2_first_order[mutant_line], dict_sus_Op2_set[mutant_line])
    for mutant_line in dict_sus_Tarantula_set:
        dict_sus_Tarantula_combine[mutant_line] = max(dict_sus_Tarantula_first_order[mutant_line], dict_sus_Tarantula_set[mutant_line])
    for mutant_line in dict_sus_Dstar3_set:
        dict_sus_Dstar3_combine[mutant_line] = max(dict_sus_Dstar3_first_order[mutant_line], dict_sus_Dstar3_set[mutant_line])

    Sus_Jaccard = sorted(dict_sus_Jaccard_combine.items(), key=operator.itemgetter(1), reverse=True)
    Sus_Ochiai = sorted(dict_sus_Ochiai_combine.items(), key=operator.itemgetter(1), reverse=True)
    Sus_Op2 = sorted(dict_sus_Op2_combine.items(), key=operator.itemgetter(1), reverse=True)
    Sus_Tarantula = sorted(dict_sus_Tarantula_combine.items(), key=operator.itemgetter(1), reverse=True)
    Sus_Dstar3 = sorted(dict_sus_Dstar3_combine.items(), key=operator.itemgetter(1), reverse=True)

    with open(path_suspicious_combine, 'w') as f:
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
