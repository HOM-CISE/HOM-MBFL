import argparse

'''
Get the command line parameter and return them.
参数列表:
--inputs_dir 测试用例存放路径
--inputs_type 测试用例类型（文件[file]或参数[args]类型）
--true_root_dir 正确程序根目录
--true_source_path 正确源代码路径
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

    parser.add_argument('--true_root_dir', action='store',
                        default="./test_data/true_root/",
                        dest='true_root_dir',
                        help='True example root dictionary.')

    parser.add_argument('--true_source_path', action='store',
                        default="./test_data/true_root/source/tot_info.c",
                        dest='true_source_path',
                        help='True program path.')

    parser.add_argument('--timeout', action='store',
                        dest='timeout',
                        type=int,
                        default=1,
                        help="run time limit of every program.")

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.2')

    results = parser.parse_args()

    return results


def createRunTrueSourceScriptFileMode(true_root_dir, true_source_path, timeout, inputs_dir):
    f = open("./output/input_list.txt", 'r')
    input_paths = f.read().split("\n")[:-1]
    f.close()

    f = open(true_root_dir + "run.sh", "w")
    f.writelines("mkdir " + true_root_dir + "outputs\n")

    gcc_command = 'gcc ' + true_source_path + ' -o ' + true_source_path + '.exe -lm\n'
    f.writelines(gcc_command)

    for i in range(len(input_paths)):
        command = 'echo ">>>>>>>>running test ' + str(i + 1) + '"\n'
        f.writelines(command)
        command = "timeout " + str(timeout) + " " \
                  + true_source_path + ".exe < " \
                  + inputs_dir + input_paths[i] + " > " \
                  + true_root_dir + "outputs/" + input_paths[i] + ".out\n"
        f.writelines(command)

    f.close()


'''
读取output下的inputs_list文件（测试用例文件名列表），从所有测试用例文件中读出内容，续到运行正确源代码的run.sh脚本中
'''
def createRunTrueSourceScriptArgsMode(true_root_dir, true_source_path, timeout, inputs_dir):

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

    # 生成运行正确源代码的run.sh脚本
    f = open(true_root_dir+"run.sh", "w")
    f.writelines("mkdir " + true_root_dir + "outputs\n")

    gcc_command = 'gcc '+ true_source_path +' -o '+ true_source_path +'.exe -lm\n'
    f.writelines(gcc_command)

    for i in range(len(list_input_args)):
        command = 'echo ">>>>>>>>running test ' + str(i+1) + '"\n'
        f.writelines(command)
        command = "timeout " + str(timeout) + " " \
              + true_source_path +".exe " \
              + list_input_args[i] +" > "\
              + true_root_dir + "outputs/" + input_paths[i]+".out\n"
        f.writelines(command)

    f.close()


if __name__ == "__main__":
    args = parserCommad()

    if args.inputs_type == "file":  # 文件模式
        createRunTrueSourceScriptFileMode(args.true_root_dir, args.true_source_path, args.timeout, args.inputs_dir)
    elif args.inputs_type == "args":  # 参数模式
        createRunTrueSourceScriptArgsMode(args.true_root_dir, args.true_source_path, args.timeout, args.inputs_dir)
    else:  # inputs_type异常
        raise Exception("!!!!!!-----inputs_type参数输入异常-------")
