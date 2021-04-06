import math
import random
import time

file_res_record = ""

def _createResRecord(list_mutant_line, dict_mutant_information, file_res_record_temp):
    global file_res_record
    if len(list_mutant_line) == 0:
        file_res_record = file_res_record + file_res_record_temp + '\n'
        return

    for mutant_item in dict_mutant_information[list_mutant_line[0]]:
        file_res_record_line = file_res_record_temp + "   |||   "
        file_res_record_line = file_res_record_line + mutant_item
        list_mutant_line_copy = list_mutant_line.copy()[1:]
        _createResRecord(list_mutant_line_copy, dict_mutant_information, file_res_record_line)


def createResRecord(list_res_mutant_line, dict_mutant_information):
    # print(list_res_mutant_line)
    global file_res_record
    file_res_record = ""

    for res_mutant_line in list_res_mutant_line:
        list_mutant_line = res_mutant_line.split(',')

        if len(list_mutant_line) > 1:
            # Randomly select the mutants for each mutable line, and limit the number mutants of each mutant set is lower than max_num_mutant.
            # max_mutant_num = 10001 ################################(Modifiable configuration)###########################
            # select_mutant_line_num = int(math.pow((max_mutant_num / len(list_res_mutant_line)), 1/len(list_mutant_line)))
            select_mutant_line_num = 1  # force 1
            if select_mutant_line_num < 1:
                select_mutant_line_num = 1
                # print("max_mutant_num is greater than " + str(max_mutant_num) + ", max_mutant_num is " + str(len(list_mutant_line)))

            dict_mutant_information_new = {}
            for mutant_line in list_mutant_line:
                list_select_mutant_index = []
                for select_mutant_line_index in range(select_mutant_line_num):
                    list_select_mutant_index.append(random.randint(0, len(dict_mutant_information[mutant_line])-1))

                dict_mutant_information_new[mutant_line] = []
                for select_mutant_index in list_select_mutant_index:
                    dict_mutant_information_new[mutant_line].append(dict_mutant_information[mutant_line][select_mutant_index])

            # for key in dict_mutant_information_new:
            #     print(key + ":")
            #     for item in dict_mutant_information_new[key]:
            #         print(item)

            _createResRecord(list_mutant_line, dict_mutant_information_new, "")
        else:
            _createResRecord(list_mutant_line, dict_mutant_information, "")


if __name__ == "__main__":
    # 1.read the file of "./output/res_record.txt", use a dictionary to save mutants' information.
    # And record all of the mutable line-index as key.
    with open("./output/res_record.txt", 'r') as f:
        str_res_record = f.read()
    f.close()
    dict_mutant_information = {}
    list_res_record_line = str_res_record.split('\n')[:-1]
    for res_record_line in list_res_record_line:
        line_index = res_record_line.split("line: ")[1].split("   index: ")[0]
        if dict_mutant_information.get(line_index) == None:
            dict_mutant_information[line_index] = []
            dict_mutant_information[line_index].append(res_record_line)
        else:
            dict_mutant_information[line_index].append(res_record_line)
    # for temp in dict_mutant_information.keys():
    #     print(temp)
    #     for item in dict_mutant_information[temp]:
    #         print(dict_mutant_information[temp])
    #         break
    #         print()
    #     print()
    #     print()
    #     print()

    # for key in dict_mutant_information:
    #     print(key + ":")
    #     for item in dict_mutant_information[key]:
    #         print(item)


    # 2.read all mutant sets' "res_mutant_line.txt" to generate "res_record.txt".
    with open("./_entire_randomization_higher_order_mutant_set/res_mutant_line.txt", 'r') as f:
        list_res_mutant_line = f.read().split('\n')
    f.close()
    createResRecord(list_res_mutant_line, dict_mutant_information)
    with open("./_entire_randomization_higher_order_mutant_set/res_record.txt", 'w') as f:
        f.write(file_res_record)
    f.close()