# compare two Document
from util import isFileEqual
import argparse

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--true_root_dir', action='store',
                        default="./test_data/true_root/",
                        dest='true_root_dir',
                        help='True example root dictionary.')

    parser.add_argument('--defect_root_dir', action='store',
                        default="./test_data/defect_root/",
                        dest='defect_root_dir',
                        help='Defect example root dictionary.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results


if __name__ == '__main__':

    true_outputs_list = []
    defect_outputs_list = []
    input_path_list = []
    with open("./output/input_list.txt", 'r') as f:
        input_path_list = f.read().split("\n")[:-1]
    f.close()
    
### use input_path_list replace outputs_list
    true_outputs_dir = parserCommad().true_root_dir + "outputs/"    # the path of true outputs
    for input_path in input_path_list:
        true_outputs_list.append(true_outputs_dir + input_path + ".out")
    
    defect_root_dir = parserCommad().defect_root_dir + "outputs/"   # the path of defect outputs
    for input_path in input_path_list:
        defect_outputs_list.append(defect_root_dir + input_path + ".out")

    # we think the number of .txt in output1 is equal in output2
    with open("./output/res_vector.in", 'w') as f :
        f.write("")   # create and clean res_record.txt
    f.close()
	
    f = open("./output/res_vector.in", 'a')
    
    for true_outputs_path, defect_outputs_path in zip(true_outputs_list, defect_outputs_list):
        try:
            if isFileEqual(true_outputs_path, defect_outputs_path):
                f.write("0")
            else:
                f.write("1")
        except MemoryError:
            f.write("1")
        except FileNotFoundError:
            f.write("1")
        except UnicodeError:
            f.write("1")
    
    f.write("\n")
    f.close()
