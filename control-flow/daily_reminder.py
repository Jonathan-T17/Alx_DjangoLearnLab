# daily_reminder.py
# Personal Daily Reminder
# This program reminds users of their daily priority tasks.

# Prompt the user for a task and its priority
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for priority-based reminder
match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Reminder: Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Reminder: Your task '{task}' is LOW priority."
    case _:
        reminder = f"Reminder: Your task '{task}' has UNKNOWN priority."

# Add time-bound note with conditional statements
if time_bound == "yes":
    reminder += " That requires immediate attention today!"

# Output the customized reminder
print(reminder)
