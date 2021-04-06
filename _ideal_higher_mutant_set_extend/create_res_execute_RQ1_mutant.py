import os
import util
import argparse

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--RQ1_mutant_path', action='store',
                        default="./_RQ1_mutant_set/",
                        dest='RQ1_mutant_path',
                        help='RQ1 mutant root dictionary.')

    parser.add_argument('--num_mutants_set', action='store',
                        dest='num_mutants_set',
                        type=int,
                        default=5,
                        help='number of mutants sets.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results

if __name__ == "__main__":

    num_mutants_set = parserCommad().num_mutants_set

    for mutant_set_index in range(1, num_mutants_set+1):
        compile_dir = parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/compile/"
        file_name_list = os.listdir(compile_dir)
        file_name = file_name_list[0]
        replace_index = util.findIndex(file_name, "_")
        file_name = file_name[:replace_index[-1]]

        mutation_dir = parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/Mutant_source/"
        mutation_file_list = os.listdir(mutation_dir)
        mutation_file_number = len(mutation_file_list)

        with open(parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/res_execute_mutant.txt", 'w') as f :
            f.write("")   # create and clean res_record.txt
            f.close()
        f = open(parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/res_execute_mutant.txt", 'a')

        for i in range(mutation_file_number):
            file_temp_name = file_name + "_" +str(i+1) + ".c.exe"
            if file_temp_name in file_name_list:
                f.write(str(i+1)+"\n")

        f.close()
