task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ")
time_bound =input("Is it time-bound? (yes/no): ")

match (priority):
    case("high"):
        if time_bound=="yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: Your high-priority task {task} is not time-bound, but should be completed soon.")
    case("medium"):
        if time_bound=="yes":
            print(f"Reminder: Your medium-priority task {task} is time-bound. Please plan accordingly.")
        else:
            print(f"Reminder: Your medium-priority task {task} is not time-bound. You can schedule it at your convenience.")
    case("low"):
        if time_bound=="yes":
            print(f"Reminder: Your low-priority task {task} is time-bound. Try to complete it when possible.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority or time-bound input.")      