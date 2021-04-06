def collatingFaultLineRankAverage():
	f_result = open("./result_set_number.csv", 'w')

	f_result.write("test_cases_num, ,FOM_mutant, "
				   + ",ideal_second_mutant,ideal_third_mutant,ideal_fourth_mutant,ideal_fifth_mutant,"
				   + "between_second_mutant,between_third_mutant,between_fourth_mutant,between_fifth_mutant,"
				   + "worst_second_mutant,worst_third_mutant,worst_fourth_mutant,worst_fifth_mutant,"
				   + "sum_of_mutants, sum_of_compile_mutants\n")
	# v1 - v1544    one_fault
	# v1545 - v1752    two_faults
	# v1753 - v1762    three_faults
	for i in range(1, 1762+1):
		try:
			f = open("./v" + str(i) + "/output/input_list.txt", 'r')
			test_case_num = len(f.readlines())
			f_result.write(str(test_case_num))
		except FileNotFoundError:
			f_result.write("-")
		f_result.write(", ,")

		try:
			f = open("./v" + str(i) + "/output/res_fault_version.in", 'r')
			mutant_num = len(f.readlines())
			f_result.write(str(mutant_num))
		except FileNotFoundError:
			f_result.write("-")
		f_result.write(", ,")

		list_set_path = ["ideal_second_order_HOM",
						 "ideal_third_order_HOM",
						 "ideal_fourth_order_HOM",
						 "ideal_fifth_order_HOM",
						 "between_second_order_HOM",
						 "between_third_order_HOM",
						 "between_fourth_order_HOM",
						 "between_fifth_order_HOM",
						 "worst_second_order_HOM",
						 "worst_third_order_HOM",
						 "worst_fourth_order_HOM",
						 "worst_fifth_order_HOM"]
		for set_path in list_set_path:
			try:
				f = open("./v"+str(i)+"/_entire_randomization_higher_order_mutant_set/set/" + set_path + "/res_fault_version.in", 'r')
				mutant_num = len(f.readlines())
				f_result.write(str(mutant_num))
			except FileNotFoundError:
				f_result.write("-")
			f_result.write(",")
		f_result.write(" ,")

		try:
			f = open("./v"+str(i)+"/_entire_randomization_higher_order_mutant_set/res_mutant_line.txt", 'r')
			mutant_num = len(f.readlines())
			f_result.write(str(mutant_num))
		except FileNotFoundError:
			f_result.write("-")
		f_result.write(",")
		try:
			f = open("./v"+str(i)+"/_entire_randomization_higher_order_mutant_set/res_fault_version.in", 'r')
			mutant_num = len(f.readlines())
			f_result.write(str(mutant_num))
		except FileNotFoundError:
			f_result.write("-")
		f_result.write("")

		f_result.write("\n")
	f_result.close()
	

if __name__ == "__main__":

	collatingFaultLineRankAverage()
	