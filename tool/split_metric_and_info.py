import os
import shutil

def createDictionarySet(path_HOM_result):
    try:
        shutil.rmtree(path_HOM_result + "/set")
    except FileNotFoundError:
        pass
    try:
        os.mkdir(path_HOM_result + "/set")
        os.mkdir(path_HOM_result + "/set/ideal_HOM")
        os.mkdir(path_HOM_result + "/set/ideal_second_order_HOM")
        os.mkdir(path_HOM_result + "/set/ideal_third_order_HOM")
        os.mkdir(path_HOM_result + "/set/ideal_fourth_order_HOM")
        os.mkdir(path_HOM_result + "/set/ideal_fifth_order_HOM")
        os.mkdir(path_HOM_result + "/set/ideal_sixth_order_HOM")
        os.mkdir(path_HOM_result + "/set/ideal_seventh_order_HOM")
        os.mkdir(path_HOM_result + "/set/between_HOM")
        os.mkdir(path_HOM_result + "/set/between_second_order_HOM")
        os.mkdir(path_HOM_result + "/set/between_third_order_HOM")
        os.mkdir(path_HOM_result + "/set/between_fourth_order_HOM")
        os.mkdir(path_HOM_result + "/set/between_fifth_order_HOM")
        os.mkdir(path_HOM_result + "/set/between_sixth_order_HOM")
        os.mkdir(path_HOM_result + "/set/between_seventh_order_HOM")
        os.mkdir(path_HOM_result + "/set/worst_HOM")
        os.mkdir(path_HOM_result + "/set/worst_second_order_HOM")
        os.mkdir(path_HOM_result + "/set/worst_third_order_HOM")
        os.mkdir(path_HOM_result + "/set/worst_fourth_order_HOM")
        os.mkdir(path_HOM_result + "/set/worst_fifth_order_HOM")
        os.mkdir(path_HOM_result + "/set/worst_sixth_order_HOM")
        os.mkdir(path_HOM_result + "/set/worst_seventh_order_HOM")
        os.mkdir(path_HOM_result + "/set/second_order_HOM")
        os.mkdir(path_HOM_result + "/set/third_order_HOM")
        os.mkdir(path_HOM_result + "/set/fourth_order_HOM")
        os.mkdir(path_HOM_result + "/set/fifth_order_HOM")
        os.mkdir(path_HOM_result + "/set/sixth_order_HOM")
        os.mkdir(path_HOM_result + "/set/seventh_order_HOM")
        os.mkdir(path_HOM_result + "/set/all_HOM")
    except FileExistsError:
        pass


def str2numlist(list_mutant_line):
    list_mutant_line_num = []
    for mutant_line in list_mutant_line:
        mutant_line = mutant_line.strip('\n')
        mutant_line_num = mutant_line.split(",")
        for num_index in range(len(mutant_line_num)):
            mutant_line_num[num_index] = int(mutant_line_num[num_index])
        list_mutant_line_num.append(mutant_line_num)
    return list_mutant_line_num


def createAllHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                 list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    # use list_fault_record_line to filter "ideal", "between" and "worst"

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line)-1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt)-1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt)-1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line)-1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric)-1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric)-1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createIdealSecondHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                           list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line)-1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt)-1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt)-1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line)-1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric)-1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric)-1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createIdealThirdHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createIdealFourthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createIdealFifthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createIdealSixthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createIdealSeventhHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createIdealHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"


    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createBetweenSecondHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createBetweenThirdHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createBetweenFourthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createBetweenFifthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createBetweenSixthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createBetweenSeventhHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createBetweenHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createWorstSecondHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createWorstThirdHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createWorstFourthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createWorstFifthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createWorstSixthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createWorstSeventhHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createWorstHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createSecondHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createThirdHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createFourthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createFifthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createSixthHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


