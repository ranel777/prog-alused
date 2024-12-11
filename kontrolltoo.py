import tkinter as tk
def calculate_bmr(sex, weight, height, age):
    """
    Arvutab baasainevahetuse (BMR) vastavalt soo, kaalu, pikkuse ja vanuse põhjal.
    
    :param sex: 'male' või 'female'
    :param weight: kaal kilogrammides
    :param height: pikkus sentimeetrites
    :param age: vanus aastates
    :return: BMR väärtus
    """
    if sex == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    return bmr

def calculate_daily_calories(bmr, activity_level):
    """
    Arvutab päevased kalorivajadused vastavalt BMR-ile ja aktiivsustasemele.
    
    :param bmr: baasainevahetuse väärtus
    :param activity_level: aktiivsustegur
    :return: päevased kalorid
    """
    return bmr * activity_level

def get_activity_level():
    """
    Küsib kasutajalt aktiivsustaset ja tagastab vastava teguri.
    
    :return: aktiivsustegur
    """
    print("Vali oma aktiivsustase:")
    print("1. Istuv eluviis (×1.2)")
    print("2. Väike aktiivsus (×1.375)")
    print("3. Mõõdukas aktiivsus (×1.55)")
    print("4. Kõrge aktiivsus (×1.725)")
    print("5. Väga kõrge aktiivsus (×1.9)")
    
    choice = int(input("Sisesta valik (1-5): "))
    activity_factors = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }
    return activity_factors.get(choice, 1.2)

def main():
    print("Tere tulemast kalorite kalkulaatorisse!")
    print("Autor: Teie Nimi")
    
    while True:
        age = int(input("Sisesta oma vanus (aastates): "))
        sex = input("Sisesta oma sugu (male/female): ").lower()
        weight = float(input("Sisesta oma kaal (kg): "))
        height = float(input("Sisesta oma pikkus (cm): "))
        
        activity_level = get_activity_level()
        
        bmr = calculate_bmr(sex, weight, height, age)
        daily_calories = calculate_daily_calories(bmr, activity_level)
        
        print(f"Teie päevane kalorivajadus on: {daily_calories:.2f} kcal")
        
        # Makrotoitainete jaotus
        protein = daily_calories * 0.20 / 4  # 20% valku
        fat = daily_calories * 0.30 / 9      # 30% rasva
        carbs = daily_calories * 0.50 / 4    # 50% süsivesikuid
        
        print(f"Makrotoitainete jaotus:")
        print(f"Valgud: {protein:.2f} g")
        print(f"Rasvad: {fat:.2f} g")
        print(f"Süsivesikud: {carbs:.2f} g")
        
        cont = input("Kas soovite jätkata? (jah/ei): ").lower()
        if cont != 'jah':
            break

if __name__ == "__main__":
    main()