from _datetime import datetime

user_input = input("Enter your goal with a deadline, separated by a colon(:)\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
# calculate how many days from now till deadline
days_remaining = deadline_date - today_date

print(f"Dear user, days left for your goal: {goal} is {days_remaining.days} days")