def createSeventhHom(path_HOM, list_fault_record_line, list_res_record_txt, list_mutant_line, list_fault_metric,
                         list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line):
    path_res_fault_version_in = path_HOM + "/res_fault_version.in"
    path_res_original_version_in = path_HOM + "/res_original_version.in"
    path_mutant_line_txt = path_HOM + "/res_mutant_line.txt"
    path_all_execute_mutant_txt = path_HOM + "/all_execute_mutant.txt"
    path_res_execute_mutant_txt = path_HOM + "/res_execute_mutant.txt"
    path_res_record_txt = path_HOM + "/res_record.txt"

    list_mutant_line_num = str2numlist(list_mutant_line)
    list_info_filter_line = []

    # use list_fault_record_line to filter "ideal", "between" and "worst"
    for mutant_line_num in range(len(list_mutant_line_num)):
        # print(list_mutant_line_num[mutant_line_num])
        is_has_fault_line = False
        is_has_true_line = False
        for num in list_mutant_line_num[mutant_line_num]:
            if num in list_fault_record_line:
                is_has_fault_line = True
            else:
                is_has_true_line = True
        if is_has_fault_line and is_has_true_line:
            # is_between
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif is_has_fault_line and (not is_has_true_line):
            # is_ideal
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
        elif (not is_has_fault_line) and is_has_true_line:
            # is_worst
            # print(list_mutant_line_num[mutant_line_num])
            list_info_filter_line.append(mutant_line_num)
            pass
    # print(len(list_info_filter_line))

    # use list_mutant_line to filter "second", "third", "fourth", "fifth", "sixth", "seventh"
    list_info_filter_line_temp = []
    for info_filter_line in list_info_filter_line:
        if len(list_mutant_line_num[info_filter_line]) == 2:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 3:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 4:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 5:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 6:
            pass
        elif len(list_mutant_line_num[info_filter_line]) == 7:
            # print(list_mutant_line_num[info_filter_line])
            list_info_filter_line_temp.append(info_filter_line)
            pass
    list_info_filter_line = list_info_filter_line_temp
    # print(len(list_info_filter_line))

    list_res_record_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_record_txt_temp.append(list_res_record_txt[info_filter_line])
    list_res_record_txt = list_res_record_txt_temp
    list_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_mutant_line_temp.append(list_mutant_line[info_filter_line])
    list_mutant_line = list_mutant_line_temp
    list_fault_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_fault_metric_temp.append(list_fault_metric[info_filter_line])
    list_fault_metric = list_fault_metric_temp
    list_original_metric_temp = []
    for info_filter_line in list_info_filter_line:
        list_original_metric_temp.append(list_original_metric[info_filter_line])
    list_original_metric = list_original_metric_temp
    list_all_execute_mutant_txt_temp = []
    for info_filter_line in list_info_filter_line:
        list_all_execute_mutant_txt_temp.append(list_all_execute_mutant_txt[info_filter_line])
    list_all_execute_mutant_txt = list_all_execute_mutant_txt_temp
    list_res_execute_mutant_line_temp = []
    for info_filter_line in list_info_filter_line:
        list_res_execute_mutant_line_temp.append(list_res_execute_mutant_line[info_filter_line])
    list_res_execute_mutant_line = list_res_execute_mutant_line_temp

    # print(len(list_res_record_txt))
    # print(len(list_mutant_line))
    # print(len(list_fault_metric))
    # print(len(list_original_metric))
    # print(len(list_all_execute_mutant_txt))
    # print(len(list_res_execute_mutant_line))

    # generate the six file.
    f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'w')
    for res_execute_mutant_line_index in range(len(list_res_execute_mutant_line)):
        f_res_execute_mutant_txt.write(str(list_res_execute_mutant_line[res_execute_mutant_line_index]))
        if res_execute_mutant_line_index != len(list_res_execute_mutant_line) - 1:
            f_res_execute_mutant_txt.write('\n')
    f_res_execute_mutant_txt.close()

    f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'w')
    for all_execute_mutant_txt_index in range(len(list_all_execute_mutant_txt)):
        f_all_execute_mutant_txt.write(list_all_execute_mutant_txt[all_execute_mutant_txt_index].strip('\n'))
        if all_execute_mutant_txt_index != len(list_all_execute_mutant_txt) - 1:
            f_all_execute_mutant_txt.write('\n')
    f_all_execute_mutant_txt.close()

    f_res_record_txt = open(path_res_record_txt, 'w')
    for res_record_txt_index in range(len(list_res_record_txt)):
        f_res_record_txt.write(list_res_record_txt[res_record_txt_index].strip('\n'))
        if res_record_txt_index != len(list_res_record_txt) - 1:
            f_res_record_txt.write('\n')
    f_res_record_txt.close()

    f_mutant_line_txt = open(path_mutant_line_txt, 'w')
    for mutant_line_txt_index in range(len(list_mutant_line)):
        f_mutant_line_txt.write(list_mutant_line[mutant_line_txt_index].strip('\n'))
        if mutant_line_txt_index != len(list_mutant_line) - 1:
            f_mutant_line_txt.write('\n')
    f_mutant_line_txt.close()

    f_res_original_version_in = open(path_res_original_version_in, 'w')
    for original_metric_line_index in range(len(list_original_metric)):
        f_res_original_version_in.write(list_original_metric[original_metric_line_index].strip('\n'))
        if original_metric_line_index != len(list_original_metric) - 1:
            f_res_original_version_in.write('\n')
    f_res_original_version_in.close()

    f_res_fault_version_in = open(path_res_fault_version_in, 'w')
    for fault_metric_line_index in range(len(list_fault_metric)):
        f_res_fault_version_in.write(list_fault_metric[fault_metric_line_index].strip('\n'))
        if fault_metric_line_index != len(list_fault_metric) - 1:
            f_res_fault_version_in.write('\n')
    f_res_fault_version_in.close()


