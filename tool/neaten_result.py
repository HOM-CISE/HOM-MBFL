####### need_fix #########
path_project = "./schedule2/five_faults/"
fault_number = 5
version_number = 5


print("=======Jaccard==========Jaccard==============Jaccard===========Jaccard============")
######## FOM ##########
for version_index in range(1, 1+version_number):
    path_log = path_project + "v" + str(version_index) + "/output/record_rank_and_EXAM.log"
    f_FOM_path_log = open(path_log, 'r')
    list_path_log = f_FOM_path_log.read().split('\n')
    # print(list_path_log)
    for path_log_line in list_path_log:
        str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
        # print(str_MBFL_type)
        if (str_MBFL_type == "Jaccard"):  #======================================================================================
            # source_line = path_log_line.split("  N:")[1].split("  rank:")[0] #============??????????????????????????????????????
            # print("========", source_line)
            FOM_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
            FOM_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
            FOM_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
            print(FOM_rank, "\t", FOM_same_rank, "\t", FOM_EXAM_score, "\t", end="")

    print()

print("=========================================================================")

######### HOM_entire ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_entire/_entire_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_entire_result = open(path_log, "r")
            list_path_log = f_HOM_entire_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Jaccard"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_entire_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_entire_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_entire_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_entire_rank, "\t", HOM_entire_same_rank, "\t", HOM_entire_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()


print("==============================================")

######## HOM_line_balancing ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_line_balancing/_line_balancing_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_line_balancing_result = open(path_log, "r")
            list_path_log = f_HOM_line_balancing_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Jaccard"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_line_balancing_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_line_balancing_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_line_balancing_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_line_balancing_rank, "\t", HOM_line_balancing_same_rank, "\t", HOM_line_balancing_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()



print("======Ochiai===============Ochiai=======Ochiai===============Ochiai===========")
######## FOM ##########
for version_index in range(1, 1+version_number):
    path_log = path_project + "v" + str(version_index) + "/output/record_rank_and_EXAM.log"
    f_FOM_path_log = open(path_log, 'r')
    list_path_log = f_FOM_path_log.read().split('\n')
    # print(list_path_log)
    for path_log_line in list_path_log:
        str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
        # print(str_MBFL_type)
        if (str_MBFL_type == "Ochiai"):  #======================================================================================
            # source_line = path_log_line.split("  N:")[1].split("  rank:")[0] #============??????????????????????????????????????
            # print("========", source_line)
            FOM_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
            FOM_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
            FOM_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
            print(FOM_rank, "\t", FOM_same_rank, "\t", FOM_EXAM_score, "\t", end="")

    print()

print("=========================================================================")

######### HOM_entire ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_entire/_entire_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_entire_result = open(path_log, "r")
            list_path_log = f_HOM_entire_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Ochiai"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_entire_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_entire_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_entire_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_entire_rank, "\t", HOM_entire_same_rank, "\t", HOM_entire_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()


print("==============================================")

######## HOM_line_balancing ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_line_balancing/_line_balancing_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_line_balancing_result = open(path_log, "r")
            list_path_log = f_HOM_line_balancing_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Ochiai"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_line_balancing_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_line_balancing_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_line_balancing_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_line_balancing_rank, "\t", HOM_line_balancing_same_rank, "\t", HOM_line_balancing_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()





print("====Op2==========Op2========Op2==========Op2========Op2======")
######## FOM ##########
for version_index in range(1, 1+version_number):
    path_log = path_project + "v" + str(version_index) + "/output/record_rank_and_EXAM.log"
    f_FOM_path_log = open(path_log, 'r')
    list_path_log = f_FOM_path_log.read().split('\n')
    # print(list_path_log)
    for path_log_line in list_path_log:
        str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
        # print(str_MBFL_type)
        if (str_MBFL_type == "Op2"):  #======================================================================================
            # source_line = path_log_line.split("  N:")[1].split("  rank:")[0] #============??????????????????????????????????????
            # print("========", source_line)
            FOM_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
            FOM_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
            FOM_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
            print(FOM_rank, "\t", FOM_same_rank, "\t", FOM_EXAM_score, "\t", end="")

    print()

print("=========================================================================")

######### HOM_entire ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_entire/_entire_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_entire_result = open(path_log, "r")
            list_path_log = f_HOM_entire_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Op2"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_entire_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_entire_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_entire_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_entire_rank, "\t", HOM_entire_same_rank, "\t", HOM_entire_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()


print("==============================================")

######## HOM_line_balancing ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_line_balancing/_line_balancing_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_line_balancing_result = open(path_log, "r")
            list_path_log = f_HOM_line_balancing_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Op2"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_line_balancing_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_line_balancing_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_line_balancing_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_line_balancing_rank, "\t", HOM_line_balancing_same_rank, "\t", HOM_line_balancing_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()





