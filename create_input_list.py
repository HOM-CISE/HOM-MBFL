import os
import argparse

'''
Get the command line parameter and return them.
参数列表:
--inputs_dir 测试用例存放路径
--version 代码版本
'''
def parserCommad():
    parser = argparse.ArgumentParser()

    parser.add_argument('--inputs_dir', action='store',
                        default='./test_data/inputs/',
                        dest='inputs_dir',
                        help='test cases dictionary.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.1')

    results = parser.parse_args()
    return results


'''
获取 --inputs_dir 参数对应目录下所有的测试用例，并生成文件列表
'''
if __name__ == "__main__":
    inputs_dir = parserCommad().inputs_dir
    paths = []
    for dirpath, dirnames, filenames in os.walk(inputs_dir):
        for filepath in filenames:
            paths.append(os.path.join(filepath))

    # create input_list.txt
    with open("./output/input_list.txt", 'w') as f :
        f.write("")   # create and clean res_record.txt

    f = open("./output/input_list.txt", 'a')
    for input_path in paths:
        f.write(str(input_path)+"\n")

    f.close()