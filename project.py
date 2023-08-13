import tkinter as tk
from typing import Optional

class ShopMenuGUI:
    """
    A simple shop menu GUI application using tkinter.
    """

    def __init__(self, window: tk.Tk):
        """
        Initializes the GUI for the shop menu.

        Args:
            window (tk.Tk): The main window of the GUI.
        """
        self.window = window
        self.window.title("Shop Menu")

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Set the window size
        window_width = int(screen_width / 4)
        window_height = int(screen_height / 4)
        window_geometry = f"{window_width}x{window_height}+{window_width // 4}+{window_height // 4}"
        self.window.geometry(window_geometry)

        # Title
        self.frame_title = tk.Frame(self.window)
        self.label_title = tk.Label(self.frame_title, text='MENU', font=('Helvetica', 18, 'bold'), anchor='center')
        self.label_title.pack(pady=10)
        self.frame_title.pack()

        # Shop button
        self.frame_buttons = tk.Frame(self.window)
        self.button_shop = tk.Button(self.frame_buttons, text='Shop', command=self.open_shop_menu)
        self.button_shop.pack(side='left', padx=10, pady=5)
        self.frame_buttons.pack()

        # Variables to store quantity and price
        self.cookie_quantity = tk.StringVar()
        self.sandwich_quantity = tk.StringVar()
        self.water_quantity = tk.StringVar()

        self.cookie_price = 1.5
        self.sandwich_price = 4.0
        self.water_price = 1.0

        # Final Total bar
        self.total_label = tk.Label(self.window, text="Final Total: $0.00", font=('Helvetica', 14))
        self.total_label.pack(pady=10)

    def open_shop_menu(self):
        """
        Opens the shop menu with input fields for items.
        """
        self.frame_buttons.pack_forget()

        # Shop Menu Frame
        self.frame_shop = tk.Frame(self.window)

        # Cookie input
        self.label_cookie = tk.Label(self.frame_shop, text="Cookie - $1.50")
        self.label_cookie.grid(row=0, column=0, padx=10, pady=5)
        self.entry_cookie = tk.Entry(self.frame_shop, textvariable=self.cookie_quantity, width=10)
        self.entry_cookie.grid(row=0, column=1, padx=10, pady=5)

        # Sandwich input
        self.label_sandwich = tk.Label(self.frame_shop, text="Sandwich - $4.00")
        self.label_sandwich.grid(row=1, column=0, padx=10, pady=5)
        self.entry_sandwich = tk.Entry(self.frame_shop, textvariable=self.sandwich_quantity, width=10)
        self.entry_sandwich.grid(row=1, column=1, padx=10, pady=5)

        # Water input
        self.label_water = tk.Label(self.frame_shop, text="Water - $1.00")
        self.label_water.grid(row=2, column=0, padx=10, pady=5)
        self.entry_water = tk.Entry(self.frame_shop, textvariable=self.water_quantity, width=10)
        self.entry_water.grid(row=2, column=1, padx=10, pady=5)

        # Calculate button
        self.button_calculate = tk.Button(self.frame_shop, text="Calculate", command=self.calculate_total)
        self.button_calculate.grid(row=3, column=0, padx=10, pady=5)

        # Back button
        self.button_back_shop = tk.Button(self.frame_shop, text='Back', command=self.back_shop_menu)
        self.button_back_shop.grid(row=3, column=1, padx=10, pady=5)

        self.frame_shop.pack(pady=20)

    def back_shop_menu(self):
        """
        Returns to the main shop menu.
        """
        self.frame_shop.pack_forget()
        self.frame_buttons.pack()

    def calculate_total(self):
        """
        Calculates and displays the total price of selected items.
        """
        try:
            # Get quantity values
            cookie_qty = int(self.cookie_quantity.get())
            sandwich_qty = int(self.sandwich_quantity.get())
            water_qty = int(self.water_quantity.get())

            # Validate input: Check if any quantity is negative or not valid
            if cookie_qty < 0 or sandwich_qty < 0 or water_qty < 0:
                raise ValueError("Invalid input: Quantity cannot be negative")

            # Calculate total price
            total = (cookie_qty * self.cookie_price) + \
                    (sandwich_qty * self.sandwich_price) + \
                    (water_qty * self.water_price)

            # Update total label
            self.total_label.config(text=f"Total: ${total:.2f}")

        except ValueError:
            self.total_label.config(text="Invalid input")

def main():
    root = tk.Tk()
    root.resizable(False, False)  # Make the GUI non-resizable
    gui = ShopMenuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
