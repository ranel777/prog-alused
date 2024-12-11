import tkinter as tk
from tkinter import messagebox
import random

# Funktsioon baasainevahetuse (BMR) arvutamiseks
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

# Funktsioon päevase kalorivajaduse arvutamiseks
def calculate_daily_calories(bmr, activity_level):
    """
    Arvutab päevased kalorivajadused vastavalt BMR-ile ja aktiivsustasemele.
    
    :param bmr: baasainevahetuse väärtus
    :param activity_level: aktiivsustegur
    :return: päevased kalorid
    """
    return bmr * activity_level

# Funktsioon toiduainete soovituste kuvamiseks
def food_recommendations(daily_calories, goal):
    foods = {
        "Leib": 250, "Piim (2,5%)": 50, "Juust": 350, "Värske kurk": 15, "Kartul": 85,
        "Makaronid": 110, "Piimakohv": 70, "Müsli": 370, "Riis": 130, "Tatar": 340
    }

    recommended_foods = []
    total_calories = 0
    while total_calories < daily_calories and len(recommended_foods) < 5:
        food = random.choice(list(foods.items()))
        if total_calories + food[1] <= daily_calories:
            recommended_foods.append(food)
            total_calories += food[1]

    # Kuvame soovitatud toiduained
    print("\nSoovitused toiduainete valimiseks vastavalt teie eesmärgile:")
    for food, calories in recommended_foods:
        print(f"{food}: {calories} kcal/100g")

# Graafiline kasutajaliides

def calculate_and_display():
    """
    Arvutab ja kuvab kasutaja päevase kalorivajaduse ning makrotoitainete jaotuse.
    """
    try:
        # Sisendi andmed
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        sex = sex_var.get()
        activity_level = activity_levels[activity_var.get()]
        goal = goal_var.get()

        # BMR ja kalorite arvutamine
        bmr = calculate_bmr(sex, weight, height, age)
        daily_calories = calculate_daily_calories(bmr, activity_level)
        
        # Makrotoitainete jaotus
        protein = daily_calories * 0.20 / 4  # 20% valku
        fat = daily_calories * 0.30 / 9      # 30% rasva
        carbs = daily_calories * 0.50 / 4    # 50% süsivesikuid
        
        # Kuvamine
        result_text.set(f"Päevane kalorivajadus: {daily_calories:.2f} kcal")
        protein_text.set(f"Valgud: {protein:.2f} g")
        fat_text.set(f"Rasvad: {fat:.2f} g")
        carbs_text.set(f"Süsivesikud: {carbs:.2f} g")
        
        # Toiduainete soovitused
        food_recommendations(daily_calories, goal)
        
    except ValueError:
        messagebox.showerror("Viga", "Palun sisesta kehtivad andmed kõigis väliades!")

# Graafilise liidese akna loomine
root = tk.Tk()
root.title("Kalorite Kalkulaator")
root.geometry("400x500")

# Teate sisestamine
title_label = tk.Label(root, text="Tere tulemast kalorite kalkulaatorisse!\nAutor: Ranel", font=("Arial", 14))
title_label.pack(pady=10)

# Kasutaja andmed
age_label = tk.Label(root, text="Vanus (aastates):")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

weight_label = tk.Label(root, text="Kaal (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Pikkus (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

sex_label = tk.Label(root, text="Sugu:")
sex_label.pack()

sex_var = tk.StringVar()
male_rb = tk.Radiobutton(root, text="Mees", variable=sex_var, value="male")
male_rb.pack()
female_rb = tk.Radiobutton(root, text="Naine", variable=sex_var, value="female")
female_rb.pack()

activity_label = tk.Label(root, text="Aktiivsustase:")
activity_label.pack()

activity_var = tk.StringVar()
activity_levels = {
    "1": 1.2,   # Väga madal
    "2": 1.375, # Madal
    "3": 1.55,  # Mõõdukas
    "4": 1.725, # Kõrge
    "5": 1.9    # Väga kõrge
}
activity_menu = tk.OptionMenu(root, activity_var, "1", "2", "3", "4", "5")
activity_menu.pack()

goal_label = tk.Label(root, text="Eesmärk:")
goal_label.pack()

goal_var = tk.StringVar()
goal_menu = tk.OptionMenu(root, goal_var, "kaalulangus", "kaalutõus", "kaalu hoidmine")
goal_menu.pack()

# Arvutamise nupp
calc_button = tk.Button(root, text="Arvuta", command=calculate_and_display)
calc_button.pack(pady=20)

# Tulemuste kuvamine
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

protein_text = tk.StringVar()
protein_label = tk.Label(root, textvariable=protein_text)
protein_label.pack()

fat_text = tk.StringVar()
fat_label = tk.Label(root, textvariable=fat_text)
fat_label.pack()

carbs_text = tk.StringVar()
carbs_label = tk.Label(root, textvariable=carbs_text)
carbs_label.pack()

# Käivita Tkinteri peamine tsükkel
root.mainloop()
