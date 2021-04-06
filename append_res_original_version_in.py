import util
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

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results


if __name__ == "__main__":
    output_path1 = "./temp_outputs/"
    output_path2 = parserCommad().true_root_dir + "outputs/"
    input_list = []
    with open("./output/input_list.txt", "r") as f:
        input_list = f.read().split("\n")[:-1]
    f.close()

    f = open("./output/res_original_version.in", "a")
    for input_sample in input_list:
        try:
            if util.isFileEqual(output_path1 + input_sample +".out", output_path2 + input_sample +".out"):
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