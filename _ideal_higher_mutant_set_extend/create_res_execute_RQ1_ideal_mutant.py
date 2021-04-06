import os
import util

if __name__ == "__main__":

        compile_dir = "./_RQ1_mutant_set/mutant_set_ideal/compile/"
        file_name_list = os.listdir(compile_dir)
        file_name = file_name_list[0]
        replace_index = util.findIndex(file_name, "_")
        file_name = file_name[:replace_index[-1]]

        mutation_dir = "./_RQ1_mutant_set/mutant_set_ideal/Mutant_source/"
        mutation_file_list = os.listdir(mutation_dir)
        mutation_file_number = len(mutation_file_list)

        with open("./_RQ1_mutant_set/mutant_set_ideal" + "/res_execute_mutant.txt", 'w') as f :
            f.write("")   # create and clean res_record.txt
            f.close()
        f = open("./_RQ1_mutant_set/mutant_set_ideal" + "/res_execute_mutant.txt", 'a')

        for i in range(mutation_file_number):
            file_temp_name = file_name + "_" +str(i+1) + ".c.exe"
            if file_temp_name in file_name_list:
                f.write(str(i+1)+"\n")

        f.close()
