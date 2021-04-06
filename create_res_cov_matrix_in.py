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
    gcov_dir = parserCommad().defect_root_dir + "gcov/"
    file_name_list = os.listdir(gcov_dir)
    file_name = file_name_list[0]
    replace_index = util.findIndex(file_name, ".")
    file_name = file_name[:replace_index[-1]]

    file_number = len(file_name_list)

    with open("./output/res_cov_matrix.in", 'w') as f :
        f.write("")   # create and clean res_record.txt
        f.close()
    f = open("./output/res_cov_matrix.in", 'a')

    for i in range(file_number):
        file_temp_name = file_name + "." + str(i+1)
        with open(gcov_dir + file_temp_name, "r") as fp:
            gcov_list = fp.readlines()[5:]
        fp.close()

        for line in gcov_list:
            ch = line.split(":")[0][-1]
            if ch == '-':
                f.write("2")
            elif ch == '#':
                f.write("0")
            else:
                f.write("1")

        f.write("\n")

