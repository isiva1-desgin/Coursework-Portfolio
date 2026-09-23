
Age = input("Please enter your age: ")
num_age = int(Age)

Weight = input("Please enter your weight in pounds: ")
num_weight = int(Weight)

Heart_Rate = input("Please enter you heart rate in beats per minute: ")
num_HR = int(Heart_Rate)

Time = input("Please enter the length of your workout in minutes: ")
num_time = int(Time)

calories_burned = ((num_age * 0.2757) + (num_weight * 0.03295) + (num_HR * 1.0781) - 75.4991) * (num_time) * (1/8.368)

print(f"Calories burned: {calories_burned:.2f} calories")