if __name__ == "__main__":
    for version_index in range(1, 6):
        print("版本号：" + str(version_index))
        str_faults_number = "five_faults"
        print("错误数量字符串：" + str_faults_number)
        path_HOM_result = "./schedule2/" + str_faults_number + "/v" + str(version_index) + "_line_balancing/_line_balancing_randomization_higher_order_mutant_set"
        # path_HOM_result = "./schedule2/" + str_faults_number + "/v" + str(version_index) + "_entire/_entire_randomization_higher_order_mutant_set"

        path_res_fault_version_in = path_HOM_result + "/res_fault_version.in"
        path_res_original_version_in = path_HOM_result + "/res_original_version.in"
        path_mutant_line_txt = path_HOM_result + "/res_mutant_line.txt"
        path_all_execute_mutant_txt = path_HOM_result + "/all_execute_mutant.txt"
        path_res_execute_mutant_txt = path_HOM_result + "/res_execute_mutant.txt"
        path_res_record_txt = path_HOM_result + "/res_record.txt"
        path_fault_record_txt = "./schedule2/" + str_faults_number + "/v" + str(version_index) + "/output/Fault_Record.txt"

        f_fault_metric = open(path_res_fault_version_in, 'r')
        f_original_metric = open(path_res_original_version_in, 'r')
        f_mutant_line = open(path_mutant_line_txt, 'r')
        f_all_execute_mutant_txt = open(path_all_execute_mutant_txt, 'r')
        f_res_execute_mutant_txt = open(path_res_execute_mutant_txt, 'r')
        f_res_record_txt = open(path_res_record_txt, 'r')
        f_fault_record = open(path_fault_record_txt, 'r')

        list_fault_metric = f_fault_metric.readlines()
        list_original_metric = f_original_metric.readlines()
        list_mutant_line = f_mutant_line.readlines()
        list_all_execute_mutant_txt = f_all_execute_mutant_txt.readlines()
        list_res_execute_mutant_txt = f_res_execute_mutant_txt.readlines()
        list_res_record_txt = f_res_record_txt.readlines()
        list_fault_record = f_fault_record.readlines()

        list_res_execute_mutant_line = []
        for line in list_res_execute_mutant_txt:
            list_res_execute_mutant_line.append(int(line.split('\n')[0]))
        list_fault_record_line = []
        for line in list_fault_record:
            list_fault_record_line.append(int(line.split(":   Original:")[0].split("Line ")[1]))

        f_fault_metric.close()
        f_original_metric.close()
        f_mutant_line.close()
        f_all_execute_mutant_txt.close()
        f_res_execute_mutant_txt.close()
        f_res_record_txt.close()
        f_fault_record.close()

        print("可运行的变异体序号为：", list_res_execute_mutant_line)
        print("错误行为: ", list_fault_record_line)

        # 整理待分解输出的6个文件内容list
        list_res_record_txt_temp = []
        for res_execute_mutant_line in list_res_execute_mutant_line:
            list_res_record_txt_temp.append(list_res_record_txt[res_execute_mutant_line - 1])
        list_res_record_txt = list_res_record_txt_temp

        list_mutant_line_temp = []
        for res_execute_mutant_line in list_res_execute_mutant_line:
            list_mutant_line_temp.append(list_mutant_line[res_execute_mutant_line - 1])
        list_mutant_line = list_mutant_line_temp

        list_fault_metric = list_fault_metric
        list_original_metric = list_original_metric
        list_all_execute_mutant_txt = list_all_execute_mutant_txt
        list_res_execute_mutant_line = list_res_execute_mutant_line

        # print(len(list_res_record_txt))
        # print(len(list_mutant_line))
        # print(len(list_fault_metric))
        # print(len(list_original_metric))
        # print(len(list_all_execute_mutant_txt))
        # print(len(list_res_execute_mutant_line))

        # 对每一类文件夹中都保留六个文件(对每个文件夹单写函数实现)，方便后续的计算。
        createDictionarySet(path_HOM_result)
        createAllHom(path_HOM_result+"/set/all_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                     list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createIdealSecondHom(path_HOM_result+"/set/ideal_second_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createIdealThirdHom(path_HOM_result+"/set/ideal_third_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createIdealFourthHom(path_HOM_result+"/set/ideal_fourth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createIdealFifthHom(path_HOM_result+"/set/ideal_fifth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createIdealSixthHom(path_HOM_result+"/set/ideal_sixth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createIdealSeventhHom(path_HOM_result+"/set/ideal_seventh_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createIdealHom(path_HOM_result+"/set/ideal_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createBetweenSecondHom(path_HOM_result+"/set/between_second_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createBetweenThirdHom(path_HOM_result+"/set/between_third_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createBetweenFourthHom(path_HOM_result+"/set/between_fourth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createBetweenFifthHom(path_HOM_result+"/set/between_fifth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createBetweenSixthHom(path_HOM_result+"/set/between_sixth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createBetweenSeventhHom(path_HOM_result+"/set/between_seventh_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createBetweenHom(path_HOM_result+"/set/between_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createWorstSecondHom(path_HOM_result+"/set/worst_second_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createWorstThirdHom(path_HOM_result+"/set/worst_third_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createWorstFourthHom(path_HOM_result+"/set/worst_fourth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createWorstFifthHom(path_HOM_result+"/set/worst_fifth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createWorstSixthHom(path_HOM_result+"/set/worst_sixth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createWorstSeventhHom(path_HOM_result+"/set/worst_seventh_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createWorstHom(path_HOM_result+"/set/worst_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createSecondHom(path_HOM_result+"/set/second_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createThirdHom(path_HOM_result+"/set/third_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createFourthHom(path_HOM_result+"/set/fourth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createFifthHom(path_HOM_result+"/set/fifth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createSixthHom(path_HOM_result+"/set/sixth_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
        createSeventhHom(path_HOM_result+"/set/seventh_order_HOM", list_fault_record_line, list_res_record_txt, list_mutant_line,
                             list_fault_metric, list_original_metric, list_all_execute_mutant_txt, list_res_execute_mutant_line)
