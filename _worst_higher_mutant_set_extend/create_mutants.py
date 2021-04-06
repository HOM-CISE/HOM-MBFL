
import os
import os.path
import shutil
import argparse
import util


def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--mutant_root', action='store',
                        default="./_worst_mutant_set/",
                        dest='mutant_root',
                        help='Path of storing worst mutants.')

    parser.add_argument('--defect_source_path', action='store',
                        default="./test_data/defect_root/source/tcas.c",
                        dest='defect_source_path',
                        help='Defect program path.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results


def moveFileto(sourceDir, targetDir):
    '''
    copy file to a new dictionary
    :param sourceDir:
    :param targetDir:
    :return:
    '''

    shutil.copy(sourceDir, targetDir)


def Mutation(filename1, filename2, root1, root2):

    first_file = open(filename1)
    first_data = first_file.readlines()

    s0 = os.path.splitext(filename2)[0]
    s1 = os.path.splitext(filename2)[1]

    index = 0
    for data in first_data:
        index = index + 1
        dirFrom = (root1 + filename2)
        Rename = s0 + "_" + str(index) + s1
        moveFileto(dirFrom, root2+filename2)

        src_file_name = os.path.join(root2, filename2)
        rename_file_name = os.path.join(root2, Rename)
        os.rename(src_file_name, rename_file_name)

        dirTo = root2 + Rename
        f = open(dirTo, 'r+')
        print("create: ", dirTo)

        list_res_record_line = data.split("\n")[0].split("   |||   ")[1:]
        mu_source = []
        for res_record_line in list_res_record_line:
            original_line = int(res_record_line.split("line: ")[1].split("   index:")[0])
            mutant_index = int(res_record_line.split("index: ")[1].split("   original:")[0])
            original = res_record_line.split("original: ")[1].split("   mutated:")[0]
            mutated = res_record_line.split("mutated: ")[1]

            mu_source = f.readlines()
            main_str = mu_source[original_line - 1]
            left_str = main_str[:mutant_index]
            right_str = main_str[mutant_index + len(original):]
            mu_source[original_line - 1] = left_str + mutated + right_str
            f.seek(0, 0)  # Reset the pointer of reading file

        for mu_source_line in mu_source:
            f.writelines(mu_source_line)
        f.close()


if __name__ == "__main__":
    args = parserCommad()
    defect_source_name = args.defect_source_path[util.findIndex(args.defect_source_path, "/")[-1] + 1:]
    defect_source_path = args.defect_source_path[: util.findIndex(args.defect_source_path, "/")[-1] + 1]
    mutant_root = args.mutant_root
    # print(defect_source_name)
    # print(defect_source_path)

    str_mutant_source_path = mutant_root + "Mutant_source/"
    if not os.path.exists(str_mutant_source_path):
        os.mkdir(str_mutant_source_path)

    Mutation(mutant_root+"res_record.txt", defect_source_name,
             defect_source_path, str_mutant_source_path)
