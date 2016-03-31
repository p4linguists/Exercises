inp=input('Enter word: ')
# lex مجموعه اي از صورت مفرد تمام کلمات
lex=['کتاب','اژدها','نبات','عنان']
# jam مجموعه اي از اسم هاي جمع
jam=['مردم','ملت','لشکر']
# mks مجموعه اي از جمع هاي مکسر
mks=['اساتيد','مبالغ','اقلام']
if inp[-2:] in ['ها','ان','ات']:
    if inp not in lex:
        print('جمع')
    else:
        print('مفرد')
elif inp in jam:
    print ('اسم جمع')
elif inp in mks:
    print ('جمع مکسر')
else:
    print('مفرد')
