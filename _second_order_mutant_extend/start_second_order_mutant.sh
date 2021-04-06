second_order_mutant_starttime=`date +'%Y-%m-%d %H:%M:%S'`

echo "=====[second_order_mutant_starttime]: "second_order_mutant_starttime
echo "===========second_order_mutant_initialize args:"

# 测试用例存放目录
inputs_dir="./test_data/inputs/"
# 测试用例输入类型（文件[file] OR 命令参数[args]）
inputs_type="file"
# 正确程序根目录
true_root_dir="./test_data/true_root/"
# 正确源代码路径
true_source_path="./test_data/true_root/source/test.c"

# 缺陷程序根目录
defect_root_dir="./test_data/defect_root/"
# 缺陷源代码目录
defect_source_dir="./test_data/defect_root/source/"
# 缺陷源代码路径
defect_source_path="./test_data/defect_root/source/test.c"
# 判断程序运行超时，并终止运行程序的阈值
timeout=10

# this is a first order mutant suspicious file for combine second order mutants
first_order_mutant_suspicious_file="./output/suspicious_first_order_Dstar3.txt"

# Mutant source code path
second_order_mutant_path="./second_order_mutant_extend/result/"

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
rm -rf ./second_order_mutant_extend/result
rm -rf ./second_order_mutant_extend/__pycache__
#rm -rf ./output
#rm -rf $true_source_path".exe"
#rm -rf $true_root_dir"run.sh"
#rm -rf $true_root_dir"outputs"
#rm -rf $defect_source_path".exe"
#rm -rf $defect_root_dir"run_cov.sh"
#rm -rf $defect_root_dir"compile"
#rm -rf $defect_root_dir"gcov"
#rm -rf $defect_root_dir"Mutation_source"
#rm -rf $defect_root_dir"outputs"
echo "======================(accept)clear_temp_file==========================="
sleep 1

#=======================================================================================================================
# 根据所有一阶变异体怀疑度，创建二阶变异体记录文件：./result/logs/res_record_second_order.txt
mkdir ./second_order_mutant_extend/result
mkdir ./second_order_mutant_extend/result/logs

python3 ./second_order_mutant_extend/create_second_order_mutants_record.py --first_order_mutant_suspicious_file $first_order_mutant_suspicious_file
echo "===========(accept)Create res_record_second_order.txt ========================="

# 修改本目录及子目录下所有文件使用权限
chmod 777 -R ./*
rm -rf $defect_source_path".exe"
# 复制被测代码及其目录下所有文件，到变异体源码操作目录（保证变异体程序编译时，其他关联文件也存在）
cp -r $defect_source_dir $second_order_mutant_path
# 创建二阶变异体源代码（将被测程序拷贝后重命名，修改文件中的内容）
python3 ./second_order_mutant_extend/create_second_order_mutants.py --second_order_mutant_path $second_order_mutant_path --defect_source_path $defect_source_path
echo "===========(accept)combine second order mutant source ======================"

# 创建编译二阶变异体程序脚本，并执行
python3 ./second_order_mutant_extend/create_compile_second_order_mutants_shell.py --second_order_mutant_path $second_order_mutant_path
sh ./second_order_mutant_extend/compile_second_order_mutants.sh
rm ./second_order_mutant_extend/compile_second_order_mutants.sh
echo "==================== (accept)compile second order mutants ====================="

# 记录可运行的二阶变异体（通过编译的变异体），记录变异体编号到./second_order_mutant_extend/result/logs/res_execute_mutant.txt
python3 ./second_order_mutant_extend/create_res_execute_second_order_mutants.py --second_order_mutant_path $second_order_mutant_path
echo "==================== (accept)create res_execute_mutant ====================="

# 统计所有可运行变异体的详细信息，即按照res_execute_mutant.txt文件的变异体序号组合res_record_second_order.txt文件的变异体详细信息
python3 ./second_order_mutant_extend/create_all_execute_mutants.py
echo "==================== (accept)create all_execute_mutants ====================="


# 生成二阶变异体执行脚本create_res_original_fault_version_second_order_in.sh
python3 ./second_order_mutant_extend/create_res_original_fault_version_second_order_in_shell.py --inputs_dir $inputs_dir --inputs_type $inputs_type --true_root_dir $true_root_dir --defect_root_dir $defect_root_dir --second_order_mutant_path $second_order_mutant_path --timeout $timeout
echo "===== (accept)create create_res_original_fault_version_in.sh ============="

# 执行create_res_original_fault_version_second_order_in.sh
sh ./create_res_original_fault_version_second_order_in.sh
rm ./create_res_original_fault_version_second_order_in.sh
echo "===== (accept)create res_original_version.in & res_fault_version.in ======"

# calculation the suspicious of set of second order mutants
python3 ./second_order_mutant_extend/clac_sus_second_order.py
echo "===================== (accept) calculate the suspicious ============="


echo ""
echo ""
echo "================= Thank you for your using! =============================="
echo ""
second_order_mutant_endtime=`date +'%Y-%m-%d %H:%M:%S'`
echo "=====[second_order_mutant_starttime]: "$second_order_mutant_starttime
echo "=====[second_order_mutant_endtime]: "$second_order_mutant_endtime
start_second=$(date --date="$second_order_mutant_starttime" +%s)
end_second=$(date --date="$second_order_mutant_endtime" +%s)
echo "run time(sec): "$((end_second-start_second))
echo "=====[starttime]: "$second_order_mutant_starttime >> ./time.log
echo "=====[endtime]: "$second_order_mutant_endtime >> ./time.log
echo "run time(sec): "$((end_second-start_second)) >> ./time.log
echo "=============================================" >> ./time.log
echo ""
echo ""
echo ""


