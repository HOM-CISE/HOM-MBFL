import os

if __name__ == "__main__":

    with open("./compile_mutation.sh", "w") as f:
        f.write("")
    f.close()

    mutation_dir = "./_RQ1_mutant_set/mutant_set_ideal/Mutant_source/"
    compile_dir = "./_RQ1_mutant_set/mutant_set_ideal/compile/"

    file_name_list = os.listdir(mutation_dir)

    f = open("./compile_mutation.sh", "a")

    if not os.path.exists(compile_dir):
        os.mkdir(compile_dir)

    for file_name in file_name_list:
        f.write("gcc " + mutation_dir + file_name + " -o " + compile_dir + file_name + ".exe -lm\n")

    f.close()