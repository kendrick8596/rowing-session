# Python Project - Input of rowing data to calculate pace, calories burned, and set a 12k goal

import csv
from session import RowingSession


# Take input data from users
meters = RowingSession.get_rowing_input('Enter meters rowed: ')
my_time = RowingSession.get_rowing_input('Enter time in seconds: ')
weight = RowingSession.get_rowing_input('Enter your weight in pounds: ')
carbs = RowingSession.get_rowing_input('Enter daily carbs: ')
workout_date = input('Enter Date: ')

# Create instance of the class
session_split = RowingSession(meters, my_time, weight, carbs, workout_date)
performance = session_split.calculate_performance()
print(f"You 500 meter split pace is: {performance['pace']:.2f} in seconds.")
print(f"Power Output for session: {performance['watts']:.0f}")

kcal_burned = session_split.calculate_kcal_burned()
print(f"You burned {kcal_burned:.2f} calories this session.")

keto_check = session_split.is_keto_burn()

# Master dictionary
row_to_save = {"date": session_split.workout_date,
               "meters": session_split.meters,
               "pace": performance['pace'],
               "watts": performance['watts'],
               "kcal": kcal_burned,
               "weight": session_split.weight}

# Call the method to save the data to the file
session_split.save_to_log(row_to_save)

def print_workout_summary():
    total_meters = 0
    total_kcal = 0
    workout_count = 0

    try:
        with open('rowing_history.csv', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)

            # loop through the csv file and convert back to numbers for math
            for row in reader:
                total_meters += int(row['meters'])
                total_kcal += float(row['kcal'])
                workout_count += 1

        # print the progress report
        print("\n--- Progress Report ---")
        print(f"Total Workouts: {workout_count}")
        print(f"Total Distance: {total_meters} meters")
        print(f"Total Calories: {round(total_kcal)} kcal")

        # check against 12k weekly goal
        if total_meters >= 12000:
            print("Goal Status: 12k Weekly Goal Met!")
        else:
            print(f"Goal Status: {12000 - total_meters} meters to go for your 12k goal.")
    
    except FileNotFoundError:
        print("No log file found yet. Get rowing!")

print(print_workout_summary())