task=input("Enter your task: ")
priority=input("Enter priority (high/medium/low): ")
time_bound=input("Is it time-bound? (yes/no): ")

match (priority):
    case("high"):
        if time_bound=="yes":
            print(f"Reminder: Your high-priority task '{task}' is time-bound. Please complete it as soon as possible.")
        else:
            print(f"Reminder: Your high-priority task '{task}' is not time-bound, but should be completed soon.")
    case("medium"):
        if time_bound=="yes":
            print(f"Reminder: Your medium-priority task '{task}' is time-bound. Please plan accordingly.")
        else:
            print(f"Reminder: Your medium-priority task '{task}' is not time-bound. You can schedule it at your convenience.")
    case("low"):
        if time_bound=="yes":
            print(f"Reminder: Your low-priority task '{task}' is time-bound. Try to complete it when possible.")
        else:
            print(f"Reminder: Your low-priority task '{task}' is not time-bound. You can do it whenever you have time.")
    case _:
        print("Invalid priority or time-bound input.")      