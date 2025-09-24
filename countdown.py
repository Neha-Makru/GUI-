from tkinter import *
import datetime

root = Tk()
root.title("Countdown to Your Deadline!")
root.geometry("400x200")
root.configure(bg="#2c3e50")

def calculate_time_left():
    e = user_input.get()
    
    try:
        deadline_date = datetime.datetime.strptime(e.strip(), "%d/%m/%Y")
    except ValueError:
        l.config(text="Please enter the date in the format dd/mm/yyyy", fg="#e74c3c")
        return

    today_date = datetime.datetime.today()
    time_left = deadline_date - today_date
    
    days_left = time_left.days

    if days_left >= 0:
        l.config(text=f"Only {days_left} days left!", fg="#2ecc71")
    else:
        l.config(text=f"The deadline passed {abs(days_left)} days ago.", fg="#e74c3c")

main_frame = Frame(root, bg="#2c3e50")
main_frame.pack(expand=True)

user_input = Entry(main_frame, width=30, font=("Helvetica", 14), bd=0, relief="flat", justify="center")
user_input.insert(0, "Enter date (dd/mm/yyyy)")
user_input.bind("<FocusIn>", lambda event: user_input.delete(0, "end"))
user_input.pack(pady=10)

calculate_button = Button(main_frame, text="Calculate Days Left", command=calculate_time_left, 
                          fg='white', bg="#3498db", activebackground="#2980b9", 
                          font=("Helvetica", 12, "bold"), bd=0, relief="flat", padx=15, pady=5)
calculate_button.pack(pady=5)

l = Label(main_frame, text="", bg="#2c3e50", font=("Helvetica", 16, "bold"))
l.pack(pady=10)

root.mainloop()
