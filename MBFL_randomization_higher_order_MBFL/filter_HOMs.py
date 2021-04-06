
if __name__ == "__main__":
    f_res_mutant_line_r = open("./_MBFL_randomization_higher_order_mutant_set/res_mutant_line.txt", 'r')
    f_res_execute_mutant_r = open("./_MBFL_randomization_higher_order_mutant_set/res_execute_mutant.txt", 'r')
    f_all_execute_mutant_r = open("./_MBFL_randomization_higher_order_mutant_set/all_execute_mutant.txt", 'r')
    f_res_record_r = open("./_MBFL_randomization_higher_order_mutant_set/res_record.txt", 'r')

    list_mutant_line = f_res_mutant_line_r.readlines()
    dict_order_mutant_num = {}
    for mutant_line_index in range(1, len(list_mutant_line)+1):
        num_mutant_order = len(list_mutant_line[mutant_line_index-1].split(','))
        if dict_order_mutant_num.get(num_mutant_order) == None:
            dict_order_mutant_num[num_mutant_order] = [mutant_line_index]
        else:
            dict_order_mutant_num[num_mutant_order].append(mutant_line_index)

    list_res_execute_mutant = f_res_execute_mutant_r.readlines()
    dict_used_order_mutant_num = {}
    for res_execute_mutant_index in list_res_execute_mutant:
        for item_key in dict_order_mutant_num:
            if int(res_execute_mutant_index) in dict_order_mutant_num[item_key]:
                if dict_used_order_mutant_num.get(item_key) == None:
                    dict_used_order_mutant_num[item_key] = [int(res_execute_mutant_index)]
                else:
                    dict_used_order_mutant_num[item_key].append(int(res_execute_mutant_index))
                break

    every_order_generate_HOMs = 0
    every_order_used_HOMs = 0
    for item_key in dict_order_mutant_num:
        every_order_generate_HOMs = len(dict_order_mutant_num[item_key])
        every_order_used_HOMs = int(every_order_generate_HOMs / 50 * 10)
        if len(dict_used_order_mutant_num[item_key]) > every_order_used_HOMs:
            dict_used_order_mutant_num[item_key] = dict_used_order_mutant_num[item_key][:every_order_used_HOMs]

    # print(dict_used_order_mutant_num)
    # print(len(dict_used_order_mutant_num[2]))

    f_res_execute_mutant_w = open("./_MBFL_randomization_higher_order_mutant_set/res_execute_mutant.txt", 'w')
    f_all_execute_mutant_w = open("./_MBFL_randomization_higher_order_mutant_set/all_execute_mutant.txt", 'w')
    list_res_record = f_res_record_r.readlines()

    is_first_write = True
    for item_key in dict_used_order_mutant_num:
        if not is_first_write:
            f_res_execute_mutant_w.write('\n')
            f_all_execute_mutant_w.write('\n')
        list_res_execute_mutant_write = []
        for item in dict_used_order_mutant_num[item_key]:
            list_res_execute_mutant_write.append(str(item))
        f_res_execute_mutant_w.write("\n".join(list_res_execute_mutant_write).strip())
        list_all_execute_mutant = []
        for item in dict_used_order_mutant_num[item_key]:
            list_all_execute_mutant.append("Mutant_index: " + str(item) + "   Source_" + list_res_record[item-1])
        f_all_execute_mutant_w.write("".join(list_all_execute_mutant).strip())
        is_first_write = False

    f_res_execute_mutant_w.write('\n')
    f_all_execute_mutant_w.write('\n')
    f_res_execute_mutant_r.close()
    f_all_execute_mutant_r.close()
    f_res_record_r.close()
    f_res_mutant_line_r.close()
    f_res_execute_mutant_w.close()
    f_all_execute_mutant_w.close()