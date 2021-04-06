import os
import util
import argparse

def parserCommad():
    '''
    Get the command line parameter and return them.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--mutant_root', action='store',
                        default="./_MBFL_randomization_higher_order_mutant_set/",
                        dest='mutant_root',
                        help='mutant root dictionary.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    return results

if __name__ == "__main__":
    mutant_root = parserCommad().mutant_root

    f = open(mutant_root + "res_execute_mutant.txt", 'r')
    list_execute_mutant = f.read().split('\n')[0:-1]
    f.close()

    f = open(mutant_root + "res_record.txt", 'r')
    list_mutant_record = f.read().split('\n')[0:-1]
    f.close()

    with open(mutant_root + "all_execute_mutant.txt", 'w') as f :
        f.write("")   # create and clean all_execute_mutant.txt
        f.close()

    f = open(mutant_root + "all_execute_mutant.txt", 'a')
    for i in range(len(list_execute_mutant)):
        f.write("Mutant_index: " + list_execute_mutant[i] + "   Source_" + list_mutant_record[int(list_execute_mutant[i])-1] + '\n')
    f.close()
