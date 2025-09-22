# 1. Prompt User for Input
task_description = input("Enter your task description: ")
task_priority = input("Enter the priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes/no): ")

# 2. Provide a Personalized Reminder
reminder = f"Task: {task_description}"

if task_priority == "high" and time_bound == "yes":
    reminder += " -> Priority: High, Time-bound: Yes. This is URGENT and should be done immediately."
elif task_priority == "high" and time_bound == "no":
    reminder += " -> Priority: High, Time-bound: No. This is important, schedule it soon."
elif task_priority == "medium" and time_bound == "yes":
    reminder += " -> Priority: Medium, Time-bound: Yes. This needs to be done today."
elif task_priority == "low" and time_bound == "no":
    reminder += " -> Priority: Low, Time-bound: No. This is not urgent, you can do it when you have free time."
else:
    reminder += " -> Priority: Unknown, Time-bound: Unknown. Check your task details."

# 3. Output the Reminder
print("Reminder:", reminder)