print("======Tarantula========Tarantula=========Tarantula===========Tarantula===========")
######## FOM ##########
for version_index in range(1, 1+version_number):
    path_log = path_project + "v" + str(version_index) + "/output/record_rank_and_EXAM.log"
    f_FOM_path_log = open(path_log, 'r')
    list_path_log = f_FOM_path_log.read().split('\n')
    # print(list_path_log)
    for path_log_line in list_path_log:
        str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
        # print(str_MBFL_type)
        if (str_MBFL_type == "Tarantula"):  #======================================================================================
            # source_line = path_log_line.split("  N:")[1].split("  rank:")[0] #============??????????????????????????????????????
            # print("========", source_line)
            FOM_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
            FOM_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
            FOM_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
            print(FOM_rank, "\t", FOM_same_rank, "\t", FOM_EXAM_score, "\t", end="")

    print()

print("=========================================================================")

######### HOM_entire ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_entire/_entire_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_entire_result = open(path_log, "r")
            list_path_log = f_HOM_entire_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Tarantula"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_entire_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_entire_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_entire_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_entire_rank, "\t", HOM_entire_same_rank, "\t", HOM_entire_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()


print("==============================================")

######## HOM_line_balancing ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_line_balancing/_line_balancing_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_line_balancing_result = open(path_log, "r")
            list_path_log = f_HOM_line_balancing_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Tarantula"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_line_balancing_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_line_balancing_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_line_balancing_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_line_balancing_rank, "\t", HOM_line_balancing_same_rank, "\t", HOM_line_balancing_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()




print("=======Dstar3===========Dstar3======Dstar3===========Dstar3=========Dstar3======")
######## FOM ##########
for version_index in range(1, 1+version_number):
    path_log = path_project + "v" + str(version_index) + "/output/record_rank_and_EXAM.log"
    f_FOM_path_log = open(path_log, 'r')
    list_path_log = f_FOM_path_log.read().split('\n')
    # print(list_path_log)
    for path_log_line in list_path_log:
        str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
        # print(str_MBFL_type)
        if (str_MBFL_type == "Dstar3"):  #======================================================================================
            # source_line = path_log_line.split("  N:")[1].split("  rank:")[0] #============??????????????????????????????????????
            # print("========", source_line)
            FOM_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
            FOM_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
            FOM_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
            print(FOM_rank, "\t", FOM_same_rank, "\t", FOM_EXAM_score, "\t", end="")

    print()

print("=========================================================================")

######### HOM_entire ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_entire/_entire_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_entire_result = open(path_log, "r")
            list_path_log = f_HOM_entire_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Dstar3"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_entire_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_entire_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_entire_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_entire_rank, "\t", HOM_entire_same_rank, "\t", HOM_entire_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()


print("==============================================")

######## HOM_line_balancing ############
list_path_set = ["all_HOM",
                 "ideal_HOM",
                 "ideal_second_order_HOM",
                 "ideal_third_order_HOM",
                 "ideal_fourth_order_HOM",
                 "ideal_fifth_order_HOM",
                 "ideal_sixth_order_HOM",
                 "ideal_seventh_order_HOM",
                 "between_HOM",
                 "between_second_order_HOM",
                 "between_third_order_HOM",
                 "between_fourth_order_HOM",
                 "between_fifth_order_HOM",
                 "between_sixth_order_HOM",
                 "between_seventh_order_HOM",
                 "worst_HOM",
                 "worst_second_order_HOM",
                 "worst_third_order_HOM",
                 "worst_fourth_order_HOM",
                 "worst_fifth_order_HOM",
                 "worst_sixth_order_HOM",
                 "worst_seventh_order_HOM",
                 "second_order_HOM",
                 "third_order_HOM",
                 "fourth_order_HOM",
                 "fifth_order_HOM",
                 "sixth_order_HOM",
                 "seventh_order_HOM"]
for version_index in range(1, 1+version_number):
    for path_set in list_path_set:
        path_log = path_project + "v" + str(version_index) + "_line_balancing/_line_balancing_randomization_higher_order_mutant_set/set/" + path_set + "/record_rank_and_EXAM.log"
        try:
            f_HOM_line_balancing_result = open(path_log, "r")
            list_path_log = f_HOM_line_balancing_result.read().split('\n')
            for path_log_line in list_path_log:
                str_MBFL_type = path_log_line.split(":  m:")[0].split("  ")[-1]
                # print(str_MBFL_type)
                if (str_MBFL_type == "Dstar3"):  # ======================================================================================
                    source_line = path_log_line.split("  N:")[1].split("  rank:")[0]
                    HOM_line_balancing_rank = path_log_line.split("  rank:")[1].split("  EXAM:")[0]
                    HOM_line_balancing_same_rank = path_log_line.split("  n:")[1].split("  N:")[0]
                    HOM_line_balancing_EXAM_score = path_log_line.split("  EXAM:")[1].split("  rank_loc:")[0]
                    print(HOM_line_balancing_rank, "\t", HOM_line_balancing_same_rank, "\t", HOM_line_balancing_EXAM_score, "\t", end='')
        except FileNotFoundError:
            for fault_index in range(fault_number):
                print("-\t-\t-\t", end='')
    print()