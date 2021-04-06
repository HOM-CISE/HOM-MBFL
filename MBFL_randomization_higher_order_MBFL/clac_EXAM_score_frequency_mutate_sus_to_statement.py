import operator


def calcRankValue(m, n):
    return ((m+1) + (m+n)) / 2


def calcEXAM(rank, N):
    return rank / N


def calcRankm(list_sus_rank, num_fault_line):
    now_num_fault_line = 0
    now_fault_line_index = 0
    for index in range(len(list_sus_rank)):
        if list_sus_rank[index][2] == True:
            now_num_fault_line = now_num_fault_line + 1
        if now_num_fault_line >= num_fault_line:
            now_fault_line_index = index
            break
    # print(now_fault_line_index)

    # can't locate the now_num_fault_line'th faults.
    if now_num_fault_line < num_fault_line:
        return 99999999

    rank_m = 0
    now_rank = list_sus_rank[now_fault_line_index][0]
    for index in range(now_fault_line_index):
        if list_sus_rank[index][0] < now_rank:
            if list_sus_rank[index][2] == False:
                rank_m = rank_m + 1

    return rank_m


def calcRankn(list_sus_rank, num_fault_line):
    now_num_fault_line = 0
    now_fault_line_index = 0
    for index in range(len(list_sus_rank)):
        if list_sus_rank[index][2] == True:
            now_num_fault_line = now_num_fault_line + 1
        if now_num_fault_line >= num_fault_line:
            now_fault_line_index = index
            break
    # print(now_fault_line_index)

    rank_n = 0
    now_rank = list_sus_rank[now_fault_line_index][0]
    for index in range(len(list_sus_rank)):
        if list_sus_rank[index][0] > now_rank:
            break
        if list_sus_rank[index][0] == now_rank:
            if list_sus_rank[index][2] == False:
                rank_n = rank_n + 1
    # print(rank_n)

    return rank_n


