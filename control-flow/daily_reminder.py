# daily_reminder.py
# Personal Daily Reminder
# This program reminds users of their daily priority tasks.

# Prompt the user for a task and its priority
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Using match-case for priority-based reminders
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Add time-bound note with conditional statements
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority == "low":
    reminder += ". Consider completing it when you have free time."

# ✅ Print final reminder to the user
print(reminder)
