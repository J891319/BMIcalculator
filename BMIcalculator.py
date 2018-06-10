name0 = input('What is the patient\'s name?')
weight_kg0 = input('What is the weight of the patient? (kg)')
height_m0 = input('What is the height of the patient? (m)')

def bmi(name, weight_kg, height_m):
    bmi = int(weight_kg) / (int(height_m) ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    elif bmi > 25:
        return name + " is overweight"


result0 = bmi(name0, weight_kg0, height_m0)

print(result0)
