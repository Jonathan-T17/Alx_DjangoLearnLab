# daily_reminder.py
# Personal Daily Reminder
# This program reminds users of their daily priority tasks.


# prompt the user for a task and its priority
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# using match-case for priority-based reminders
match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' is HIGH priority."
        print(reminder)
    case "medium":
        reminder = f"Reminder: Your task '{task}' is MEDIUM priority."
        print(reminder)
    case "low":
        reminder = f"Reminder: Your task '{task}' is LOW priority."
        print(reminder)

    case _:
        reminder = f"Reminder: Your task '{task}' is UNKNOWN priority."
        print(reminder)

# add time-bound note with conditional statements
if time_bound == "yes":
    reminder += " This task requires immediate attention today!\nPlease complete it on time!"

# Output final reminder
print(reminder)
