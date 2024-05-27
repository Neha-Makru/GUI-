from tkinter import *
import datetime

root = Tk()
root.title("Your Timer Program!")

def calculate_time_left():
    e = user_input.get()
    input_list = e.split(":")
    goal = input_list[0]
    deadline = input_list[1]

    try:
        deadline_date = datetime.datetime.strptime(deadline.strip(), "%d.%m.%Y")
    except ValueError:
        l.config(text="Please enter the date in the format dd.mm.yyyy")
        return

    today_date = datetime.datetime.today()

    time_left = deadline_date - today_date
    l.config(text=f"The time left before your goal '{goal.strip()}' is to be reached is: {time_left}")

user_input = Entry(root, width=50)
user_input.pack(pady=10)

calculate_button = Button(root, text="Calculate Time Left", command=calculate_time_left, fg='white', bg='black')
calculate_button.pack(pady=5)

l = Label(root, text="")
l.pack(pady=10)

root.mainloop()
