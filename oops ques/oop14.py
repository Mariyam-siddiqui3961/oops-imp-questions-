# Loan Calculator using Tkinter:
# (i). Write python GUI application is developed for computing
# loan payments. The code consists of the following steps:
# 1.Design the user interface consisting of labels using Label( ),
# text entry boxes using Entry( ), and a button using Button( ).
# 2.Process the event. When the button is clicked, the
# program invokes a callback functions, using
# getMonthlyPayment( ) to obtain the user input for the
# interest rate, number of years, and loan amount from the
# text entries. The monthly and total payments are computed
# using computePayment( ) and displayed in the labels.

import tkinter as tk

def compute_payment():
    try:
        principal = float(loan_amount_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100 / 12
        years = int(years_entry.get())

        # Compute monthly payment
        monthly_payment = principal * interest_rate / (1 - (1 + interest_rate) ** (-years * 12))
        total_payment = monthly_payment * years * 12

        monthly_payment_label.config(text="Monthly Payment: ${:.2f}".format(monthly_payment))
        total_payment_label.config(text="Total Payment: ${:.2f}".format(total_payment))
    except ValueError:
        error_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Loan Calculator")

# Create labels
loan_amount_label = tk.Label(root, text="Loan Amount:")
loan_amount_label.grid(row=0, column=0, padx=10, pady=5)

interest_rate_label = tk.Label(root, text="Interest Rate (%):")
interest_rate_label.grid(row=1, column=0, padx=10, pady=5)

years_label = tk.Label(root, text="Number of Years:")
years_label.grid(row=2, column=0, padx=10, pady=5)

monthly_payment_label = tk.Label(root, text="")
monthly_payment_label.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

total_payment_label = tk.Label(root, text="")
total_payment_label.grid(row=5, column=0, padx=10, pady=5, columnspan=2)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=6, column=0, padx=10, pady=5, columnspan=2)

# Create entry boxes
loan_amount_entry = tk.Entry(root)
loan_amount_entry.grid(row=0, column=1, padx=10, pady=5)

interest_rate_entry = tk.Entry(root)
interest_rate_entry.grid(row=1, column=1, padx=10, pady=5)

years_entry = tk.Entry(root)
years_entry.grid(row=2, column=1, padx=10, pady=5)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=compute_payment)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
