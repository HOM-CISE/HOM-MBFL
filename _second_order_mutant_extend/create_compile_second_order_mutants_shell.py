
import os
import argparse

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--second_order_mutant_path', action='store',
                        default="./second_order_mutant_extend/result/",
                        dest='second_order_mutant_path',
                        help='Path of storing second-order mutants.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results

if __name__ == "__main__":

    mutation_dir = parserCommad().second_order_mutant_path + "Mutation_source/"
    compile_dir = parserCommad().second_order_mutant_path + "compile/"
    file_name_list = os.listdir(mutation_dir)

    with open("./second_order_mutant_extend/compile_second_order_mutants.sh", "w") as f:
        f.write("")
    f.close()

    f = open("./second_order_mutant_extend/compile_second_order_mutants.sh", "a")

    if not os.path.exists(compile_dir):
        os.mkdir(compile_dir)

    for file_name in file_name_list:
        f.write("gcc " + mutation_dir + file_name + " -o " + compile_dir + file_name + ".exe -lm\n")

    f.close()