import argparse
import json
import util

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser(description="Use res_vector.in and res_cov_matrix.in to generate res_record.txt")

    parser.add_argument('--defect_source_path', action='store',
                        default="./test_data/defect_root/source/tot_info.c",
                        dest='defect_source_path',
                        help='Defect program path.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 2.0')

    results = parser.parse_args()

    return results


def readSource(source_path):
    '''
    read the source file.

    :return: a list of sources, the element type of the list is "str".
    '''

    f = open(source_path, "r")
    source_str = f.read()
    f.close()
    source_line_list = source_str.split('\n')
    return source_line_list


def getMutantOperator():
    '''
    read the mutant operator

    :return: a dict including mutant operator
    '''
    with open("mutation_operator_no_space.json", 'r') as f :
        s = f.read()
    f.close()
    return json.loads(s)


if __name__ == "__main__":

    # read the source file
    source_list = readSource(parserCommad().defect_source_path)

    # read mutant operator
    mutant_opt = getMutantOperator()

    with open("./output/res_vector.in", "r") as f:
        res_vector_in = f.read()
    f.close()

    with open("./output/res_cov_matrix.in") as f:
        res_cov_matrix_in = f.read()
        res_cov_matrix_in_list = res_cov_matrix_in.split("\n")
    f.close()

    failed_input_index_list = []
    for i in range(len(res_vector_in)):
        if res_vector_in[i] is '1':
            failed_input_index_list.append(i)

    mutant_line_list = []
    for failed_input_index in failed_input_index_list:
        for index, cov_line_type in enumerate(res_cov_matrix_in_list[failed_input_index], start=1):
            if cov_line_type is "1":
                if index not in mutant_line_list:
                    mutant_line_list.append(index)
    mutant_line_list.sort()

    # to find and write all the feasible operator
    with open("./output/res_record.txt", 'w') as f :
        f.write("")   # create and clean res_record.txt
        f.close()

    f = open("./output/res_record.txt", 'a')
    for line_index in mutant_line_list:
        source_line = source_list[line_index-1]
        for key in mutant_opt:
            if util.isFind(source_line, key):
                for value in mutant_opt[key]:
                    for loc in util.findIndex(source_line, key):
                        f.write("line: " + str(line_index) + "   index: " + str(loc)
                                + "   original: " + key + "   mutated: " + value + '\n')

