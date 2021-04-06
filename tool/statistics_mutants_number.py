str_project_name = "schedule2"
list_version = range(1, 6)
str_fault_nums = "five_faults"

def str2numlist(list_mutant_line):
    list_mutant_line_num = []
    for mutant_line in list_mutant_line:
        mutant_line = mutant_line.strip('\n')
        mutant_line_num = mutant_line.split(",")
        for num_index in range(len(mutant_line_num)):
            mutant_line_num[num_index] = int(mutant_line_num[num_index])
        list_mutant_line_num.append(mutant_line_num)
    return list_mutant_line_num

if __name__ == "__main__":
    for version_index in list_version:
        path_FOM_version_result = "./" + str_project_name + "/" + str_fault_nums + "/v" + str(version_index) + "/output/"

        with open(path_FOM_version_result + "all_res_record.txt") as f_all_mutants:
            print(str(len(f_all_mutants.readlines())), "\t", end="")
            f_all_mutants.close()
        with open(path_FOM_version_result + "res_record.txt") as f_res_record:
            list_res_record = f_res_record.readlines()
            print(str(len(list_res_record)), "\t", end="")
            f_res_record.close()
        with open(path_FOM_version_result + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()


        path_HOM_version_result = "./" + str_project_name + "/" + str_fault_nums + "/v" + str(version_index) + "_entire/_entire_randomization_higher_order_mutant_set/"

        with open(path_HOM_version_result + "res_record.txt") as f_HOM_res_record:
            print(str(len(f_HOM_res_record.readlines())), "\t", end="")
            f_HOM_res_record.close()
        with open(path_HOM_version_result + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print(str(len(list_res_record)), "\t", end="")
        with open(path_HOM_version_result + "set/second_order_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print(str(len(list_res_record)), "\t", end="")
        with open(path_HOM_version_result + "set/third_order_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print(str(len(list_res_record)), "\t", end="")
        with open(path_HOM_version_result + "set/fourth_order_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print(str(len(list_res_record)), "\t", end="")
        with open(path_HOM_version_result + "set/fifth_order_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print(str(len(list_res_record)), "\t", end="")
        with open(path_HOM_version_result + "set/sixth_order_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print(str(len(list_res_record)), "\t", end="")
        with open(path_HOM_version_result + "set/seventh_order_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        path_fault_record_txt = "./" + str_project_name + "/" + str_fault_nums + "/v" + str(version_index) + "/output/Fault_Record.txt"
        f_fault_record = open(path_fault_record_txt, 'r')
        list_fault_record = f_fault_record.readlines()
        list_fault_record_line = []
        for line in list_fault_record:
            list_fault_record_line.append(int(line.split(":   Original:")[0].split("Line ")[1]))

        path_mutant_line_txt = path_HOM_version_result + "/res_mutant_line.txt"
        f_HOM_mutant_line = open(path_mutant_line_txt, 'r')
        list_mutant_line = f_HOM_mutant_line.readlines()
        f_HOM_mutant_line.close()
        list_filter_line_ideal = []
        list_filter_line_between = []
        list_filter_line_worst = []
        list_mutant_line_num = str2numlist(list_mutant_line)
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
                list_filter_line_between.append(mutant_line_num)
                pass
            elif is_has_fault_line and (not is_has_true_line):
                # is_ideal
                list_filter_line_ideal.append(mutant_line_num)
                pass
            elif (not is_has_fault_line) and is_has_true_line:
                # is_worst
                list_filter_line_worst.append(mutant_line_num)
                pass

        print(str(len(list_filter_line_ideal)), "\t", end="")
        with open(path_HOM_version_result + "set/ideal_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print(str(len(list_filter_line_between)), "\t", end="")
        with open(path_HOM_version_result + "set/between_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print(str(len(list_filter_line_worst)), "\t", end="")
        with open(path_HOM_version_result + "set/worst_HOM/" + "all_execute_mutant.txt") as f_all_execute_mutants:
            print(str(len(f_all_execute_mutants.readlines())), "\t", end="")
            f_res_record.close()

        print()