# Problem Set # 3 - Day 1

csep = "\t\t"
cssep = "\t"

# open text file
textFile = open("PS03_ILP.txt", "w")

employeeName = str(input("Enter employee name: "))
rendredHours = float(input("Enter rendered hours: "))
ratePerHour = float(input("Enter rate per hour: "))
sssContribution = float(input("Enter SSS contribution: "))
phContribution = float(input("Enter PhilHealth contribution: "))
loanAmount = float(input("Enter loan amount: "))

# compute gross
gross = round(rendredHours * ratePerHour, 2)
# compute contri
totalContributions = round(sssContribution + phContribution + loanAmount,2)
# compute tax
tax = round(gross * 0.10, 2)
# compute deductions
totalDeductions = round(totalContributions + tax, 2)
# compute NET
net = round(gross - totalDeductions, 2)

print("=====\t PAYSLIP \t =====", file = textFile)
print(file = textFile)
print("=====\t EMPLOYEE INFO \t =====", file = textFile)
print("Employee Name:", employeeName, sep = csep, file = textFile)
print("Rendered Hours:", rendredHours, sep = csep, file = textFile)
print("Rate per Hour:", ratePerHour, sep = csep, file = textFile)
print("Gross Salary:", gross, sep = csep, file = textFile)

print(file = textFile)
print("=====\t DEDUCTIONS \t =====", file = textFile)
print("SSS:", sssContribution, sep = csep, file = textFile)
print("PhilHealth:", phContribution, sep = cssep, file = textFile)
print("Loans:", loanAmount, sep = csep, file = textFile)
print("Tax:", tax, sep = csep, file = textFile)
print("Total:", totalDeductions, sep = csep, file = textFile)

print(file = textFile)
print("=====\t NET SALARY \t =====", file = textFile)
print("Php", net, sep = csep, file = textFile)

#close textFile
textFile.close()


