# importing the required module
import matplotlib.pyplot as plt #pip install matplotlib
import pandas as pd #pip install pandas

#read the csv file into dataframe format, take note about the path of the file
#listMarkDataFrame = pd.read_csv(r"C:\Users\adham\OneDrive\Desktop\projects\mark_counter\listmark.csv", delimiter = ";")
listMarkDataFrame = pd.read_csv("listmark.csv", delimiter = ";")
#assign dataframe to a list
listMark = listMarkDataFrame.values
#length of the list
listMarkLength = len(listMark)
#total credit hour
totalCreditHour = 13
creditHourList = [3, 3, 3, 2, 2];
#list of student PNGK
studentPNGKList = [];

#number of student in each grade class
firstClassStdTotal = 0
secondClassUpperStdTotal = 0
secondClassLowerStdTotal = 0
thirdClassStdTotal = 0

#number of student grade in SFG4093
SFG4093StdAplus = 0
SFG4093StdAsolid = 0
SFG4093StdAminus = 0
SFG4093StdBplus = 0
SFG4093StdBsolid = 0
SFG4093StdBminus = 0
SFG4093StdCplus = 0
SFG4093StdCsolid = 0
SFG4093StdCminus = 0
SFG4093StdDsolid = 0
SFG4093StdEsolid = 0

#number of student grade in SFS4113
SFS4113StdAplus = 0
SFS4113StdAsolid = 0
SFS4113StdAminus = 0
SFS4113StdBplus = 0
SFS4113StdBsolid = 0
SFS4113StdBminus = 0
SFS4113StdCplus = 0
SFS4113StdCsolid = 0
SFS4113StdCminus = 0
SFS4113StdDsolid = 0
SFS4113StdEsolid = 0

#number of student grade in SFB3213
SFB3213StdAplus = 0
SFB3213StdAsolid = 0
SFB3213StdAminus = 0
SFB3213StdBplus = 0
SFB3213StdBsolid = 0
SFB3213StdBminus = 0
SFB3213StdCplus = 0
SFB3213StdCsolid = 0
SFB3213StdCminus = 0
SFB3213StdDsolid = 0
SFB3213StdEsolid = 0

#number of student grade in SFF4422
SFF4422StdAplus = 0
SFF4422StdAsolid = 0
SFF4422StdAminus = 0
SFF4422StdBplus = 0
SFF4422StdBsolid = 0
SFF4422StdBminus = 0
SFF4422StdCplus = 0
SFF4422StdCsolid = 0
SFF4422StdCminus = 0
SFF4422StdDsolid = 0
SFF4422StdEsolid = 0

#number of student grade in SFC3312
SFC3312StdAplus = 0
SFC3312StdAsolid = 0
SFC3312StdAminus = 0
SFC3312StdBplus = 0
SFC3312StdBsolid = 0
SFC3312StdBminus = 0
SFC3312StdCplus = 0
SFC3312StdCsolid = 0
SFC3312StdCminus = 0
SFC3312StdDsolid = 0
SFC3312StdEsolid = 0

#to calculate the PNGK for each student
#print the header in console
print(f"{'Matric':<10}{'Name':<25}{'PNGK':<20}")
for i in range(listMarkLength):
    totalAllgradePointerPerStudent = 0
    creditHourListIndex = 0
    for j in range(3, 8):
        #get the mark for each subject from each student
        value = float(listMark[i][j])
        if value >= 90:
            gradePointer = 4.00
        elif value >= 80:
            gradePointer = 4.00
        elif value >= 75:
            gradePointer = 3.75
        elif value >= 70:
            gradePointer = 3.50
        elif value >= 65:
            gradePointer = 3.00
        elif value >= 60:
            gradePointer = 2.75
        elif value >= 55:
            gradePointer = 2.50
        elif value >= 50:
            gradePointer = 2.00
        elif value >= 45:
            gradePointer = 1.75
        elif value >= 40:
            gradePointer = 1.00
        else:
            gradePointer = 0
        
        #accumulate all grade pointer for each subject for each student
        totalAllgradePointerPerStudent = totalAllgradePointerPerStudent + (gradePointer*creditHourList[creditHourListIndex])
        creditHourListIndex = creditHourListIndex + 1
        
    #formula used --> (total of grade * credit hour) / total credit hour
    studentPNGK = totalAllgradePointerPerStudent / totalCreditHour
    #formating to 2 decimal places
    studentPNGKRounded = format(studentPNGK, ".2f")
    #add to studentPNGKList
    studentPNGKList.insert(i, studentPNGKRounded)
    #formating to print in console
    print(f"{listMark[i][1]:<10}{listMark[i][2]:<25}{studentPNGKRounded:<20}")

