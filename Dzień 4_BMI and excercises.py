"""#FAT #BURNER
Napisz program, który na podstawie masy [kg] i wzrostu [cm] wylicza wskaźnik BMI
(https://en.wikipedia.org/wiki/Body_mass_index) oraz informuje użytkownika, w jakim jest zakresie. Zakresy można wpisać
“z palca” (ale może nieco mądrzej niż ciągiem if-elif-else dla każdego zakresu! 😉 ) albo odczytać z dowolnego API,
np. https://rapidapi.com/navii/api/bmi-calculator . Następnie program losuje jedną z aktywności fizycznych oraz czas
jej wykonania, np. bieganie przez 30 minut. Czas nie może być dłuższy niż podany przez użytkownika (maksymalny czas,
który można poświęcić na ćwiczenia). Zadbaj o to, aby czas aktywności był jakoś uzależniony od BMI (na przykład osoba
z niedowagą nie powinna ćwiczyć mniej niż osoba o wadze normalnej - ustal pewien minimalny czas; ale już osoba
z nadwagą powinna ćwiczyć dłużej - ustal odpowiedni nieliniowy mnożnik, tak aby nie przekroczyć maksimum). Utwórz
w ten sposób plan treningowy na 7 następnych dni, wyniki zapisując do pliku .txt.

Propozycja rozszerzenia: przygotuj urozmaicony plan treningowy uwzględniający maksymalny czas wpisany przez użytkownika
- kilka aktywności fizycznych ma wypełniać całą dzienną ilość czasu, mają zajmować jakąs ustaloną minimalną długość
(np. 10 minut) oraz nie mogą się powtarzać jednego dnia."""

import math
import random
import os

def bmi_calculation(mass, height):  # Provide mass in kilos and height in meters
    height = float(str(height).replace(',', '.'))
    mass = float(str(mass).replace(',', '.'))
    return mass / height**2


def data_input():
    height = input('Please enter your height (in meters)\n')
    mass = input('Please enter your mass (in kilos)\n')
    training_time = input('Please enter how much time (in minutes) you can spend for training (daily)\n')
    return {'Height': height, 'Mass': mass, 'Training time': training_time}


def bmi_check(bmi, bmi_scale):
    for key in bmi_scale:
        if bmi >= bmi_scale[key][0] and bmi <= bmi_scale[key][1]:
            print('Your BMI ({:.2f}) category is: {}'.format(bmi, key))
            return key

def random_time(exercise_time, factor):
    exe_time = random.choice(range(int(exercise_time/2), int(exercise_time))) * factor
    if exe_time <= exercise_time:
        return exe_time
    elif not exe_time:
        random_time(exercise_time, factor)
    else:
        random_time(exercise_time, factor)


if __name__ == '__main__':
    bmi_scale = {  # First two values are BMI indexes, the third one is an exercise length factor
        'Very severely underweight': [0, 15, 0.45],
        'Severely underweight': [15, 16, 0.6],
        'Underweight': [16, 18.5, 0.75],
        'Normal (healthy weight)': [18.5, 25, 0.9],
        'Overweight': [25, 30, 1.05],
        'Obese Class I (Moderately obese)': [30, 35, 1.2],
        'Obese Class II (Severely obese)': [35, 40, 1.35],
        'Obese Class III (Very severely obese)': [40, math.inf, 1.5]
    }
    exercises = ['Jogging', 'Swimming', 'Walking', 'Nordic Walking', 'Cycling', 'Volleyball', 'Tennis']
    data = data_input()  # Invoke the input section for data
    bmi = bmi_calculation(data['Mass'], data['Height'])  # Calculate BMI
    bmi_category = bmi_check(bmi, bmi_scale)  # Check which category BMI fits to
    with open('Workout plan.txt', 'w') as file:
        for d in range(1, 8):
            training = random.choice(exercises)  # Random choice of exercises
            training_length = int(random_time(int(data['Training time']), bmi_scale[bmi_category][2]))  # Training length picked base on a BMI category
            plan = 'Your exercise for day {} is: {}. Length of the exercise is: {}\n'. format(d, training, training_length)  
            file.write(plan)

    print('The plan for whole week has been saved as a file {} in {}'.format(file.name, os.getcwd()))

