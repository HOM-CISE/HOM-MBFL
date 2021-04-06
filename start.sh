starttime=`date +'%Y-%m-%d %H:%M:%S'`

echo "=====[starttime]: "$starttime
echo "===========initialize args:"

# 测试用例存放目录
inputs_dir="./test_data/inputs/"
# 测试用例输入类型（文件[file] OR 命令参数[args]）
inputs_type="args"

# 正确程序根目录
true_root_dir="./test_data/true_root/"
# 正确源代码路径
true_source_path="./test_data/true_root/source/tcas.c"

# 缺陷程序根目录
defect_root_dir="./test_data/defect_root/"
# 缺陷源代码目录
defect_source_dir="./test_data/defect_root/source/"
# 缺陷源代码路径
defect_source_path="./test_data/defect_root/source/tcas.c"

# 判断程序运行超时，并终止运行程序的阈值
timeout=10

echo "inputs_dir = "$inputs_dir
echo "inputs_type = "$inputs_type
echo "true_root_dir = "$true_root_dir
echo "true_source_path = "$true_source_path
echo "defect_root_dir = "$defect_root_dir
echo "defect_source_dir = "$defect_source_dir
echo "defect_source_path = "$defect_source_path
echo "timeout = "$timeout
echo "======================(accept)initialize================================"

# clear all temp files
rm -rf ./__pycache__
rm -rf ./output
rm -rf $true_source_path".exe"
rm -rf $true_root_dir"run.sh"
rm -rf $true_root_dir"outputs"
rm -rf $defect_source_path".exe"
rm -rf $defect_root_dir"run_cov.sh"
rm -rf $defect_root_dir"compile"
rm -rf $defect_root_dir"gcov"
rm -rf $defect_root_dir"Mutation_source"
rm -rf $defect_root_dir"outputs"
echo "======================(accept)clear_temp_file==========================="
sleep 1

# 修改本目录及子目录下所有文件使用权限
chmod 777 -R ./*
# 复制缺陷代码及其目录下所有文件，到变异体源码操作目录（保证变异体程序编译时，其他关联文件也存在）
cp -r $defect_source_dir $defect_root_dir"Mutation_source/"

# 替换输入文件的文件名中存在的非法字符（对输入文件重命名）
python3 rename_inputs_file.py --inputs_dir $inputs_dir
echo "=======================(accept)rename_inputs_file======================="


# 创建输出文件夹（存放最后结果文件夹）
mkdir ./output
# 拷贝Fault_Record.txt记录错误代码文件到output下
cp $defect_root_dir"Fault_Record.txt" output/Fault_Record.txt

# 读取测试用例文件夹下所有测试用例，并且生成输出序列，以保证测试用例的顺序
python3 create_input_list.py --inputs_dir $inputs_dir

# 根据测试用例类型生成运行正确程序的完整shell脚本
python3 create_run_true_source_shell.py --inputs_dir $inputs_dir --inputs_type $inputs_type --true_root_dir $true_root_dir --true_source_path $true_source_path --timeout $timeout

# 运行生成的正确程序shell脚本
sh $true_root_dir"run.sh"
echo "=======================(accept)run_true_source=========================="


# 根据测试用例类型生成运行缺陷程序和运行覆盖的完整shell脚本run_cov.sh
python3 create_run_defect_source_shell.py --inputs_dir $inputs_dir --inputs_type $inputs_type --defect_root_dir $defect_root_dir --defect_source_path $defect_source_path --timeout $timeout

# 运行run_cov.sh
sh $defect_root_dir"run_cov.sh"
echo "=====================(accept)run_defect_source=========================="


# 比对每一个正确源程序输出和缺陷源程序输出是否相同，比对结果保存到output/res_vector.in中
python3 create_res_vector_in.py --true_root_dir $true_root_dir --defect_root_dir $defect_root_dir
echo "==================== (accept)create res_vector.in ======================"

# 生成缺陷源程序运行所有测试用例的覆盖情况，覆盖矩阵保存在output/res_cov_matrix.in中
python3 create_res_cov_matrix_in.py --defect_root_dir $defect_root_dir
echo "===================== (accept)create res_cov_matrix.in =================="

# generate the suspicious of each covered source line using SBFL, and save the list in "output/suspicious_SBFL.txt"
python3 clac_sus_SBFL.py
echo "===================== (accept)calc suspicious_SBFL.txt =================="

# 生成缺陷源程序所有的变异体
python3 create_all_res_record.py --defect_source_path $defect_source_path
echo "==================== (accept)create all_res_record.txt ======================"
# 生成缺陷源程序被执行错误的测试用例覆盖的语句，所产生的变异体列表
python3 create_res_record.py --defect_source_path $defect_source_path
echo "==================== (accept)create res_record.txt ======================"


# 生成变异体程序源码
python3 create_mutation.py --defect_root_dir $defect_root_dir --defect_source_path $defect_source_path
echo "==================== (accept)create mutation_source ====================="


# 创建编译变异体程序脚本，并执行
python3 create_compile_mutation_shell.py --defect_root_dir $defect_root_dir
sh ./compile_mutation.sh
rm ./compile_mutation.sh
echo "==================== (accept)compile mutation ====================="


# 记录可运行的变异体（通过编译的变异体），记录变异体编号到output/res_execute_mutant.txt
python3 ./create_res_execute_mutant.py --defect_root_dir $defect_root_dir
echo "==================== (accept)create res_execute_mutant ====================="

# 记录所有可运行变异体的详细信息，即按照res_execute_mutant.txt文件的变异体序号组合res_record.txt文件的变异体详细信息
python3 ./create_all_execute_mutants.py
echo "==================== (accept)create all_execute_mutants ====================="

# 生成变异体执行脚本create_res_original_fault_version_in.sh
python3 ./create_res_original_fault_version_in_shell.py --inputs_dir $inputs_dir --inputs_type $inputs_type --true_root_dir $true_root_dir --defect_root_dir $defect_root_dir --timeout $timeout
echo "===== (accept)create create_res_original_fault_version_in.sh ============="

# 执行create_res_original_fault_version_in.sh
sh ./create_res_original_fault_version_in.sh
rm ./create_res_original_fault_version_in.sh
echo "===== (accept)create res_original_version.in & res_fault_version.in ======"

# 计算一阶变异体怀疑度
python3 ./clac_sus_first_order.py
python3 ./calc_EXAM_score.py
echo "===================== (accept) calculate the suspicious ============="



echo ""
echo ""
echo "================= Thank you for your using! =============================="
echo ""
endtime=`date +'%Y-%m-%d %H:%M:%S'`
echo "=====[starttime]: "$starttime
echo "=====[endtime]: "$endtime
start_second=$(date --date="$starttime" +%s)
end_second=$(date --date="$endtime" +%s)
echo "run time(sec): "$((end_second-start_second))
echo "=====[starttime]: "$starttime >> ./time.log
echo "=====[endtime]: "$endtime >> ./time.log
echo "run time(sec): "$((end_second-start_second)) >> ./time.log
echo "===========FOM==================================" >> ./time.log
echo ""
echo ""
echo ""