#create a graph for student grade
#get the student PNGK list
studentPNGKListLength = len(studentPNGKList)
#calculate student graduation class
for i in range(studentPNGKListLength):
    PNGKValue = float(studentPNGKList[i])
    if PNGKValue >= 3.67:
        firstClassStdTotal = firstClassStdTotal + 1
    elif PNGKValue >= 3.00:
        secondClassUpperStdTotal = secondClassUpperStdTotal + 1
    elif PNGKValue >= 2.50:
        secondClassLowerStdTotal = secondClassLowerStdTotal + 1
    else:
        thirdClassStdTotal = thirdClassStdTotal + 1

# x axis values
x = ["1st Class","2nd Class Upper","2nd Class Lower", "3rd Class"]
# corresponding y axis values
y = [firstClassStdTotal, secondClassUpperStdTotal, secondClassLowerStdTotal, thirdClassStdTotal]
# plotting the points 
plt.plot(x, y)
# naming the x axis
plt.xlabel("Graduation Class")
# naming the y axis
plt.ylabel("Number of Students")
# giving a title to my graph
plt.title("Student Graduation Class Graph")
# function to show the plot
plt.show()

#create a graph of grade for each subject
#subject SFG4093
for i in range(listMarkLength):
    value = float(listMark[i][3])
    if value >= 90:
        SFG4093StdAplus+=1
    elif value >= 80:
        SFG4093StdAminus+=1
    elif value >= 75:
        SFG4093StdAsolid+=1
    elif value >= 70:
        SFG4093StdBplus+=1
    elif value >= 65:
        SFG4093StdBsolid+=1
    elif value >= 60:
        SFG4093StdBminus+=1
    elif value >= 55:
        SFG4093StdCplus+=1
    elif value >= 50:
        SFG4093StdCsolid+=1
    elif value >= 45:
        SFG4093StdCminus+=1
    elif value >= 40:
        SFG4093StdDsolid+=1
    else:
        SFG4093StdEsolid+=1

#subject SFS4113
for i in range(listMarkLength):
    value = float(listMark[i][4])
    if value >= 90:
        SFS4113StdAplus+=1
    elif value >= 80:
        SFS4113StdAminus+=1
    elif value >= 75:
        SFS4113StdAsolid+=1
    elif value >= 70:
        SFS4113StdBplus+=1
    elif value >= 65:
        SFS4113StdBsolid+=1
    elif value >= 60:
        SFS4113StdBminus+=1
    elif value >= 55:
        SFS4113StdCplus+=1
    elif value >= 50:
        SFS4113StdCsolid+=1
    elif value >= 45:
        SFS4113StdCminus+=1
    elif value >= 40:
        SFS4113StdDsolid+=1
    else:
        SFS4113StdEsolid+=1

#subject SFB3213
for i in range(listMarkLength):
    value = float(listMark[i][5])
    if value >= 90:
        SFB3213StdAplus+=1
    elif value >= 80:
        SFB3213StdAminus+=1
    elif value >= 75:
        SFB3213StdAsolid+=1
    elif value >= 70:
        SFB3213StdBplus+=1
    elif value >= 65:
        SFB3213StdBsolid+=1
    elif value >= 60:
        SFB3213StdBminus+=1
    elif value >= 55:
        SFB3213StdCplus+=1
    elif value >= 50:
        SFB3213StdCsolid+=1
    elif value >= 45:
        SFB3213StdCminus+=1
    elif value >= 40:
        SFB3213StdDsolid+=1
    else:
        SFB3213StdEsolid+=1

