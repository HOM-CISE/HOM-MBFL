between_worst_ideal_MBFL_run_starttime=`date +'%Y-%m-%d %H:%M:%S'`

echo "==========[between_worst_ideal_MBFL_run_starttime]: "between_worst_ideal_MBFL_run_starttime
echo "=================between_worst_ideal_MBFL_run_initialize args:"

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


rm -rf ./_between_worst_ideal_mutant_set
echo "======================(accept)clear_temp_file==========================="
mkdir ./_between_worst_ideal_mutant_set


# 创建可变异的变异行行数列表
python3 ./between_worst_ideal_higher_mutant_set_extend/create_res_mutant_line.py
echo "==================== (accept)create between_worst_ideal_mutant_set & res_mutant_line.txt ======================"


# 随机选择两个变异体行，组合成二阶变异体列表
python3 ./between_worst_ideal_higher_mutant_set_extend/create_res_record.py
echo "==================== (accept)create res_record.txt ======================"


# 修改本目录及子目录下所有文件使用权限
chmod 777 -R ./*
rm -rf $defect_source_path".exe"


# 复制被测代码及其目录下所有文件，到变异体源码操作目录（保证变异体程序编译时，其他关联文件也存在）
cp -r $defect_source_dir ./_between_worst_ideal_mutant_set/


# 创建变异体源代码（将被测程序拷贝后重命名，修改文件中的内容）
python3 ./between_worst_ideal_higher_mutant_set_extend/create_mutants.py --mutant_root ./_between_worst_ideal_mutant_set/ --defect_source_path $defect_source_path
echo "==================== (accept)combine mutant sources of each set ======================"


# 创建编译变异体程序脚本，并执行
python3 ./between_worst_ideal_higher_mutant_set_extend/create_compile_mutants_shell.py --mutant_root ./_between_worst_ideal_mutant_set/
sh ./compile_mutation.sh
rm ./compile_mutation.sh
echo "==================== (accept)complie mutants of each set  ============================"


# 记录可运行的变异体（通过编译的变异体）
python3 ./between_worst_ideal_higher_mutant_set_extend/create_res_execute_mutant.py --mutant_root ./_between_worst_ideal_mutant_set/
echo "==================== (accept)create res_execute_mutant.txt ==============================="

# 统计所有可运行变异体的详细信息，即按照res_execute_mutant.txt文件的变异体序号组合res_record.txt文件的变异体详细信息
python3 ./between_worst_ideal_higher_mutant_set_extend/create_all_execute_mutants.py --mutant_root ./_between_worst_ideal_mutant_set/
echo "==================== (accept)create all_execute_mutant.txt ==============================="


# 生成变异体执行脚本create_res_original_fault_version_in.sh
python3 ./between_worst_ideal_higher_mutant_set_extend/create_res_original_fault_version_in_shell.py --inputs_dir $inputs_dir --inputs_type $inputs_type --true_root_dir $true_root_dir --defect_root_dir $defect_root_dir --mutant_root ./_between_worst_ideal_mutant_set/ --timeout $timeout
echo "==================== (accept) create create_res_original_fault_version_in.sh ============="

# 执行create_res_original_fault_version_in.sh
sh ./create_worst_res_original_fault_version_in.sh
rm ./create_worst_res_original_fault_version_in.sh
echo "==================== (accept) create res_original_version.in & res_fault_version.in ======"

# calculate the suspicious of each set of mutants.
python3 ./between_worst_ideal_higher_mutant_set_extend/clac_worst_sus.py
python3 ./between_worst_ideal_higher_mutant_set_extend/combine_worst_sus.py
python3 ./between_worst_ideal_higher_mutant_set_extend/clac_worst_EXAM_score.py
echo "==================== (accept) calculate the suspicious and EXAM score ==================================="


echo ""
echo ""
echo "================= Thank you for your using! =============================="
echo ""
between_worst_ideal_MBFL_run_endtime=`date +'%Y-%m-%d %H:%M:%S'`
echo "=====[starttime]: "$between_worst_ideal_MBFL_run_starttime
echo "=====[endtime]: "$between_worst_ideal_MBFL_run_endtime
start_second=$(date --date="$between_worst_ideal_MBFL_run_starttime" +%s)
end_second=$(date --date="$between_worst_ideal_MBFL_run_endtime" +%s)
echo "run time(sec): "$((end_second-start_second))
echo "=====[starttime]: "$between_worst_ideal_MBFL_run_starttime >> ./time.log
echo "=====[endtime]: "$between_worst_ideal_MBFL_run_endtime >> ./time.log
echo "run time(sec): "$((end_second-start_second)) >> ./time.log
echo "===============between_worst_ideal_MBFL==============================" >> ./time.log
echo ""
echo ""
echo ""
