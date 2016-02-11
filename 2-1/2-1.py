grades=[]
grades.append(float(input('CourseA grade? ')))
grades.append(float(input('CourseB grade? ')))
grades.append(float(input('CourseC grade? ')))
avg= sum(grades)/len(grades)
print('Your average is '+str(round(avg,2)))
