import argparse

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser(description="create second order mutants record based on first order mutant suspicious file.")

    parser.add_argument('--first_order_mutant_suspicious_file', action='store',
                        default="../output/suspicious_first_order_Dstar3.txt",
                        dest='first_order_mutant_suspicious_file',
                        help='the path of file recorded all first order mutants suspicious.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results


def readSuspiciousFile(first_order_mutant_suspicious_file):
    list_first_order_information = []
    with open(first_order_mutant_suspicious_file, 'r') as f:
        list_first_order_information = f.read().splitlines()
    f.close()
    return list_first_order_information


def filterFirstOrderMutant(list_first_order_information):
    # filter a max suspicious line of each line.

    list_second_order_information = []
    list_filter_mutants = []

    for item_index in range(len(list_first_order_information)):

        suspicious_now_item = list_first_order_information[item_index].split("_sus:")[1].split("   Mutant_index:")[0]
        source_line_now_item = list_first_order_information[item_index].split("Source_line: ")[1].split("   index:")[0]

        if len(list_filter_mutants) == 0:
            list_filter_mutants.append((item_index, suspicious_now_item, source_line_now_item))
            continue

        if source_line_now_item == list_filter_mutants[-1][2]: # if now mutant has the same line of the last of filtered mutants
            if suspicious_now_item > list_filter_mutants[-1][1]: # update mutant if now mutant has higher suspicious than the last of filtered mutants
                list_filter_mutants[-1] = (item_index, suspicious_now_item, source_line_now_item)
        else:
            list_filter_mutants.append((item_index, suspicious_now_item, source_line_now_item))


    # Use two first-order mutants to combine a second-order mutant
    for line_index_a in range(len(list_filter_mutants)):
        for line_index_b in range(len(list_filter_mutants)):
            if line_index_b >= line_index_a:
                break
            list_second_order_information.append(list_first_order_information[list_filter_mutants[line_index_a][0]]
                                                 + "   |||||   "
                                                 + list_first_order_information[list_filter_mutants[line_index_b][0]])

    return list_second_order_information


def writeSecondOrderMutantsRecord(list_second_order_information):
    with open("./second_order_mutant_extend/result/logs/second_order_mutants_record.txt", 'w') as f:
        f.write("")
    f.close()

    with open("./second_order_mutant_extend/result/logs/second_order_mutants_record.txt", 'w') as f:
        for line in list_second_order_information:
            f.write(line+'\n')
    f.close()

if __name__ == "__main__":

    # read the first order mutant suspicious file
    list_first_order_information = readSuspiciousFile(parserCommad().first_order_mutant_suspicious_file)

    # filter first order mutant information to combine second order mutants
    list_second_order_information = filterFirstOrderMutant(list_first_order_information)

    # write down the information about second order mutant information
    writeSecondOrderMutantsRecord(list_second_order_information)
