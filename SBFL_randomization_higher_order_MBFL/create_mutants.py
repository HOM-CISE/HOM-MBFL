
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
                        default="../_SBFL_randomization_higher_order_mutant_set/",
                        dest='mutant_root',
                        help='Path of storing mutants.')

    parser.add_argument('--defect_source_path', action='store',
                        default="../test_data/defect_root/source/tcas.c",
                        dest='defect_source_path',
                        help='Defect program path.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results


def copyFileto(sourceDir, targetDir):
    '''
    copy file to a new dictionary
    :param sourceDir:
    :param targetDir:
    :return:
    '''

    shutil.copy(sourceDir, targetDir)


def Mutation(str_path_res_record, defect_source_name, defect_source_path, str_mutant_source_path):

    f_res_record = open(str_path_res_record)
    list_res_record = f_res_record.readlines()

    str_file_name = os.path.splitext(defect_source_name)[0]
    str_file_extend_name = os.path.splitext(defect_source_name)[1]

    index = 0
    for str_res_record in list_res_record:
        index = index + 1
        dirFrom = (defect_source_path + defect_source_name)
        Rename = str_file_name + "_" + str(index) + str_file_extend_name
        copyFileto(dirFrom, str_mutant_source_path+defect_source_name)

        src_file_name = os.path.join(str_mutant_source_path, defect_source_name)
        rename_file_name = os.path.join(str_mutant_source_path, Rename)
        os.rename(src_file_name, rename_file_name)

        dirTo = str_mutant_source_path + Rename
        f = open(dirTo, 'r+')
        print("create: ", dirTo)

        list_res_record_line = str_res_record.split("\n")[0].split("   |||   ")[1:]
        # print(list_res_record_line)

        mu_source = []
        mu_source = f.readlines()
        for res_record_line in list_res_record_line:
            original_line = int(res_record_line.split("line: ")[1].split("   index:")[0])
            mutant_index = int(res_record_line.split("index: ")[1].split("   original:")[0])
            original = res_record_line.split("original: ")[1].split("   mutated:")[0]
            mutated = res_record_line.split("mutated: ")[1]

            main_str = mu_source[original_line - 1]
            left_str = main_str[:mutant_index]
            right_str = main_str[mutant_index+len(original):]
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

    str_mutant_source_path = mutant_root + "Mutation_source/"
    if not os.path.exists(str_mutant_source_path):
        os.mkdir(str_mutant_source_path)

    Mutation(mutant_root+"res_record.txt", defect_source_name,
             defect_source_path, str_mutant_source_path)
