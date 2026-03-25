# Python Project - Input of rowing data to calculate pace, calories burned, and set a 12k goal

import csv
import os
from datetime import date

class RowingSession:
    def __init__(self, meters, my_time, weight, carbs, workout_date=None):
        self.meters = meters
        self.my_time = my_time
        self.weight = weight
        #self.MET = MET
        self.carbs = carbs

        if workout_date is None:
            self.workout_date = date.today()
        else:
            self.workout_date = workout_date

    def calculate_performance(self):
        # calculate peformance 500 meter split and watts
        pace = (self.my_time / (self.meters / 500))
        watts = (2.80 / (pace / 500) ** 3)

        # created dictionary because using two values in a return statement creates a tuple
        return {"pace": pace, "watts": watts}
    
    def calculate_kcal_burned(self):
        # convert pounds to kilograms
        weight_in_kg = self.weight / 2.20462
        
        # convert my_time from seconds to minutes
        time_in_minutes = self.my_time / 60

        adjusted_MET = self.calculate_base_MET(performance['watts'])
        print(adjusted_MET)

        # calculate the calories burned
        kcal_per_minute = (adjusted_MET * 3.5 * weight_in_kg) / 200
        kcal = kcal_per_minute * time_in_minutes
        return kcal
    
    def calculate_base_MET(self, watts):
        # convert pounds to kilograms
        weight_in_kg = self.weight / 2.20462

        # caculate vo2 -> standard rowing formula
        vo2 = (2.8 * watts) / weight_in_kg + 3.5

        # calculate base MET
        base_MET = vo2 / 3.5
        
        # add multiplier of 4 to get the correct MET of workout
        return round(base_MET * 4, 2)

    def is_keto_burn(self):
        # check to see if you are in keto burn
        if self.carbs < 50:
            print('You are in Keto Burn!')
        else:
            print('Eat less carbs to get to Keto Burn!')
    
    @staticmethod
    def get_rowing_input(prompt):
        while True:
            user_input = input(prompt)
            try:
                # convert user input to integer
                value = int(user_input)

                # check for negative values
                if value < 0:
                    print('Input cannot be negative!')
                    continue
                return value
            except ValueError:
                print('Invalid Input! Please enter a numeric whole number.')

    def save_to_log(self, data_dict):
        file_name = 'rowing_history.csv'

        # defining headers for row dictionary and the headers must match
        headers = ['date', 'meters', 'pace', 'watts', 'kcal', 'weight']

        # checking to see if file exists
        file_exists = os.path.isfile(file_name)

        # open file and append new data to the file with a newline
        with open(file_name, mode='a', newline='') as csvfile:
            # create a DictWriter object and specify the fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=headers)

            # write header only if it is brand new
            if not file_exists:
                writer.writeheader()

            # write the session row
            writer.writerow(data_dict)
        
        print(f"Successfully logged data to {file_name}")

# Take input data from users
meters = RowingSession.get_rowing_input('Enter meters rowed: ')
my_time = RowingSession.get_rowing_input('Enter time in seconds: ')
weight = RowingSession.get_rowing_input('Enter your weight in pounds: ')
#MET = RowingSession.get_rowing_input('Enter your MET: ')
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