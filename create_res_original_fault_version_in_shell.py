import os
import util
import argparse

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

    parser.add_argument('--true_root_dir', action='store',
                        default="./test_data/true_root/",
                        dest='true_root_dir',
                        help='True example root dictionary.')

    parser.add_argument('--defect_root_dir', action='store',
                        default="./test_data/defect_root/",
                        dest='defect_root_dir',
                        help='Defect example root dictionary.')

    parser.add_argument('--timeout', action='store',
                        dest='timeout',
                        type=int,
                        default=1,
                        help="run time limit of every program.")

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.3')

    results = parser.parse_args()

    return results


def createResOriginalFaultVersionInShellFileMode():
    f_create_shell = open("./create_res_original_fault_version_in.sh", "w")
    mutation_list = []
    with open("./output/res_execute_mutant.txt", "r") as f:
        mutation_list = f.read()
        mutation_list = mutation_list.split("\n")[:-1]
    f.close()

    input_path = args.inputs_dir
    input_list = []
    with open("./output/input_list.txt", "r") as f:
        input_list = f.read().split("\n")[:-1]
    f.close()


    file_name = ""
    compile_dir = args.defect_root_dir + "compile/"
    con_list = os.walk(compile_dir)
    for path, path_l, file_names in con_list:
        file_name = file_names[0]

    file_name = file_name[:util.findIndex(file_name, "_")[-1]]
    f_create_shell.write("chmod 777 " + compile_dir + "*\n")
    f_create_shell.write("rm ./output/res_original_version.in ./output/res_fault_version.in\n")
    f_create_shell.write("touch ./output/res_original_version.in ./output/res_fault_version.in\n")
    f_create_shell.write("\n\n")

    #f = open("./create_res_original_fault_version_in.sh", "a")

    for excute_mutation in mutation_list:
        f_create_shell.write("mkdir ./temp_outputs/\n")
        for input_sample in input_list:
            f_create_shell.write("nowtime=`date +'%Y-%m-%d %H:%M:%S'`\n")
            f_create_shell.write('echo "=====[nowtime]: "$nowtime\n')
            f_create_shell.write('echo "<<<<<<<<<<<'+file_name+'_' + excute_mutation + '.c.exe ||run| '+ input_sample +'"\n')
            f_create_shell.write('timeout ' + str(args.timeout) + " " + compile_dir + file_name + '_' + excute_mutation + '.c.exe < ' + input_path + input_sample + ' > ./temp_outputs/' + input_sample + '.out\n')
            f_create_shell.write('return_code=$?\n')
            f_create_shell.write('echo return_code=$return_code\n')
            f_create_shell.write('if [ $return_code -eq 124 ]; then\n')
            f_create_shell.write('rm -rf ' + compile_dir + file_name + '_' + excute_mutation + '.c.exe\n')
            f_create_shell.write('echo \"' + compile_dir + file_name + '_' + excute_mutation + '.c.exe was deleted successfully.\"\n')
            f_create_shell.write('fi\n')
            f_create_shell.write('if [ $return_code -eq 134 ]; then\n')
            f_create_shell.write('rm -rf ' + compile_dir + file_name + '_' + excute_mutation + '.c.exe\n')
            f_create_shell.write('echo \"' + compile_dir + file_name + '_' + excute_mutation + '.c.exe was deleted successfully.\"\n')
            f_create_shell.write('fi\n')
            f_create_shell.write('if [ $return_code -eq 139 ]; then\n')
            f_create_shell.write('rm -rf ' + compile_dir + file_name + '_' + excute_mutation + '.c.exe\n')
            f_create_shell.write('echo \"' + compile_dir + file_name + '_' + excute_mutation + '.c.exe was deleted successfully.\"\n')
            f_create_shell.write('fi\n')
            f_create_shell.write('\n')
        f_create_shell.write("python ./append_res_original_version_in.py --true_root_dir " + args.true_root_dir + "\n")
        f_create_shell.write("python ./append_res_fault_version_in.py --defect_root_dir " + args.defect_root_dir + "\n")
        f_create_shell.write("rm -rf ./temp_outputs/\n")
        f_create_shell.write("\n")
    f_create_shell.close()


