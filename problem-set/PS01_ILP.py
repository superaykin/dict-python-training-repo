'''
PS01 - IKENN LOUIE PALMA
DAY 01
'''

file=textPrint = open('PS01_ILP.txt', "w")

# NAME
lastName = "PALMA"
firstName = "IKENN LOUIE"
middleName = "M"
suffix = ""
dob = "Feb. 1991"
contactNo = "09454700XXX"
address = "Brgy. Gredu, City of OBANAP"

# EDUCATIONAL BACKGROUND
elementary = "RIZAL ELEMENTARY SCHOOL"
secondary = "OBANAP NATIONAL HIGH SCHOOL"
college = "NORTH COLLEGE INC."

#skills
skills = ['computer skills', 'technical', 'drawing', 'listening', 'sleeping', 'problem solving']

#parents name
fatherName = "TATAY PALMA"
motherName = "NANAY PALMA"

#working experience
workExperience = "LGU PANABO"



# PRINTING THE INFO
print('####################################################################################', file=textPrint)
print('###########', "\t\t\t", "PERSONAL PROFILE", "\t\t\t", '###########', file=textPrint)
print('####################################################################################',  file=textPrint)
print("\n",  file=textPrint)
print("Lastname:\t\t", lastName,  file=textPrint)
print("Firstname:\t\t", firstName,  file=textPrint)
print("Middlename:\t\t", middleName,  file=textPrint)
print("Date of Birth:\t\t", dob,  file=textPrint)
print("Address:\t\t", address,  file=textPrint)
print("Skills:\t\t", skills,  file=textPrint)

print("\n",  file=textPrint)
print("\nI. PARENTS BACKGROUND:",  file=textPrint)
print("Father:\t\t", fatherName,  file=textPrint)
print("Mother:\t\t", motherName,  file=textPrint)

print("\n",  file=textPrint)
print("\nII. EDUCATIONAL BACKGROUND:",  file=textPrint)
print("\n",  file=textPrint)
print("Elementary:\t\t", elementary,  file=textPrint)
print("High School:\t\t", secondary,  file=textPrint)
print("Tertiary:\t\t", college,  file=textPrint)

print("\n",  file=textPrint)
print("\nIII. WORK EXPERIENCE:",  file=textPrint)
print("1. \t\t", college,  file=textPrint)

file=textPrint.close()