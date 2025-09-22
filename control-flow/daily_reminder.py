# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case to handle priority
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Try to complete it as soon as possible.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Plan to work on it soon.")
    
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that still requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")

print("Well done on completing this project! Let the world hear about this milestone achieved.")

