import os
import shutil

# 配置版本，确定一次执行的版本范围
begin_version_index = 1
end_version_index = 100 + 1


# 生成替换数据集和导出结果shell脚本，并串行运行所有版本。
if __name__ == "__main__":
    f = open("start_multi_version_FOM_and_HOM_MBFL.sh", "w")
    for version_index in range(begin_version_index, end_version_index):
        src_test_data_path = "../version/v" + str(version_index) + "/test_data"
        tag_test_data_path = "./test_data"

        f.write("cp -r " + src_test_data_path + " " + tag_test_data_path)
        f.write("\nsh start.sh")
        f.write("\nsh start_entire_randomization_higher_order_MBFL.sh")
        f.write("\nmkdir ../result/v" + str(version_index))
        f.write("\nmv output ../result/v" + str(version_index) + "/output")
        f.write("\nmv _entire_randomization_higher_order_mutant_set ../result/v" + str(version_index) + "/_entire_randomization_higher_order_mutant_set")
        f.write("\nrm -rf " + tag_test_data_path)
        f.write("\necho 'v" + str(version_index) + " is already execute.\\n\\n'\n\n")
    f.close()