#subject SFF4422
for i in range(listMarkLength):
    value = float(listMark[i][6])
    if value >= 90:
        SFF4422StdAplus+=1
    elif value >= 80:
        SFF4422StdAminus+=1
    elif value >= 75:
        SFF4422StdAsolid+=1
    elif value >= 70:
        SFF4422StdBplus+=1
    elif value >= 65:
        SFF4422StdBsolid+=1
    elif value >= 60:
        SFF4422StdBminus+=1
    elif value >= 55:
        SFF4422StdCplus+=1
    elif value >= 50:
        SFF4422StdCsolid+=1
    elif value >= 45:
        SFF4422StdCminus+=1
    elif value >= 40:
        SFF4422StdDsolid+=1
    else:
        SFF4422StdEsolid+=1

#subject SFC3312
for i in range(listMarkLength):
    value = float(listMark[i][7])
    if value >= 90:
        SFC3312StdAplus+=1
    elif value >= 80:
        SFC3312StdAminus+=1
    elif value >= 75:
        SFC3312StdAsolid+=1
    elif value >= 70:
        SFC3312StdBplus+=1
    elif value >= 65:
        SFC3312StdBsolid+=1
    elif value >= 60:
        SFC3312StdBminus+=1
    elif value >= 55:
        SFC3312StdCplus+=1
    elif value >= 50:
        SFC3312StdCsolid+=1
    elif value >= 45:
        SFC3312StdCminus+=1
    elif value >= 40:
        SFC3312StdDsolid+=1
    else:
        SFC3312StdEsolid+=1

# line for SFG4093 subject
x1 = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]
y1 = [SFG4093StdAplus, SFG4093StdAminus, SFG4093StdAsolid, 
      SFG4093StdBplus, SFG4093StdBsolid, SFG4093StdBminus,
      SFG4093StdCplus, SFG4093StdCsolid, SFG4093StdCminus,
      SFG4093StdDsolid, SFG4093StdEsolid]
# plotting the SFG4093 subject points 
plt.plot(x1, y1, label = "SFG4093")
  
# line for SFS4113 subject
x2 = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]
y2 = [SFS4113StdAplus, SFS4113StdAminus, SFS4113StdAsolid, 
      SFS4113StdBplus, SFS4113StdBsolid, SFS4113StdBminus,
      SFS4113StdCplus, SFS4113StdCsolid, SFS4113StdCminus,
      SFS4113StdDsolid, SFS4113StdEsolid]
# plotting the SFS4113 subject points 
plt.plot(x2, y2, label = "SFS4113")

# line for SFB3213 subject
x3 = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]
y3 = [SFB3213StdAplus, SFB3213StdAminus, SFB3213StdAsolid, 
      SFB3213StdBplus, SFB3213StdBsolid, SFB3213StdBminus,
      SFB3213StdCplus, SFB3213StdCsolid, SFB3213StdCminus,
      SFB3213StdDsolid, SFB3213StdEsolid]
# plotting the SFS4113 subject points 
plt.plot(x3, y3, label = "SFB3213")

# line for SFF4422 subject
x4 = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]
y4 = [SFF4422StdAplus, SFF4422StdAminus, SFF4422StdAsolid, 
      SFF4422StdBplus, SFF4422StdBsolid, SFF4422StdBminus,
      SFF4422StdCplus, SFF4422StdCsolid, SFF4422StdCminus,
      SFF4422StdDsolid, SFF4422StdEsolid]
# plotting the SFF4422 subject points 
plt.plot(x4, y4, label = "SFF4422")

# line for SFC3312 subject
x5 = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]
y5 = [SFC3312StdAplus, SFC3312StdAminus, SFC3312StdAsolid, 
      SFC3312StdBplus, SFC3312StdBsolid, SFC3312StdBminus,
      SFC3312StdCplus, SFC3312StdCsolid, SFC3312StdCminus,
      SFC3312StdDsolid, SFC3312StdEsolid]
# plotting the SFC3312 subject points 
plt.plot(x5, y5, label = "SFC3312")
  
# naming the x axis
plt.xlabel("Grade")
# naming the y axis
plt.ylabel("Number of Students")
# giving a title to my graph
plt.title("Graph of Grade For Each Subject")
  
# show a legend on the plot
plt.legend()
  
# function to show the plot
plt.show()


