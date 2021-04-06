
import os
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

    mutation_dir = parserCommad().defect_root_dir + "Mutation_source/"
    compile_dir = parserCommad().defect_root_dir + "compile/"
    file_name_list = os.listdir(mutation_dir)

    with open("./compile_mutation.sh", "w") as f:
        f.write("")
    f.close()

    f = open("./compile_mutation.sh", "a")

    if not os.path.exists(compile_dir):
        os.mkdir(compile_dir)

    for file_name in file_name_list:
        f.write("gcc " + mutation_dir + file_name + " -o " + compile_dir + file_name + ".exe -lm\n")

    f.close()