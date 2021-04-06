import argparse
import util

'''
Get the command line parameter and return them.
参数列表:
--inputs_dir 测试用例存放路径
--inputs_type 测试用例类型（文件[file]或参数[args]类型）
--defect_root_dir 缺陷程序根目录
--defect_source_path 缺陷源代码路径
--timeout 判断程序运行超时，并终止运行程序的阈值
--version 代码版本
'''
def parserCommad():
    parser = argparse.ArgumentParser()

    parser.add_argument('--inputs_dir', action='store',
                        default='./test_data/inputs/',
                        dest='inputs_dir',
                        help='test cases dictionary.')

    parser.add_argument('--inputs_type', action='store',
                        default="file",
                        dest='inputs_type',
                        help="test cases type. [file] or [args]")

    parser.add_argument('--defect_root_dir', action='store',
                        default="./test_data/defect_root/",
                        dest='defect_root_dir',
                        help='Defect example root dictionary.')

    parser.add_argument('--defect_source_path', action='store',
                        default="./test_data/defect_root/source/tot_info.c",
                        dest="defect_source_path",
                        help='Defect program path.')

    parser.add_argument('--timeout', action='store',
                        dest='timeout',
                        type=int,
                        default=30,
                        help="run time limit of every program.")

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.2')

    results = parser.parse_args()

    return results


def createRunDefectSourceScriptFileMode(defect_root_dir, defect_source_path, timeout, inputs_dir):

    f = open("./output/input_list.txt", 'r')
    input_paths = f.read().split("\n")[:-1]
    f.close()

    f = open(defect_root_dir + "run_cov.sh", "w")
    f.writelines("rm -rf " + defect_root_dir + "gcov\nmkdir " + defect_root_dir + "gcov\nmkdir " + defect_root_dir + "outputs\n")
    f.writelines("gcc -fprofile-arcs -ftest-coverage " + defect_source_path + " -o " + defect_source_path + ".exe -lm\n")
    source_file_name = defect_source_path[ util.findIndex(defect_source_path, "/")[-1]+1 : util.findIndex(defect_source_path, ".")[-1] ]
    f.writelines("mv " + source_file_name + ".gcno " + defect_source_path + ".gcno\n\n")

    for i in range(len(input_paths)):
        command = 'echo ">>>>>>>>running test ' + str(i+1) + '"\n'
        f.writelines(command)
        command = "timeout "  + str(timeout) + " " \
              + defect_source_path +".exe < " \
              + inputs_dir + input_paths[i] +" > "\
              + defect_root_dir + "outputs/" + input_paths[i]+".out\n" \
              + "mv " + source_file_name + ".gcda " + defect_source_path + ".gcda\n" \
              + "gcov " + defect_source_path + ".exe" \
              + "\nmv " + source_file_name + ".c.gcov " \
              + defect_root_dir + "gcov/" + source_file_name \
              + ".gcov." + str(i+1) + "\n\n"

        f.writelines(command)
    f.writelines("rm " + defect_source_path + ".gcno\n")
    f.writelines("rm " + defect_source_path + ".gcda\n")
    f.close()


def createRunDefectSourceScriptArgsMode(defect_root_dir, defect_source_path, timeout, inputs_dir):

    # 获取测试用例文件列表
    f = open("./output/input_list.txt", 'r')
    input_paths = f.read().split("\n")[:-1]
    f.close()

    # 打开所有测试用例文件，读取文件内的参数
    list_input_args = []
    for i in range(len(input_paths)):
        f = open(inputs_dir + input_paths[i], 'r')
        input_args = f.read()
        list_input_args.append(input_args)
        f.close()

    # 生成运行缺陷源代码的run_cov.sh脚本
    f = open(defect_root_dir + "run_cov.sh", "w")
    f.writelines("rm -rf " + defect_root_dir + "gcov\nmkdir " + defect_root_dir + "gcov\nmkdir " + defect_root_dir + "outputs\n")
    f.writelines("gcc -fprofile-arcs -ftest-coverage " + defect_source_path + " -o " + defect_source_path + ".exe -lm\n")
    source_file_name = defect_source_path[ util.findIndex(defect_source_path, "/")[-1]+1 : util.findIndex(defect_source_path, ".")[-1] ]
    f.writelines("mv " + source_file_name + ".gcno " + defect_source_path + ".gcno\n\n")

    for i in range(len(input_paths)):
        command = 'echo ">>>>>>>>running test ' + str(i+1) + '"\n'
        f.writelines(command)
        command = "timeout "  + str(timeout) + " " \
              + defect_source_path +".exe " \
              + list_input_args[i] +" > "\
              + defect_root_dir + "outputs/" + input_paths[i]+".out\n" \
              + "mv " + source_file_name + ".gcda " + defect_source_path + ".gcda\n" \
              + "gcov " + defect_source_path + ".exe" \
              + "\nmv " + source_file_name + ".c.gcov " \
              + defect_root_dir + "gcov/" + source_file_name \
              + ".gcov." + str(i+1) + "\n\n"

        f.writelines(command)
    f.writelines("rm " + defect_source_path + ".gcno\n")
    f.writelines("rm " + defect_source_path + ".gcda\n")
    f.close()


if __name__ == "__main__" :
    args = parserCommad()

    if args.inputs_type == "file":  # 文件模式
        createRunDefectSourceScriptFileMode(args.defect_root_dir, args.defect_source_path, args.timeout, args.inputs_dir)
    elif args.inputs_type == "args":  # 参数模式
        createRunDefectSourceScriptArgsMode(args.defect_root_dir, args.defect_source_path, args.timeout, args.inputs_dir)
    else:  # inputs_type异常
        raise Exception("!!!!!!-----inputs_type参数输入异常-------")


