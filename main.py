def bmi_hisobla(boy, vazn):
    if boy <= 0 or vazn <= 0:
        print("Xato: Bo‘y va vazn 0 dan katta bo‘lishi kerak!")
        return
    
    bmi = vazn / (boy * boy)
    print(f"BMI = {bmi:.2f}", end=", ")
    
    if bmi < 18.5:
        print("Ozganlik")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Ortiqcha vazn")
    else:
        print("Semizlik")

# Test
bmi_hisobla(1.75, 70)
# Natija: BMI = 22.86, Normal
