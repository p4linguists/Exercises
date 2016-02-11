cA=float(input('CourseA grade? '))
cB=float(input('CourseB grade? '))
cC=float(input('CourseC grade? '))
# معدل = جمع نمرات تقسيم بر تعداد نمرات
avg= (cA+cB+cC)/3
print('Your average is '+str(round(avg,2)))
"""
دستور زير به اين معناست که 
معدل را با دقت 0.01 گرد کن:
round(avg,2)
"""
