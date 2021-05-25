### Manual：

Put the program under test into "./test_data/defect_root/source/", and modify the value of "defect_source_path" in "start.sh".

Put the standard program into "./test_data/true_root/", and modify the value of "true_source_path" in "start.sh".

Put the test cases into "./test_data/inputs/", if the test cases are read by the program under test by file redirection, the value of the "input_type" in "start.sh" need to be changed to "file", not "args".

### Experimental data set：

| Benchmark |   Program    | Version(used) | LOC  |
| :-------: | :----------: | :-----------: | :--: |
|    SIR    | printtokens  |     7(7)      | 563  |
|    SIR    | printtokens2 |     9(6)      | 508  |
|    SIR    |  schedule2   |     10(4)     | 307  |
|    SIR    |   totinfo    |    23(18)     | 406  |
|    SIR    |     tcas     |    41(30)     | 173  |
|    SIR    |     sed      |     9(5)      | 7125 |
| Codeflaws |              |  3902(1408)   |  43  |

#### Remarks：

* This tool passed experiment on the "Linux version 3.10.0-957.el7.x86_64".
* python version : 3.6.8
