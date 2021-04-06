import os
import argparse

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--mutant_root', action='store',
                        default="./_line_balancing_randomization_higher_order_mutant_set/",
                        dest='mutant_root',
                        help='mutant root dictionary.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results

if __name__ == "__main__":

    mutant_root = parserCommad().mutant_root

    with open("./compile_mutation.sh", "w") as f:
        f.write("")
    f.close()

    mutation_dir = "./_line_balancing_randomization_higher_order_mutant_set/Mutation_source/"
    compile_dir = "./_line_balancing_randomization_higher_order_mutant_set/compile/"

    file_name_list = os.listdir(mutation_dir)

    f = open("./compile_mutation.sh", "a")

    if not os.path.exists(compile_dir):
        os.mkdir(compile_dir)

    for file_name in file_name_list:
        f.write("gcc " + mutation_dir + file_name + " -o " + compile_dir + file_name + ".exe -lm\n")

    f.close()