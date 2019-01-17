# Avg Grade Function | Revised | December 2018

grade_list = []

def getGrade(grade_list):

    while True:
        max_grade = 100
        grade = input("Enter grade, otherwise press enter key to exit: ")
        if grade == "":
            break
        elif grade.isdigit() or "." in grade:
            if grade == ".":
                print("That's not a valid grade!")
                continue
            else:
                grade = float(grade)
                if grade <= max_grade:
                    grade_list.append(grade)
                elif grade == 666:
                    print("If you say so... >:)")
                    grade_list.append(grade)
                else:
                    verify = input("Are you sure \""+str(grade)+"\" is the correct grade?: ")
                    if verify.lower() == "yes" or verify.lower() == "y":
                        grade_list.append(grade)
                    else:
                        print("Grade was not added to list. ")
        else:
            print("That's not a valid grade")


def averageGrade(grade_list):
    total = 0
    for grade in grade_list:
        total += grade
    average = total / len(grade_list)
    return average

def main(grade_list):

    getGrade(grade_list)
    avg = averageGrade(grade_list)
    stra = str(avg)
    maximum = max(grade_list)
    minimum = min(grade_list)
    print("Highest Grade: "+str(maximum)+" | Lowest Grade: "+str(minimum))
    print("Your average grade is ", stra[:5]+"%")

main(grade_list)