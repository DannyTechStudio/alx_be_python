task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is not time-bound.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium prority task and it's time-bound.")
        else:
            print(f"'{task}' is a medium priority task and it's not time-bound.")
    case "low":
        print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invaild priority!")
