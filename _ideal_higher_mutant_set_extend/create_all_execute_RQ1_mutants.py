import os
import util
import argparse

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--RQ1_mutant_path', action='store',
                        default="./_RQ1_mutant_set/",
                        dest='RQ1_mutant_path',
                        help='RQ1 mutant root dictionary.')

    parser.add_argument('--num_mutants_set', action='store',
                        dest='num_mutants_set',
                        type=int,
                        default=5,
                        help='number of mutants sets.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results

if __name__ == "__main__":

    num_mutants_set = parserCommad().num_mutants_set
    for mutant_set_index in range(1, num_mutants_set+1):

        f = open(parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/res_execute_mutant.txt", 'r')
        list_execute_mutant = f.read().split('\n')[0:-1]
        f.close()

        f = open(parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/res_record.txt", 'r')
        list_mutant_record = f.read().split('\n')[0:-1]
        f.close()

        with open(parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/all_execute_mutant.txt", 'w') as f:
            f.write("")   # create and clean all_execute_mutant.txt
            f.close()

        f = open(parserCommad().RQ1_mutant_path + "mutant_set_" + str(mutant_set_index) + "/all_execute_mutant.txt", 'a')
        for i in range(len(list_execute_mutant)):
            f.write("Mutant_index: " + list_execute_mutant[i] + list_mutant_record[int(list_execute_mutant[i])-1] + '\n')
        f.close()
