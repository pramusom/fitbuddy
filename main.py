# FitBuddy - Your Personal Fitness Companion
# Project: TNSDC - pramusom/fitbuddy

class FitBuddy:
    def __init__(self, name):
        self.name = name
        self.workouts = []
        self.water_intake = 0
        self.calories = 0

    def log_workout(self, exercise, duration_min):
        self.workouts.append({"exercise": exercise, "duration": duration_min})
        calories_burned = duration_min * 5  # approx
        print(f"Logged: {exercise} for {duration_min} min | Burned ~{calories_burned} kcal")
    
    def log_water(self, glasses):
        self.water_intake += glasses
        print(f"Water intake: {self.water_intake} glasses")

    def log_meal(self, food, calories):
        self.calories += calories
        print(f"Meal: {food} | Calories: {calories} | Total today: {self.calories}")

    def daily_summary(self):
        total_workout_time = sum(w['duration'] for w in self.workouts)
        print(f"\n--- FitBuddy Daily Summary for {self.name} ---")
        print(f"Workouts done: {len(self.workouts)}")
        print(f"Total workout time: {total_workout_time} min")
        print(f"Water: {self.water_intake} glasses")
        print(f"Calories intake: {self.calories} kcal")
        print("Keep going! Consistency is key.")

    def suggest_workout(self, goal="fitness"):
        plans = {
            "weight_loss": ["30 min Cardio", "15 min HIIT", "20 min Brisk Walk"],
            "muscle_gain": ["Push-ups 3x15", "Squats 3x20", "Plank 3 min"],
            "fitness": ["Jumping Jacks 10 min", "Yoga 20 min", "Cycling 15 min"]
        }
        print(f"\nSuggested plan for {goal}:")
        for ex in plans.get(goal, plans["fitness"]):
            print(f" - {ex}")

def main():
    print("Welcome to FitBuddy!")
    name = input("Enter your name: ")
    user = FitBuddy(name)
    
    while True:
        print("\n1. Log Workout  2. Log Water  3. Log Meal  4. Suggest Workout  5. Summary  6. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            ex = input("Exercise name: ")
            dur = int(input("Duration (min): "))
            user.log_workout(ex, dur)
        elif choice == "2":
            g = int(input("Glasses of water: "))
            user.log_water(g)
        elif choice == "3":
            food = input("Food name: ")
            cal = int(input("Calories: "))
            user.log_meal(food, cal)
        elif choice == "4":
            goal = input("Goal (weight_loss/muscle_gain/fitness): ")
            user.suggest_workout(goal)
        elif choice == "5":
            user.daily_summary()
        elif choice == "6":
            user.daily_summary()
            print("Goodbye! Stay Fit with FitBuddy!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
