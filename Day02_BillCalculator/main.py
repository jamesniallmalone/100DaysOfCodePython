total_bill = float(input("Please enter bill total: €"))
numchar = int(input("Please enter percentage for tip: "))
total_diners = int(input("Please enter number of diners: "))

individual_bill = total_bill / total_diners
individual_total = individual_bill + (individual_bill * numchar / 100)

individual_float = "{:.2f}".format(individual_total)
print("Each person owes : €" + str(individual_float))