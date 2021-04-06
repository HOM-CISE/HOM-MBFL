if __name__ == "__main__":

    f = open("./_RQ1_mutant_set/mutant_set_ideal/res_execute_mutant.txt", 'r')
    list_execute_mutant = f.read().split('\n')[0:-1]
    f.close()

    f = open("./_RQ1_mutant_set/mutant_set_ideal/res_record.txt", 'r')
    list_mutant_record = []
    list_mutant_record.append(f.read())
    f.close()

    with open("./_RQ1_mutant_set/mutant_set_ideal/all_execute_mutant.txt", 'w') as f:
        f.write("")   # create and clean all_execute_mutant.txt
        f.close()

    f = open("./_RQ1_mutant_set/mutant_set_ideal/all_execute_mutant.txt", 'a')
    for i in range(len(list_execute_mutant)):
        f.write("Mutant_index: " + list_execute_mutant[i] + list_mutant_record[int(list_execute_mutant[i])-1] + '\n')
    f.close()
