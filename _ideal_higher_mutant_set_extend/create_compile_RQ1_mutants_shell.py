
import os
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

    with open("./compile_mutation.sh", "w") as f:
        f.write("")
    f.close()

    for mutant_set_index in range(1, num_mutants_set+1):
        mutation_dir = parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/Mutant_source/"
        compile_dir = parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/compile/"

        file_name_list = os.listdir(mutation_dir)

        f = open("./compile_mutation.sh", "a")

        if not os.path.exists(compile_dir):
            os.mkdir(compile_dir)

        for file_name in file_name_list:
            f.write("gcc " + mutation_dir + file_name + " -o " + compile_dir + file_name + ".exe -lm\n")

        f.close()