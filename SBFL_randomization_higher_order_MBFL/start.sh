#!/usr/bin/env bash
SBFL_randomization_higher_order_MBFL_run_starttime=`date +'%Y-%m-%d %H:%M:%S'`

echo "==========[SBFl_randomization_higher_order_MBFL_run_starttime]: "$SBFL_randomization_higher_order_MBFL_run_starttime
echo "=================SBFL_randomization_higher_order_MBFL_run_initialize args:"

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

# 生成高阶变异体的最小阶数
min_order_num=2
# 生成高阶变异体的最大阶数
max_order_num=2
# 判断程序运行超时，并终止运行程序的阈值
timeout=10


echo "inputs_dir = "$inputs_dir
echo "inputs_type = "$inputs_type
echo "true_root_dir = "$true_root_dir
echo "true_source_path = "$true_source_path
echo "defect_root_dir = "$defect_root_dir
echo "defect_source_dir = "$defect_source_dir
echo "defect_source_path = "$defect_source_path
echo "min_order_num = "$min_order_num
echo "max_order_num = "$max_order_num
echo "timeout = "$timeout
echo "======================(accept)initialize================================"


rm -rf ./_SBFL_randomization_higher_order_mutant_set
echo "======================(accept)clear_temp_file==========================="
sleep 5
mkdir ./_SBFL_randomization_higher_order_mutant_set

# generate the suspicious of each covered source line using SBFL, and save the list in "output/suspicious_SBFL.txt"
python3 ./SBFL_randomization_higher_order_MBFL/clac_sus_SBFL.py
echo "===================== (accept)calc suspicious_SBFL.txt =================="

# 创建可变异的变异行行数列表
python3 ./SBFL_randomization_higher_order_MBFL/create_res_mutant_line.py --min_order_num $min_order_num --max_order_num $max_order_num
echo "==================== (accept)create SBFL_randomization_higher_order_mutant_set & res_mutant_line.txt ======================"


# 生成变异体res_record.txt列表
python3 ./SBFL_randomization_higher_order_MBFL/create_res_record.py
echo "==================== (accept)create res_record.txt ======================"


# 修改本目录及子目录下所有文件使用权限
chmod 777 -R ./*
rm -rf $defect_source_path".exe"


# 复制被测代码及其目录下所有文件，到变异体源码操作目录（保证变异体程序编译时，其他关联文件也存在）
cp -r $defect_source_dir ./_SBFL_randomization_higher_order_mutant_set/Mutation_source/


# 创建变异体源代码（将被测程序拷贝后重命名，修改文件中的内容）
python3 ./SBFL_randomization_higher_order_MBFL/create_mutants.py --mutant_root ./_SBFL_randomization_higher_order_mutant_set/ --defect_source_path $defect_source_path
echo "==================== (accept)combine mutant sources of each set ======================"


# 创建编译变异体程序脚本，并执行
python3 ./SBFL_randomization_higher_order_MBFL/create_compile_mutants_shell.py --mutant_root ./_SBFL_randomization_higher_order_mutant_set/
sh ./compile_mutation.sh
rm ./compile_mutation.sh
echo "==================== (accept)complie mutants of each set  ============================"


# 记录可运行的变异体（通过编译的变异体）
python3 ./SBFL_randomization_higher_order_MBFL/create_res_execute_mutant.py --mutant_root ./_SBFL_randomization_higher_order_mutant_set/
echo "==================== (accept)create res_execute_mutant.txt ==============================="

# 统计所有可运行变异体的详细信息，即按照res_execute_mutant.txt文件的变异体序号组合res_record.txt文件的变异体详细信息
python3 ./SBFL_randomization_higher_order_MBFL/create_all_execute_mutants.py --mutant_root ./_SBFL_randomization_higher_order_mutant_set/
echo "==================== (accept)create all_execute_mutant.txt ==============================="

# 对 res_execute_mutant.txt 和 all_execute_mutant.txt 备份，再对本文件进行筛选，并保存
cp ./_SBFL_randomization_higher_order_mutant_set/res_execute_mutant.txt ./_SBFL_randomization_higher_order_mutant_set/res_execute_mutant.txt.bak
cp ./_SBFL_randomization_higher_order_mutant_set/all_execute_mutant.txt ./_SBFL_randomization_higher_order_mutant_set/all_execute_mutant.txt.bak
python3 ./SBFL_randomization_higher_order_MBFL/filter_HOMs.py

# 生成变异体执行脚本create_res_original_fault_version_in.sh
python3 ./SBFL_randomization_higher_order_MBFL/create_res_original_fault_version_in_shell.py --inputs_dir $inputs_dir --inputs_type $inputs_type --true_root_dir $true_root_dir --defect_root_dir $defect_root_dir --mutant_root ./_SBFL_randomization_higher_order_mutant_set/ --timeout $timeout
echo "==================== (accept) create create_res_original_fault_version_in.sh ============="

# 执行create_res_original_fault_version_in.sh
sh ./create_res_original_fault_version_in.sh
rm ./create_res_original_fault_version_in.sh
echo "==================== (accept) create res_original_version.in & res_fault_version.in ======"

# calculate the suspicious of each set of mutants.
python3 ./SBFL_randomization_higher_order_MBFL/clac_sus_max_mutate_sus_to_statement.py
python3 ./SBFL_randomization_higher_order_MBFL/combine_sus_max_mutate_sus_to_statement.py
python3 ./SBFL_randomization_higher_order_MBFL/clac_EXAM_score_max_mutate_sus_to_statement.py

python3 ./SBFL_randomization_higher_order_MBFL/clac_sus_average_mutate_sus_to_statement.py
python3 ./SBFL_randomization_higher_order_MBFL/combine_sus_average_mutate_sus_to_statement.py
python3 ./SBFL_randomization_higher_order_MBFL/clac_EXAM_score_average_mutate_sus_to_statement.py

python3 ./SBFL_randomization_higher_order_MBFL/clac_sus_frequency_mutate_sus_to_statement.py
python3 ./SBFL_randomization_higher_order_MBFL/combine_sus_frequency_mutate_sus_to_statement.py
python3 ./SBFL_randomization_higher_order_MBFL/clac_EXAM_score_frequency_mutate_sus_to_statement.py
echo "==================== (accept) calculate the suspicious and EXAM score ==================================="


echo ""
echo ""
echo "================= Thank you for your using! =============================="
echo ""

SBFL_randomization_higher_order_MBFL_run_endtime=`date +'%Y-%m-%d %H:%M:%S'`
echo "=====[starttime]: "$SBFL_randomization_higher_order_MBFL_run_starttime
echo "=====[endtime]: "$SBFL_randomization_higher_order_MBFL_run_endtime
start_second=$(date --date="$SBFL_randomization_higher_order_MBFL_run_starttime" +%s)
end_second=$(date --date="$SBFL_randomization_higher_order_MBFL_run_endtime" +%s)
echo "run time(sec): "$((end_second-start_second))
echo "=====[starttime]: "$SBFL_randomization_higher_order_MBFL_run_starttime >> ./time.log
echo "=====[endtime]: "$SBFL_randomization_higher_order_MBFL_run_endtime >> ./time.log
echo "run time(sec): "$((end_second-start_second)) >> ./time.log
echo "====SBFL_randomization_higher_order_MBFL=========================================" >> ./time.log
echo ""
echo ""
echo ""
