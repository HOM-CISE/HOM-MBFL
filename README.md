### 使用方法：

将被测程序相关代码放入“./test_data/defect_root/source/”，并修改start.sh中defect_source_path变量的值。

将正确程序相关代码放入“./test_data/true_root/”，并修改start.sh中defect_source_path变量的值。

将相关测试数据放入“./test_data/inputs/”目录，如果测试数据是通过文件重定向的方式被被测程序读入，则start.sh中的inputs_type变量的值改为“file”。

### 实验验证程序：

| Benchmark |   Program    | Version(used) | LOC  |
| :-------: | :----------: | :-----------: | :--: |
|    SIR    | printtokens  |     7(7)      | 563  |
|    SIR    | printtokens2 |     9(6)      | 508  |
|    SIR    |  schedule2   |     10(4)     | 307  |
|    SIR    |   totinfo    |    23(18)     | 406  |
|    SIR    |     tcas     |    41(30)     | 173  |
|    SIR    |     sed      |     9(5)      | 7125 |
| Codeflaws |              |  3902(1408)   |  43  |

#### output文件夹下，所有生成的文件的格式及内容：

* all_execute_mutant.txt 记录所有可运行变异体的编号（编号对应res_record.txt的行号），以及该变异体的详细信息。

* all_res_record.txt 记录被测程序中，所有可变异的位置和变异的内容

* input_list.txt 记录输入的顺序列表

* res_cov_matrix.in 记录被测程序运行测试用例，所得到的语句覆盖矩阵，0表示没覆盖，1表示覆盖，2表示忽略。矩阵行数表示测试用例数量，列数表示程序行数，矩阵第一列表示被测程序的第一行。

* res_execute_mutant.txt 记录可以成功运行的变异体的编号，同变异体记录文件(res_record.txt)行号对应。

* res_fault_version.in 变异体程序输出结果和被测程序的输出结果进行比较，1代表结果不同(kill)，0代表结果相同(not kill)。矩阵的行数代表变异体的数量，矩阵的列数代表测试用例数量（或输出结果数量）。

* res_original_vector.in 变异体程序输出结果和正确程序的输出结果进行比较，1代表输出结果不同，0表示输出结果相同。

* res_record.txt 根据源代码运行覆盖情况，记录覆盖行对应源代码可以进行的变异（即生成的变异体信息）。

* res_vector.in 被测程序的测试用例通过或失效信息。1代表结果错误（failure），0代表通过（pass）。（判断运行通过和失效，是和正确结果比较得到的）

* suspicious_first_order_Jaccard.txt 计算所有变异体的Jaccard怀疑度列表（按照变异体序号顺序排序）

* suspicious_first_order_Ochiai.txt 计算所有变异体的Ochiai怀疑度列表（按照变异体序号顺序排序）

* suspicious_first_order_Op2.txt 计算所有变异体的Op2怀疑度列表（按照变异体序号顺序排序）

* suspicious_first_order_Tarantula.txt 计算所有变异体的Tarantula怀疑度列表（按照变异体序号顺序排序）

* suspicious_first_order_Dstar3.txt 计算所有变异体的Dstar3怀疑度列表（按照变异体序号顺序排序）

* suspicious_first_order.txt 统计一阶变异体得到的MBFL怀疑度列表（按照各公式的怀疑度大小排序），每一项对应代码行的怀疑度

* suspicious.txt 统计MBFL的最终怀疑度列表（综合了一阶变异体和高阶变异体），怀疑度列表中的每项代表一行代码的怀疑度。

---

#### 补充说明：


* 整个工具经测试，在"Linux version 3.10.0-957.el7.x86_64 (mockbuild@x86-040.build.eng.bos.redhat.com) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-36) (GCC) ) #1 SMP Thu Oct 4 20:48:51 UTC 2018"上可用
* python3 -V   ---> Python 3.6.8