def calcRankCombine(list_fault_line, suspicious_file_root):
    suspicious_file_path = suspicious_file_root + "suspicious_combine_frequency.txt"
    with open(suspicious_file_path, 'r') as f_suspicious_file:
        str_suspicious_list_file = f_suspicious_file.read()
        list_suspicious = str_suspicious_list_file.split('\n')
    f_suspicious_file.close()

    list_Jaccard_suspicious \
        = list_suspicious[list_suspicious.index("Sus_Jaccard:"):list_suspicious.index("Sus_Ochiai:")][1:-1]
    list_Ochiai_suspicious \
        = list_suspicious[list_suspicious.index("Sus_Ochiai:"):list_suspicious.index("Sus_Op2:")][1:-1]
    list_Op2_suspicious\
        = list_suspicious[list_suspicious.index("Sus_Op2:"):list_suspicious.index("Sus_Tarantula:")][1:-1]
    list_Tarantula_suspicious \
        = list_suspicious[list_suspicious.index("Sus_Tarantula:"):list_suspicious.index("Sus_Dstar3:")][1:-1]
    list_Dstar3_suspicious \
        = list_suspicious[list_suspicious.index("Sus_Dstar3:"):][1:-2]

    #================================= suspicious_Jaccard ==================================================
    dict_sus_Jaccard = {}
    for Jaccard_suspicious in list_Jaccard_suspicious:
        mutant_line = int(Jaccard_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Jaccard_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Jaccard_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Jaccard[mutant_line] = [sus_mutant_line, frequency_mutant_line]

    #================================= suspicious_Ochiai ==================================================
    dict_sus_Ochiai = {}
    for Ochiai_suspicious in list_Ochiai_suspicious:
        mutant_line = int(Ochiai_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Ochiai_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Ochiai_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Ochiai[mutant_line] = [sus_mutant_line, frequency_mutant_line]

    #================================= suspicious_Op2 ==================================================
    dict_sus_Op2 = {}
    for Op2_suspicious in list_Op2_suspicious:
        mutant_line = int(Op2_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Op2_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Op2_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Op2[mutant_line] = [sus_mutant_line, frequency_mutant_line]

    #================================= suspicious_Tarantula ==================================================
    dict_sus_Tarantula = {}
    for Tarantula_suspicious in list_Tarantula_suspicious:
        mutant_line = int(Tarantula_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Tarantula_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Tarantula_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Tarantula[mutant_line] = [sus_mutant_line, frequency_mutant_line]

    #================================= suspicious_Dstar3 ==================================================
    dict_sus_Dstar3 = {}
    for Dstar3_suspicious in list_Dstar3_suspicious:
        mutant_line = int(Dstar3_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Dstar3_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Dstar3_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Dstar3[mutant_line] = [sus_mutant_line, frequency_mutant_line]


    Sus_Jaccard = sorted(dict_sus_Jaccard.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    Sus_Ochiai = sorted(dict_sus_Ochiai.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    Sus_Op2 = sorted(dict_sus_Op2.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    Sus_Tarantula = sorted(dict_sus_Tarantula.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    Sus_Dstar3 = sorted(dict_sus_Dstar3.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

    # ============================== sus_rank_Jaccard ====================================================
    list_sus_rank_Jaccard = []
    for sus_Jaccard_index in range(len(Sus_Jaccard)):
        is_fault = (str(Sus_Jaccard[sus_Jaccard_index][0]) in list_fault_line)
        list_sus_rank_Jaccard.append([sus_Jaccard_index+1, Sus_Jaccard[sus_Jaccard_index][0], is_fault, Sus_Jaccard[sus_Jaccard_index][1]])

    for sus_Jaccard_index in range(1, len(list_sus_rank_Jaccard)):
        if list_sus_rank_Jaccard[sus_Jaccard_index][3] == list_sus_rank_Jaccard[sus_Jaccard_index-1][3]:
            list_sus_rank_Jaccard[sus_Jaccard_index][0] = list_sus_rank_Jaccard[sus_Jaccard_index-1][0]
        else:
            list_sus_rank_Jaccard[sus_Jaccard_index][0] = list_sus_rank_Jaccard[sus_Jaccard_index - 1][0] + 1
    # print(list_sus_rank_Jaccard)

    # ============================== sus_rank_Ochiai ==================================================
    list_sus_rank_Ochiai = []
    for sus_Ochiai_index in range(len(Sus_Ochiai)):
        is_fault = (str(Sus_Ochiai[sus_Ochiai_index][0]) in list_fault_line)
        list_sus_rank_Ochiai.append([sus_Ochiai_index+1, Sus_Ochiai[sus_Ochiai_index][0], is_fault, Sus_Ochiai[sus_Ochiai_index][1]])

    for sus_Ochiai_index in range(1, len(list_sus_rank_Ochiai)):
        if list_sus_rank_Ochiai[sus_Ochiai_index][3] == list_sus_rank_Ochiai[sus_Ochiai_index-1][3]:
            list_sus_rank_Ochiai[sus_Ochiai_index][0] = list_sus_rank_Ochiai[sus_Ochiai_index-1][0]
        else:
            list_sus_rank_Ochiai[sus_Ochiai_index][0] = list_sus_rank_Ochiai[sus_Ochiai_index - 1][0] + 1

    # ============================== sus_rank_Op2 ==================================================
    list_sus_rank_Op2 = []
    for sus_Op2_index in range(len(Sus_Op2)):
        is_fault = (str(Sus_Op2[sus_Op2_index][0]) in list_fault_line)
        list_sus_rank_Op2.append([sus_Op2_index+1, Sus_Op2[sus_Op2_index][0], is_fault, Sus_Op2[sus_Op2_index][1]])

    for sus_Op2_index in range(1, len(list_sus_rank_Op2)):
        if list_sus_rank_Op2[sus_Op2_index][3] == list_sus_rank_Op2[sus_Op2_index-1][3]:
            list_sus_rank_Op2[sus_Op2_index][0] = list_sus_rank_Op2[sus_Op2_index-1][0]
        else:
            list_sus_rank_Op2[sus_Op2_index][0] = list_sus_rank_Op2[sus_Op2_index - 1][0] + 1

    # ============================== sus_rank_Tarantula ==================================================
    list_sus_rank_Tarantula = []
    for sus_Tarantula_index in range(len(Sus_Tarantula)):
        is_fault = (str(Sus_Tarantula[sus_Tarantula_index][0]) in list_fault_line)
        list_sus_rank_Tarantula.append([sus_Tarantula_index+1, Sus_Tarantula[sus_Tarantula_index][0], is_fault, Sus_Tarantula[sus_Tarantula_index][1]])

    for sus_Tarantula_index in range(1, len(list_sus_rank_Tarantula)):
        if list_sus_rank_Tarantula[sus_Tarantula_index][3] == list_sus_rank_Tarantula[sus_Tarantula_index-1][3]:
            list_sus_rank_Tarantula[sus_Tarantula_index][0] = list_sus_rank_Tarantula[sus_Tarantula_index-1][0]
        else:
            list_sus_rank_Tarantula[sus_Tarantula_index][0] = list_sus_rank_Tarantula[sus_Tarantula_index - 1][0] + 1

    # ============================== sus_rank_Dstar3 ==================================================
    list_sus_rank_Dstar3 = []
    for sus_Dstar3_index in range(len(Sus_Dstar3)):
        is_fault = (str(Sus_Dstar3[sus_Dstar3_index][0]) in list_fault_line)
        list_sus_rank_Dstar3.append([sus_Dstar3_index+1, Sus_Dstar3[sus_Dstar3_index][0], is_fault, Sus_Dstar3[sus_Dstar3_index][1]])

    for sus_Dstar3_index in range(1, len(list_sus_rank_Dstar3)):
        if list_sus_rank_Dstar3[sus_Dstar3_index][3] == list_sus_rank_Dstar3[sus_Dstar3_index-1][3]:
            list_sus_rank_Dstar3[sus_Dstar3_index][0] = list_sus_rank_Dstar3[sus_Dstar3_index-1][0]
        else:
            list_sus_rank_Dstar3[sus_Dstar3_index][0] = list_sus_rank_Dstar3[sus_Dstar3_index - 1][0] + 1

    with open(suspicious_file_root + "suspicious_rank_combine_frequency.txt", 'w') as f:
        f.write("rank     line     is_fault_line     suspicious")
        f.write("\n\n")
        f.writelines("Sus_Jaccard:\n")
        for Sus_Jaccard_item in list_sus_rank_Jaccard:
            f.writelines(str(Sus_Jaccard_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Ochiai:\n")
        for Sus_Ochiai_item in list_sus_rank_Ochiai:
            f.writelines(str(Sus_Ochiai_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Op2:\n")
        for Sus_Op2_item in list_sus_rank_Op2:
            f.writelines(str(Sus_Op2_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Tarantula:\n")
        for Sus_Tarantula_item in list_sus_rank_Tarantula:
            f.writelines(str(Sus_Tarantula_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Dstar3:\n")
        for Sus_Dstar3_item in list_sus_rank_Dstar3:
            f.writelines(str(Sus_Dstar3_item) + '\n')
        f.writelines("\n")
    f.close()

    return (list_sus_rank_Jaccard, list_sus_rank_Ochiai, list_sus_rank_Op2, list_sus_rank_Tarantula, list_sus_rank_Dstar3)


def calcEXAMScoreCombine(list_fault_line, suspicious_file_root):
    # 1. return rank of all types of suspicious, and output "suspicious_rank.txt" in suspicious_file_root.
    tuple_rank_result = calcRankCombine(list_fault_line, suspicious_file_root)
    list_sus_rank_Jaccard, list_sus_rank_Ochiai, list_sus_rank_Op2, list_sus_rank_Tarantula, list_sus_rank_Dstar3 = (tuple_rank_result)


    # 2. calculate rank and EXAM score

    f = open(suspicious_file_root + "suspicious_EXAM_score_combine_frequency.txt", 'w')
    f.write(suspicious_file_root+"\n\n\n")


    sum_Jaccard_EXAM = 0
    sum_Ochiai_EXAM = 0
    sum_Op2_EXAM = 0
    sum_Tarantula_EXAM = 0
    sum_Dstar3_EXAM = 0

    for num_fault_line in range(1, len(list_fault_line)+1):
        f.write("Locate the EXAM score for the " + str(num_fault_line) + "th statement.\n\n")

        Jaccard_rank_m = calcRankm(list_sus_rank_Jaccard, num_fault_line)
        Jaccard_rank_n = calcRankn(list_sus_rank_Jaccard, num_fault_line)
        Jaccard_rank_N = len(list_sus_rank_Jaccard)
        Jaccard_rank = calcRankValue(Jaccard_rank_m, Jaccard_rank_n)
        Jaccard_EXAM = calcEXAM(Jaccard_rank, Jaccard_rank_N)
        f.write("Jaccard_EXAM: " + str(Jaccard_EXAM) + '\n')
        sum_Jaccard_EXAM = sum_Jaccard_EXAM + Jaccard_EXAM

        Ochiai_rank_m = calcRankm(list_sus_rank_Ochiai, num_fault_line)
        Ochiai_rank_n = calcRankn(list_sus_rank_Ochiai, num_fault_line)
        Ochiai_rank_N = len(list_sus_rank_Ochiai)
        Ochiai_rank = calcRankValue(Ochiai_rank_m, Ochiai_rank_n)
        Ochiai_EXAM = calcEXAM(Ochiai_rank, Ochiai_rank_N)
        f.write("Ochiai_EXAM: " + str(Ochiai_EXAM) + '\n')
        sum_Ochiai_EXAM = sum_Ochiai_EXAM + Ochiai_EXAM

        Op2_rank_m = calcRankm(list_sus_rank_Op2, num_fault_line)
        Op2_rank_n = calcRankn(list_sus_rank_Op2, num_fault_line)
        Op2_rank_N = len(list_sus_rank_Op2)
        Op2_rank = calcRankValue(Op2_rank_m, Op2_rank_n)
        Op2_EXAM = calcEXAM(Op2_rank, Op2_rank_N)
        f.write("Op2_EXAM: " + str(Op2_EXAM) + '\n')
        sum_Op2_EXAM = sum_Op2_EXAM + Op2_EXAM

        Tarantula_rank_m = calcRankm(list_sus_rank_Tarantula, num_fault_line)
        Tarantula_rank_n = calcRankn(list_sus_rank_Tarantula, num_fault_line)
        Tarantula_rank_N = len(list_sus_rank_Tarantula)
        Tarantula_rank = calcRankValue(Tarantula_rank_m, Tarantula_rank_n)
        Tarantula_EXAM = calcEXAM(Tarantula_rank, Tarantula_rank_N)
        f.write("Tarantula_EXAM: " + str(Tarantula_EXAM) + '\n')
        sum_Tarantula_EXAM = sum_Tarantula_EXAM + Tarantula_EXAM

        Dstar3_rank_m = calcRankm(list_sus_rank_Dstar3, num_fault_line)
        Dstar3_rank_n = calcRankn(list_sus_rank_Dstar3, num_fault_line)
        Dstar3_rank_N = len(list_sus_rank_Dstar3)
        Dstar3_rank = calcRankValue(Dstar3_rank_m, Dstar3_rank_n)
        Dstar3_EXAM = calcEXAM(Dstar3_rank, Dstar3_rank_N)
        f.write("Dstar3_EXAM: " + str(Dstar3_EXAM) + '\n')
        sum_Dstar3_EXAM = sum_Dstar3_EXAM + Dstar3_EXAM

        f.write("\n\n")

    f.write("Locate the average EXAM score for all of the statements.\n")
    f.write("Jaccard_EXAM: " + str(sum_Jaccard_EXAM / len(list_fault_line)) + '\n')
    f.write("Ochiai_EXAM: " + str(sum_Ochiai_EXAM / len(list_fault_line)) + '\n')
    f.write("Op2_EXAM: " + str(sum_Op2_EXAM / len(list_fault_line)) + '\n')
    f.write("Tarantula_EXAM: " + str(sum_Tarantula_EXAM / len(list_fault_line)) + '\n')
    f.write("Dstar3_EXAM: " + str(sum_Dstar3_EXAM / len(list_fault_line)) + '\n')
    f.close()


def calcRankSet(list_fault_line, suspicious_file_root):
    suspicious_file_path = suspicious_file_root + "suspicious_set_frequency.txt"
    with open(suspicious_file_path, 'r') as f_suspicious_file:
        str_suspicious_list_file = f_suspicious_file.read()
        list_suspicious = str_suspicious_list_file.split('\n')
    f_suspicious_file.close()

    list_Jaccard_suspicious \
        = list_suspicious[list_suspicious.index("Sus_Jaccard:"):list_suspicious.index("Sus_Ochiai:")][1:-1]
    list_Ochiai_suspicious \
        = list_suspicious[list_suspicious.index("Sus_Ochiai:"):list_suspicious.index("Sus_Op2:")][1:-1]
    list_Op2_suspicious\
        = list_suspicious[list_suspicious.index("Sus_Op2:"):list_suspicious.index("Sus_Tarantula:")][1:-1]
    list_Tarantula_suspicious \
        = list_suspicious[list_suspicious.index("Sus_Tarantula:"):list_suspicious.index("Sus_Dstar3:")][1:-1]
    list_Dstar3_suspicious \
        = list_suspicious[list_suspicious.index("Sus_Dstar3:"):][1:-2]

    #================================= suspicious_Jaccard ==================================================
    dict_sus_Jaccard = {}
    for Jaccard_suspicious in list_Jaccard_suspicious:
        mutant_line = int(Jaccard_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Jaccard_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Jaccard_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Jaccard[mutant_line] = [sus_mutant_line, frequency_mutant_line]

    #================================= suspicious_Ochiai ==================================================
    dict_sus_Ochiai = {}
    for Ochiai_suspicious in list_Ochiai_suspicious:
        mutant_line = int(Ochiai_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Ochiai_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Ochiai_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Ochiai[mutant_line] = [sus_mutant_line, frequency_mutant_line]

    #================================= suspicious_Op2 ==================================================
    dict_sus_Op2 = {}
    for Op2_suspicious in list_Op2_suspicious:
        mutant_line = int(Op2_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Op2_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Op2_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Op2[mutant_line] = [sus_mutant_line, frequency_mutant_line]

    #================================= suspicious_Tarantula ==================================================
    dict_sus_Tarantula = {}
    for Tarantula_suspicious in list_Tarantula_suspicious:
        mutant_line = int(Tarantula_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Tarantula_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Tarantula_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Tarantula[mutant_line] = [sus_mutant_line, frequency_mutant_line]

    #================================= suspicious_Dstar3 ==================================================
    dict_sus_Dstar3 = {}
    for Dstar3_suspicious in list_Dstar3_suspicious:
        mutant_line = int(Dstar3_suspicious.split('(')[1].split(',')[0])
        sus_mutant_line = float(Dstar3_suspicious.split(', [')[1].split(',')[0])
        frequency_mutant_line = int(Dstar3_suspicious.split(', ')[2].split(']')[0])
        dict_sus_Dstar3[mutant_line] = [sus_mutant_line, frequency_mutant_line]


    Sus_Jaccard = sorted(dict_sus_Jaccard.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    Sus_Ochiai = sorted(dict_sus_Ochiai.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    Sus_Op2 = sorted(dict_sus_Op2.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    Sus_Tarantula = sorted(dict_sus_Tarantula.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    Sus_Dstar3 = sorted(dict_sus_Dstar3.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

    # ============================== sus_rank_Jaccard ====================================================
    list_sus_rank_Jaccard = []
    for sus_Jaccard_index in range(len(Sus_Jaccard)):
        is_fault = (str(Sus_Jaccard[sus_Jaccard_index][0]) in list_fault_line)
        list_sus_rank_Jaccard.append([sus_Jaccard_index+1, Sus_Jaccard[sus_Jaccard_index][0], is_fault, Sus_Jaccard[sus_Jaccard_index][1]])

    for sus_Jaccard_index in range(1, len(list_sus_rank_Jaccard)):
        if list_sus_rank_Jaccard[sus_Jaccard_index][3] == list_sus_rank_Jaccard[sus_Jaccard_index-1][3]:
            list_sus_rank_Jaccard[sus_Jaccard_index][0] = list_sus_rank_Jaccard[sus_Jaccard_index-1][0]
        else:
            list_sus_rank_Jaccard[sus_Jaccard_index][0] = list_sus_rank_Jaccard[sus_Jaccard_index - 1][0] + 1
    # print(list_sus_rank_Jaccard)

    # ============================== sus_rank_Ochiai ==================================================
    list_sus_rank_Ochiai = []
    for sus_Ochiai_index in range(len(Sus_Ochiai)):
        is_fault = (str(Sus_Ochiai[sus_Ochiai_index][0]) in list_fault_line)
        list_sus_rank_Ochiai.append([sus_Ochiai_index+1, Sus_Ochiai[sus_Ochiai_index][0], is_fault, Sus_Ochiai[sus_Ochiai_index][1]])

    for sus_Ochiai_index in range(1, len(list_sus_rank_Ochiai)):
        if list_sus_rank_Ochiai[sus_Ochiai_index][3] == list_sus_rank_Ochiai[sus_Ochiai_index-1][3]:
            list_sus_rank_Ochiai[sus_Ochiai_index][0] = list_sus_rank_Ochiai[sus_Ochiai_index-1][0]
        else:
            list_sus_rank_Ochiai[sus_Ochiai_index][0] = list_sus_rank_Ochiai[sus_Ochiai_index - 1][0] + 1

    # ============================== sus_rank_Op2 ==================================================
    list_sus_rank_Op2 = []
    for sus_Op2_index in range(len(Sus_Op2)):
        is_fault = (str(Sus_Op2[sus_Op2_index][0]) in list_fault_line)
        list_sus_rank_Op2.append([sus_Op2_index+1, Sus_Op2[sus_Op2_index][0], is_fault, Sus_Op2[sus_Op2_index][1]])

    for sus_Op2_index in range(1, len(list_sus_rank_Op2)):
        if list_sus_rank_Op2[sus_Op2_index][3] == list_sus_rank_Op2[sus_Op2_index-1][3]:
            list_sus_rank_Op2[sus_Op2_index][0] = list_sus_rank_Op2[sus_Op2_index-1][0]
        else:
            list_sus_rank_Op2[sus_Op2_index][0] = list_sus_rank_Op2[sus_Op2_index - 1][0] + 1

    # ============================== sus_rank_Tarantula ==================================================
    list_sus_rank_Tarantula = []
    for sus_Tarantula_index in range(len(Sus_Tarantula)):
        is_fault = (str(Sus_Tarantula[sus_Tarantula_index][0]) in list_fault_line)
        list_sus_rank_Tarantula.append([sus_Tarantula_index+1, Sus_Tarantula[sus_Tarantula_index][0], is_fault, Sus_Tarantula[sus_Tarantula_index][1]])

    for sus_Tarantula_index in range(1, len(list_sus_rank_Tarantula)):
        if list_sus_rank_Tarantula[sus_Tarantula_index][3] == list_sus_rank_Tarantula[sus_Tarantula_index-1][3]:
            list_sus_rank_Tarantula[sus_Tarantula_index][0] = list_sus_rank_Tarantula[sus_Tarantula_index-1][0]
        else:
            list_sus_rank_Tarantula[sus_Tarantula_index][0] = list_sus_rank_Tarantula[sus_Tarantula_index - 1][0] + 1

    # ============================== sus_rank_Dstar3 ==================================================
    list_sus_rank_Dstar3 = []
    for sus_Dstar3_index in range(len(Sus_Dstar3)):
        is_fault = (str(Sus_Dstar3[sus_Dstar3_index][0]) in list_fault_line)
        list_sus_rank_Dstar3.append([sus_Dstar3_index+1, Sus_Dstar3[sus_Dstar3_index][0], is_fault, Sus_Dstar3[sus_Dstar3_index][1]])

    for sus_Dstar3_index in range(1, len(list_sus_rank_Dstar3)):
        if list_sus_rank_Dstar3[sus_Dstar3_index][3] == list_sus_rank_Dstar3[sus_Dstar3_index-1][3]:
            list_sus_rank_Dstar3[sus_Dstar3_index][0] = list_sus_rank_Dstar3[sus_Dstar3_index-1][0]
        else:
            list_sus_rank_Dstar3[sus_Dstar3_index][0] = list_sus_rank_Dstar3[sus_Dstar3_index - 1][0] + 1

    with open(suspicious_file_root + "suspicious_rank_set_frequency.txt", 'w') as f:
        f.write("rank     line     is_fault_line     suspicious")
        f.write("\n\n")
        f.writelines("Sus_Jaccard:\n")
        for Sus_Jaccard_item in list_sus_rank_Jaccard:
            f.writelines(str(Sus_Jaccard_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Ochiai:\n")
        for Sus_Ochiai_item in list_sus_rank_Ochiai:
            f.writelines(str(Sus_Ochiai_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Op2:\n")
        for Sus_Op2_item in list_sus_rank_Op2:
            f.writelines(str(Sus_Op2_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Tarantula:\n")
        for Sus_Tarantula_item in list_sus_rank_Tarantula:
            f.writelines(str(Sus_Tarantula_item) + '\n')
        f.writelines("\n")

        f.writelines("Sus_Dstar3:\n")
        for Sus_Dstar3_item in list_sus_rank_Dstar3:
            f.writelines(str(Sus_Dstar3_item) + '\n')
        f.writelines("\n")
    f.close()

    return (list_sus_rank_Jaccard, list_sus_rank_Ochiai, list_sus_rank_Op2, list_sus_rank_Tarantula, list_sus_rank_Dstar3)


def calcEXAMScoreSet(list_fault_line, suspicious_file_root):
    # 1. return rank of all types of suspicious, and output "suspicious_rank.txt" in suspicious_file_root.
    tuple_rank_result = calcRankSet(list_fault_line, suspicious_file_root)
    list_sus_rank_Jaccard, list_sus_rank_Ochiai, list_sus_rank_Op2, list_sus_rank_Tarantula, list_sus_rank_Dstar3 = (tuple_rank_result)


    # 2. calculate rank and EXAM score

    f = open(suspicious_file_root + "suspicious_EXAM_score_set_frequency.txt", 'w')
    f.write(suspicious_file_root+"\n\n\n")


    sum_Jaccard_EXAM = 0
    sum_Ochiai_EXAM = 0
    sum_Op2_EXAM = 0
    sum_Tarantula_EXAM = 0
    sum_Dstar3_EXAM = 0

    for num_fault_line in range(1, len(list_fault_line)+1):
        f.write("Locate the EXAM score for the " + str(num_fault_line) + "th statement.\n\n")

        Jaccard_rank_m = calcRankm(list_sus_rank_Jaccard, num_fault_line)
        Jaccard_rank_n = calcRankn(list_sus_rank_Jaccard, num_fault_line)
        Jaccard_rank_N = len(list_sus_rank_Jaccard)
        Jaccard_rank = calcRankValue(Jaccard_rank_m, Jaccard_rank_n)
        Jaccard_EXAM = calcEXAM(Jaccard_rank, Jaccard_rank_N)
        f.write("Jaccard_EXAM: " + str(Jaccard_EXAM) + '\n')
        sum_Jaccard_EXAM = sum_Jaccard_EXAM + Jaccard_EXAM

        Ochiai_rank_m = calcRankm(list_sus_rank_Ochiai, num_fault_line)
        Ochiai_rank_n = calcRankn(list_sus_rank_Ochiai, num_fault_line)
        Ochiai_rank_N = len(list_sus_rank_Ochiai)
        Ochiai_rank = calcRankValue(Ochiai_rank_m, Ochiai_rank_n)
        Ochiai_EXAM = calcEXAM(Ochiai_rank, Ochiai_rank_N)
        f.write("Ochiai_EXAM: " + str(Ochiai_EXAM) + '\n')
        sum_Ochiai_EXAM = sum_Ochiai_EXAM + Ochiai_EXAM

        Op2_rank_m = calcRankm(list_sus_rank_Op2, num_fault_line)
        Op2_rank_n = calcRankn(list_sus_rank_Op2, num_fault_line)
        Op2_rank_N = len(list_sus_rank_Op2)
        Op2_rank = calcRankValue(Op2_rank_m, Op2_rank_n)
        Op2_EXAM = calcEXAM(Op2_rank, Op2_rank_N)
        f.write("Op2_EXAM: " + str(Op2_EXAM) + '\n')
        sum_Op2_EXAM = sum_Op2_EXAM + Op2_EXAM

        Tarantula_rank_m = calcRankm(list_sus_rank_Tarantula, num_fault_line)
        Tarantula_rank_n = calcRankn(list_sus_rank_Tarantula, num_fault_line)
        Tarantula_rank_N = len(list_sus_rank_Tarantula)
        Tarantula_rank = calcRankValue(Tarantula_rank_m, Tarantula_rank_n)
        Tarantula_EXAM = calcEXAM(Tarantula_rank, Tarantula_rank_N)
        f.write("Tarantula_EXAM: " + str(Tarantula_EXAM) + '\n')
        sum_Tarantula_EXAM = sum_Tarantula_EXAM + Tarantula_EXAM

        Dstar3_rank_m = calcRankm(list_sus_rank_Dstar3, num_fault_line)
        Dstar3_rank_n = calcRankn(list_sus_rank_Dstar3, num_fault_line)
        Dstar3_rank_N = len(list_sus_rank_Dstar3)
        Dstar3_rank = calcRankValue(Dstar3_rank_m, Dstar3_rank_n)
        Dstar3_EXAM = calcEXAM(Dstar3_rank, Dstar3_rank_N)
        f.write("Dstar3_EXAM: " + str(Dstar3_EXAM) + '\n')
        sum_Dstar3_EXAM = sum_Dstar3_EXAM + Dstar3_EXAM

        f.write("\n\n")

    f.write("Locate the average EXAM score for all of the statements.\n")
    f.write("Jaccard_EXAM: " + str(sum_Jaccard_EXAM / len(list_fault_line)) + '\n')
    f.write("Ochiai_EXAM: " + str(sum_Ochiai_EXAM / len(list_fault_line)) + '\n')
    f.write("Op2_EXAM: " + str(sum_Op2_EXAM / len(list_fault_line)) + '\n')
    f.write("Tarantula_EXAM: " + str(sum_Tarantula_EXAM / len(list_fault_line)) + '\n')
    f.write("Dstar3_EXAM: " + str(sum_Dstar3_EXAM / len(list_fault_line)) + '\n')
    f.close()


if __name__ == "__main__":
    with open("./output/Fault_Record.txt") as f:
        str_fault_record = f.read()
    f.close()
    list_fault_line = []
    list_fault_line_temp = str_fault_record.split("Line ")[1:]
    for fault_line_temp in list_fault_line_temp:
        list_fault_line.append(fault_line_temp.split(": ")[0])
    # print(list_fault_line)

    str_mutant_suspicious_file_root = "./_MBFL_randomization_higher_order_mutant_set/"

    calcEXAMScoreCombine(list_fault_line, str_mutant_suspicious_file_root)
    calcEXAMScoreSet(list_fault_line, str_mutant_suspicious_file_root)
