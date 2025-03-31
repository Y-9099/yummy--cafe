import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

# Create the main window
root = tk.Tk()
root.title("Yummy Cafe App")
root.geometry("800x600")
root.config(bg="lightblue")  # Set background color

# Global variable to hold current page
current_page = 1

# First Page - Welcome Page
def show_welcome_page():
    global current_page
    for widget in root.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(root, text="Welcome to Yummy Cafe", font=("Arial", 30, "bold"), bg="lightblue", fg="darkblue")
    welcome_label.pack(pady=100)

    next_button = tk.Button(root, text="Next", font=("Arial", 14), bg="lightgreen", fg="black", command=show_cafe_management_page)
    next_button.pack(side="bottom", pady=30)

# Second Page - Cafe Management System
def show_cafe_management_page():
    global current_page
    for widget in root.winfo_children():
        widget.destroy()

    # Function to generate QR code for payment
    def generate_qr(payment_method, amount):
        upi_id = "9607198417@ybl"
        if payment_method == "PhonePe":
            payment_url = f'upi://pay?pa={upi_id}&pn=YAMINI THAKRE&mc=1234&tid=001&amount={amount}&purpose=Order'
        elif payment_method == "Paytm":
            payment_url = f'upi://pay?pa={upi_id}&pn=YAMINI THAKRE&mc=1234&tid=001&amount={amount}&purpose=Order'
        elif payment_method == "GooglePay":
            payment_url = f'upi://pay?pa={upi_id}&pn=YAMINI THAKRE&mc=1234&tid=001&amount={amount}&purpose=Order'
        else:
            return "Invalid Payment Method"

        # Generate and show the QR code
        qr = qrcode.make(payment_url)
        qr.show()

    title_label = tk.Label(root, text="Cafe Management System", font=("Arial", 30, "bold"), bg="lightblue", fg="darkblue")
    title_label.pack(pady=20)

    menu_items = {
        "COFFEE": 30, "TEA": 20, "SANDWITCH": 70, "BURGER": 70,
        "PIZZA": 120, "FRENCHFRIES": 80, "MOMOS": 75, "NODDLES": 85,
        "CHEESECAKES": 150, "PASTRY": 50, "DONUTS": 60, "CAKES": 250,
        "MILKSHAKES": 120, "COLD_DRINKS": 50, "SOFTY": 30, "ICE_CREAMS": 50
    }

    # Function to add selected item and its price to the order list
    order = []
    def add_to_order(item):
        if len(order) < 4:
            order.append(item)
            order_list_label.config(text="Ordered Items: " + ", ".join(order))
        else:
            messagebox.showinfo("Limit Reached", "You can only order 4 items at a time.")

    menu_frame = tk.Frame(root, bg="lightblue")
    menu_frame.pack(pady=10)

    # Create buttons for each dish in the menu
    for dish, price in menu_items.items():
        button = tk.Button(menu_frame, text=f"{dish} - {price} Rs", font=("Arial", 12), width=20, height=2,
                           bg="lightgreen", fg="black", command=lambda dish=dish: add_to_order(dish))
        button.grid(row=list(menu_items.keys()).index(dish) // 4, column=list(menu_items.keys()).index(dish) % 4, padx=5, pady=5)

    order_list_label = tk.Label(root, text="Ordered Items: None", font=("Arial", 16), bg="lightblue", fg="darkblue")
    order_list_label.pack(pady=20)

    total_amount_label = tk.Label(root, text="Total Amount: 0 Rs", font=("Arial", 16), bg="lightblue", fg="darkblue")
    total_amount_label.pack(pady=10)

    def calculate_total():
        total_amount = sum(menu_items[item] for item in order)
        total_amount_label.config(text=f"Total Amount: {total_amount} Rs")
        return total_amount

    def proceed_payment():
        total_amount = calculate_total()
        payment_method = payment_choice.get()

        if total_amount == 0:
            messagebox.showwarning("Empty Order", "Please select at least one item to order.")
        else:
            if payment_method == "":
                messagebox.showwarning("No Payment Method", "Please select a payment method.")
            else:
                generate_qr(payment_method, total_amount)

    payment_choice = tk.StringVar()
    payment_choice.set("")

    payment_label = tk.Label(root, text="Select Payment Method:", font=("Arial", 14), bg="lightblue", fg="darkblue")
    payment_label.pack(pady=10)

    payment_options = ["PhonePe", "Paytm", "GooglePay", "Cash on Delivery"]
    payment_menu = tk.OptionMenu(root, payment_choice, *payment_options)
    payment_menu.config(width=20, font=("Arial", 12))
    payment_menu.pack(pady=10)

    proceed_button = tk.Button(root, text="Proceed to Payment", font=("Arial", 14), bg="lightcoral", fg="white", command=proceed_payment)
    proceed_button.pack(pady=20)

    next_button = tk.Button(root, text="Next", font=("Arial", 14), bg="lightgreen", fg="black", command=show_vehicle_number_page)
    next_button.pack(side="bottom", pady=30)

# Third Page - Vehicle Number, Phone Number, and Current Location Input
def show_vehicle_number_page():
    for widget in root.winfo_children():
        widget.destroy()

    vehicle_label = tk.Label(root, text="Enter Vehicle Number:", font=("Arial", 20, "bold"), bg="lightblue", fg="darkblue")
    vehicle_label.pack(pady=20)

    vehicle_entry = tk.Entry(root, font=("Arial", 16))
    vehicle_entry.pack(pady=10)

    # Phone Number Entry
    phone_label = tk.Label(root, text="Enter Your Phone Number:", font=("Arial", 14), bg="lightblue", fg="darkblue")
    phone_label.pack(pady=10)

    phone_entry = tk.Entry(root, font=("Arial", 16))
    phone_entry.pack(pady=10)

    # Current Location Entry
    location_label = tk.Label(root, text="Enter Your Current Location:", font=("Arial", 14), bg="lightblue", fg="darkblue")
    location_label.pack(pady=10)

    location_entry = tk.Entry(root, font=("Arial", 16))
    location_entry.pack(pady=10)

    def show_thank_you():
        vehicle_number = vehicle_entry.get()
        phone_number = phone_entry.get()
        current_location = location_entry.get()

        if vehicle_number and phone_number and current_location:
            thank_you_label = tk.Label(root, text="THANK YOU FOR PLACING YOUR ORDER", font=("Arial", 30, "bold"), bg="lightblue", fg="green")
            thank_you_label.pack(pady=100)
        else:
            messagebox.showwarning("Empty Field", "Please fill all fields before submitting.")

    submit_button = tk.Button(root, text="Submit", font=("Arial", 14), bg="lightgreen", fg="black", command=show_thank_you)
    submit_button.pack(side="bottom", pady=30)

# Initialize by showing the first page
show_welcome_page()

# Run the main loop
root.mainloop()
