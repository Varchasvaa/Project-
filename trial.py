import customtkinter as ctk
from datetime import datetime ,timedelta 
urrent_date = datetime.now()
coming_day_date = urrent_date + timedelta(days=1)
day_of_week = coming_day_date.strftime("%A")  # Full weekday name (e.g., "Monday")
date_of_coming_day = coming_day_date.date()   # Date object of the coming day

# Print the results
print(f"Day: {day_of_week}")
print(f"Date: {date_of_coming_day}")
# Extract the day and date
 
# # Initialize CustomTkinter
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# # Create the main application window
# app = ctk.CTk()
# app.geometry("400x300")

# # Function to create a forced pop-up window
# def open_forced_popup():
#     # Create a pop-up window
#     popup = ctk.CTkToplevel(app)
#     popup.geometry("300x200")
#     popup.title("Forced Pop-Up")

#     # Make the pop-up modal (force interaction with it)
#     popup.grab_set()  # Prevent interaction with the main window
#     popup.resizable(False, False)  # Optional: disable resizing
    
#     # Add a label to the pop-up
#     label = ctk.CTkLabel(popup, text="This is a forced pop-up!", font=("Arial", 16))
#     label.pack(pady=20)
    
#     # Add a button to close the pop-up
#     close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
#     close_button.pack(pady=10)

#     # Ensure the pop-up stays on top
#     popup.transient(app)

# # Force the pop-up immediately when the app starts
# app.after(100, open_forced_popup)  # Show the pop-up after 100ms (to allow main window to load)

# # Run the application
# app.mainloop()