def createResOriginalFaultVersionInShellArgsMode():
    f_create_shell = open("./create_res_original_fault_version_in.sh", "w")
    mutation_list = []
    with open("./output/res_execute_mutant.txt", "r") as f:
        mutation_list = f.read()
        mutation_list = mutation_list.split("\n")[:-1]
    f.close()

    input_path = args.inputs_dir
    input_list = []
    with open("./output/input_list.txt", "r") as f:
        input_list = f.read().split("\n")[:-1]
    f.close()

    # 打开所有测试用例文件，读取文件内的参数
    list_input_args = []
    for i in range(len(input_list)):
        f = open(input_path + input_list[i], 'r')
        input_args = f.read()
        list_input_args.append(input_args)
        f.close()

    file_name = ""
    compile_dir = args.defect_root_dir + "compile/"
    con_list = os.walk(compile_dir)
    for path, path_l, file_names in con_list:
        file_name = file_names[0]

    file_name = file_name[:util.findIndex(file_name, "_")[-1]]


    f_create_shell.write("chmod 777 " + compile_dir +"*\n")
    f_create_shell.write("rm " + "./output/res_original_version.in ./output/res_fault_version.in\n")
    f_create_shell.write("touch ./output/res_original_version.in ./output/res_fault_version.in\n")
    f_create_shell.write("\n\n")

    #f = open("./create_res_original_fault_version_in.sh", "a")

    for excute_mutation in mutation_list:
        f_create_shell.write("mkdir ./temp_outputs/\n")
        for input_args, input_sample in zip(list_input_args, input_list):
            f_create_shell.write("nowtime=`date +'%Y-%m-%d %H:%M:%S'`\n")
            f_create_shell.write('echo "=====[nowtime]: "$nowtime\n')
            f_create_shell.write('echo "<<<<<<<<<<<' + file_name + '_' + excute_mutation + '.c.exe ||run| '+ input_sample +'"\n')
            f_create_shell.write('timeout ' + str(args.timeout) + " " + compile_dir + file_name + '_' + excute_mutation + '.c.exe '+ input_args + ' > ./temp_outputs/' + input_sample + '.out\n')
            f_create_shell.write('return_code=$?\n')
            f_create_shell.write('echo return_code=$return_code\n')
            f_create_shell.write('if [ $return_code -eq 124 ]; then\n')
            f_create_shell.write('rm -rf ' + compile_dir + file_name + '_' + excute_mutation + '.c.exe\n')
            f_create_shell.write('echo \"' + compile_dir + file_name + '_' + excute_mutation + '.c.exe was deleted successfully.\"\n')
            f_create_shell.write('fi\n')
            f_create_shell.write('if [ $return_code -eq 134 ]; then\n')
            f_create_shell.write('rm -rf ' + compile_dir + file_name + '_' + excute_mutation + '.c.exe\n')
            f_create_shell.write('echo \"' + compile_dir + file_name + '_' + excute_mutation + '.c.exe was deleted successfully.\"\n')
            f_create_shell.write('fi\n')
            f_create_shell.write('if [ $return_code -eq 139 ]; then\n')
            f_create_shell.write('rm -rf ' + compile_dir + file_name + '_' + excute_mutation + '.c.exe\n')
            f_create_shell.write('echo \"' + compile_dir + file_name + '_' + excute_mutation + '.c.exe was deleted successfully.\"\n')
            f_create_shell.write('fi\n')
            f_create_shell.write('\n')
        f_create_shell.write("python3 ./append_res_original_version_in.py --true_root_dir " + args.true_root_dir + "\n")
        f_create_shell.write("python3 ./append_res_fault_version_in.py --defect_root_dir " + args.defect_root_dir + "\n")
        f_create_shell.write("rm -rf ./temp_outputs/\n")
        f_create_shell.write("\n")
    f_create_shell.close()


if __name__ == "__main__":

    args = parserCommad()

    if args.inputs_type == "file":  # 文件模式
        createResOriginalFaultVersionInShellFileMode()
    elif args.inputs_type == "args":  # 参数模式
        createResOriginalFaultVersionInShellArgsMode()
    else:  # inputs_type异常
        raise Exception("!!!!!!-----inputs_type参数输入异常-------")
