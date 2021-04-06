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

    parser.add_argument('--defect_root_dir', action='store',
                        default="./test_data/defect_root/",
                        dest='defect_root_dir',
                        help='Defect example root dictionary.')

    parser.add_argument('--defect_source_path', action='store',
                        default="./test_data/defect_root/source/tot_info.c",
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

        res_record_line = data.split("line: ")
        res_record_line = res_record_line[1].split("   index: ")

        original_line = int(res_record_line[0])
        res_record_line = res_record_line[1].split("   original: ")

        mut_index = int(res_record_line[0])

        res_record_line = res_record_line[1].split("   mutated: ")
        original = res_record_line[0]
        res_record_line = res_record_line[1].split('\n')
        mutated = res_record_line[0]

        mu_source = f.readlines()
        main_str = mu_source[original_line - 1]
        left_str = main_str[:mut_index]
        right_str = main_str[mut_index + len(original):]
        mu_source[original_line - 1] = left_str + mutated + right_str
        f.seek(0, 0)
        for mu_source_line in mu_source:
            f.writelines(mu_source_line)
        f.close()
        """
        s = data.split("line: ")
        s = s[1].split(" original: ")
        M = int(s[0])
        s = s[1].split("\tmutated: ")
        zc = s[0]
        s = s[1].split('\n')
        rpzc = s[0]

        '''
        with open(r"D:\MBFL\Mutation_source\B1086.c",'r+') as Msource:
            msource = Msource.readlines()
            msource[M-1] = msource[M-1].replace(zc,rpzc)
            print(msource)
            Msource.seek(0,0)
            Msource.writelines(msource)

        '''
        msource = Msource.readlines()
        msource[M - 1] = msource[M - 1].replace(zc, rpzc)
        Msource.seek(0, 0)
        Msource.writelines(msource)
        Msource.close()
        """

if __name__ == "__main__":
    args = parserCommad()
    defect_source_name = args.defect_source_path[util.findIndex(args.defect_source_path, "/")[-1] + 1:]
    defect_source_path = args.defect_source_path[: util.findIndex(args.defect_source_path, "/")[-1] + 1]

    if not os.path.exists(args.defect_root_dir + "Mutation_source/"):
        os.mkdir(args.defect_root_dir + "Mutation_source/")

    Mutation('./output/res_record.txt', defect_source_name,
             defect_source_path, args.defect_root_dir + "Mutation_source/")