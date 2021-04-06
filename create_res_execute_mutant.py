import os
import util
import argparse

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--defect_root_dir', action='store',
                        default="./test_data/defect_root/",
                        dest='defect_root_dir',
                        help='Defect example root dictionary.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results

if __name__ == "__main__":

    compile_dir = parserCommad().defect_root_dir + "compile/"
    file_name_list = os.listdir(compile_dir)
    file_name = file_name_list[0]
    replace_index = util.findIndex(file_name, "_")
    file_name = file_name[:replace_index[-1]]

    mutation_dir = parserCommad().defect_root_dir + "Mutation_source/"
    mutation_file_list = os.listdir(mutation_dir)
    mutation_file_number = len(mutation_file_list)

    with open("./output/res_execute_mutant.txt", 'w') as f :
        f.write("")   # create and clean res_record.txt
        f.close()
    f = open("./output/res_execute_mutant.txt", 'a')

    for i in range(mutation_file_number):
        file_temp_name = file_name + "_" +str(i+1) + ".c.exe"
        if file_temp_name in file_name_list:
            f.write(str(i+1)+"\n")

    f.close()
