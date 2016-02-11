"""
BMI= Body Mass Index | شاخص توده بدن
برای محاسبه بي.ام.آي. وزن به کیلوگرم
را تقسیم بر مجذور قد به متر می‌کنیم.
BMI<18.5 کمبود وزن
18.5<BMI<25 وزن طبیعی
25<BMI<30 چاقی کم تا متوسط
30<BMI چاقی مفرط
"""
wk=float(input('Enter weight (kg): '))
hcm=float(input('Enter height (cm): '))
bmi=wk/(hcm*0.01)**2
print('Your BMI= '+str(round(bmi,2)))
