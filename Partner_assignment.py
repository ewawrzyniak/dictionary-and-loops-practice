import student_data
students = student_data.students
# Yao Emily W 
#promt 9

name = input('Enter a last name: ')

for student in students:
    if name == student['LName']:
        print(student['Combo,Name'])
        print(student['HR'])
        print(student['GL'])
        print(student['Email'])

#prompt 11
        
MName = 0

for student in students: #THis mnakes it go throught each student
    if student['MName'] == ' ': #this checks if there are any students without a middle name 
        print(student['Combo,Name'], + 'does not have a midddle name') # This prints out who doesnt have a middle naem 
        MName = MName + 1 #This keeps track of how many students dont have a middle name

if MName > 0: #We dont need to know how many student there are rn so we only need it to be bigfger then 0 
    MName = False
else: 
    MName = True #this means that everyone has a middle name 

if MName is True: 
    print('All students have a middle name.')
#this is only nessaryif all students avem mideden so there doesntneed to be an else statment 
    


# Prompt 12 
inGrade10 = [] #this makes list of emails that need to be held

for student in students: 
    if student['GL'] == 10: #you only need if in grade 10 because the rest of the grade levels dont matter here 
        inGrade10.append(student['Email'][0])
        inGrade10.append(student['Email'][1]) #You need both of these to ensure both emails are taken 

print (*inGrade10, sep =', ') #this prints out the list of emails collected

        
