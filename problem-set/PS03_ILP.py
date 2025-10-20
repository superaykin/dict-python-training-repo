# Problem Set # 3 - Day 1

csep = "\t\t"
cssep = "\t"

employeeName = str(input("Enter employee name: "))
rendredHours = float(input("Enter rendered hours: "))
ratePerHour = float(input("Enter rate per hour: "))
sssContribution = float(input("Enter SSS contribution: "))
phContribution = float(input("Enter PhilHealth contribution: "))
loanAmount = float(input("Enter loan amount: "))

# compute gross
gross = rendredHours * ratePerHour
# compute contri
totalContributions = sssContribution + phContribution + loanAmount
# compute tax
tax = gross * 0.10
# compute deductions
totalDeductions = totalContributions + tax
# compute NET
net = round(gross - totalDeductions, 2)

print("=====\t PAYSLIP \t =====")
print()
print("=====\t EMPLOYEE INFO \t =====")
print("Employee Name:", employeeName, sep = csep)
print("Rendered Hours:", rendredHours, sep = csep)
print("Rate per Hour:", ratePerHour, sep = csep)
print("Gross Salary:", gross, sep = csep)

print()
print("=====\t DEDUCTIONS \t =====")
print("SSS:", sssContribution, sep = csep)
print("PhilHealth:", phContribution, sep = cssep)
print("Loans:", loanAmount, sep = csep)
print("Tax:", tax, sep = csep)
print("Total:", totalDeductions, sep = csep)

print()
print("=====\t NET SALARY \t =====")
print("Php", net, sep = csep)


