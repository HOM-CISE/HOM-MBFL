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
重命名输入文件名（替换特殊字符）
'''
def inputs_file_raname(path):
    file_list = os.listdir(path)
    for file_name in file_list:
        new_file_name = file_name.replace(" ","a0x20")
        new_file_name = new_file_name.replace("!", "a0x21")
        new_file_name = new_file_name.replace("\"", "a0x22")
        new_file_name = new_file_name.replace("#", "a0x23")
        new_file_name = new_file_name.replace("$", "a0x24")
        new_file_name = new_file_name.replace("%", "a0x25")
        new_file_name = new_file_name.replace("&", "a0x26")
        new_file_name = new_file_name.replace("\'", "a0x27")
        new_file_name = new_file_name.replace("(", "a0x28")
        new_file_name = new_file_name.replace(")", "a0x29")
        new_file_name = new_file_name.replace("*", "a0x2A")
        new_file_name = new_file_name.replace("+", "a0x2B")
        new_file_name = new_file_name.replace(",", "a0x2C")
        new_file_name = new_file_name.replace("-", "a0x2D")
        new_file_name = new_file_name.replace("/", "a0x2F")
        new_file_name = new_file_name.replace(":", "a0x3A")
        new_file_name = new_file_name.replace(";", "a0x3B")
        new_file_name = new_file_name.replace("<", "a0x3C")
        new_file_name = new_file_name.replace("=", "a0x3D")
        new_file_name = new_file_name.replace(">", "a0x3E")
        new_file_name = new_file_name.replace("?", "a0x3F")
        new_file_name = new_file_name.replace("@", "a0x40")
        new_file_name = new_file_name.replace("[", "a0x5B")
        new_file_name = new_file_name.replace("\\", "a0x5C")
        new_file_name = new_file_name.replace("]", "a0x5D")
        new_file_name = new_file_name.replace("^", "a0x5E")
        new_file_name = new_file_name.replace("_", "a0x5F")
        new_file_name = new_file_name.replace("`", "a0x60")
        new_file_name = new_file_name.replace("{", "a0x7B")
        new_file_name = new_file_name.replace("|", "a0x7C")
        new_file_name = new_file_name.replace("}", "a0x7D")
        new_file_name = new_file_name.replace("~", "a0x7E")

        os.rename(path + file_name, path + new_file_name)


if __name__ == "__main__":
    inputs_dir = parserCommad().inputs_dir
    inputs_file_raname(inputs_dir)
