name0 = "James"
weight_kg0 = 70
height_m0 = 1.7

name1 = "Jack"
weight_kg1 = 70
height_m1 = 1.8

name2 = "Yaz"
weight_kg2 = 70
height_m2 = 1.75


def bmi(name, weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    elif bmi > 25:
        return name + " is overweight"


result0 = bmi(name0, weight_kg0, height_m0)
result1 = bmi(name1, weight_kg1, height_m1)
result2 = bmi(name2, weight_kg2, height_m2)

print(result0)
print(result1)
print(result2)
