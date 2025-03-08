'''
Program: customdino
Author: Madisyn Nutt
Last edited: 3/8/2025
This GUI program accepts input for customer information and a custom order.
The item can be seleted from a list of options and colors can be chosen from provided options
'''

#Import tkinter and messagebox
import  tkinter as tk
from tkinter import messagebox

#Function to create a label
def createLabel(parent, text, fontSize=12):
    label = tk.Label(parent, text=text, font=('Arial', fontSize))
    label.pack()
    return label

#Function to create an entry box
def createEntry(parent):
    entry = tk.Entry(parent)
    entry.pack()
    return entry

#Function to create a button
def createButton(parent, text, command):
    button = tk.Button(parent, text=text, command=command)
    button.pack()
    return button

#Function to create an option menu
def createDrop(parent, clicked, options):
    drop = tk.OptionMenu(parent, clicked, *options)
    drop.pack()
    return drop

#Function to create an exit button
def createExitButton(parent, text, command):
    button = tk.Button(parent, text=text, command=command)
    button.pack()
    return button
   

#Class to create the first window
class CustomerInfo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x700")
        self.title("Custom Order Form")

#Add business logo and print an error if it cannot be loaded
        try:
            self.logo = tk.PhotoImage(file="logo.png")
            logoLabel = tk.Label(self, image=self.logo)
            logoLabel.pack(pady=5)
        except Exception as e:
            messagebox.showerror("Error loading image" + e)

#Add entry boxes for customer information, with labels above each

        createLabel(self, "Custom Dinosaur", 30).pack(pady=10)
        createLabel(self, "Customer Information", 20).pack(pady=5)

        createLabel(self, "First Name:")
        self.firstName = createEntry(self)

        createLabel(self, "Last Name:")
        self.lastName = createEntry(self)

        createLabel(self, "Email:")
        self.email = createEntry(self)

        createLabel(self, "Phone:")
        self.phone = createEntry(self)
#Button to prcoceed to next window, using the callback funtion next
        createButton(self, "Next", self.next).pack(pady=5)
#Exit button, using the callback funtion exit
        createButton(self, "Exit", self.exit).pack(pady=5)

#Function for next button. Collects entered data and store to in variables
    def next(self):
        firstName = self.firstName.get()
        lastName = self.lastName.get()
        email = self.email.get()
        phone = self.phone.get()

#Input validation. Ensures entry boxes are not empty
        if not firstName or not lastName or not email or not phone:
            messagebox.showwarning("Missing information", "Please fill all fields")
            return

        self.customerName = firstName + lastName
        self.customerEmail = email
        self.customerPhone = phone
        
#Close current window and opens next window
        self.withdraw()
        itemInfoWindow = ItemInfo(self.customerName, self.customerEmail, self.customerPhone)
        itemInfoWindow.deiconify()

#Funtion for exit button. Stops program and closes window
    def exit(self):
        self.quit()
        self.destroy()
        
#Class to create second window
class ItemInfo(tk.Toplevel):
    def __init__(self, customerName, email, phone):
        super().__init__()

        self.geometry("500x700")
        self.title("Custom Order Form")

#Add product pictures and print error if it cannot be loaded
        try:
            self.dino = tk.PhotoImage(file="dino.png")
            dinoLabel = tk.Label(self, image=self.dino)
            dinoLabel.pack(pady=5)
        except Exception as e:
            messagebox.showerror("Error loading image" + e)

        createLabel(self, "Custom Dinosaur", 20).pack(pady=10)

#Create product label and an option menu for item selection and primary and secondayr colors
        createLabel(self, "Select item").pack(pady=5)

#List of avaliable products
        products = ["Brontosaurus", "T-rex", "Stegosaurus"]
        self.product = tk.StringVar()
        self.product.set("Select")
        createDrop(self, self.product, products).pack()

        createLabel(self, "Select primary color").pack(pady=5)
#List of color options for main color
        primary = ["Blue", "Green", "Pink", "Purple", "Orange", "Red"]
        self.prime = tk.StringVar()
        self.prime.set("Select")
        createDrop(self, self.prime, primary).pack()

        createLabel(self, "Select secondary color").pack(pady=5)

#List of color options for secondary color
        secondary = ["Blue", "Green", "Pink", "Purple", "Orange", "Red"]
        self.sec = tk.StringVar()
        self.sec.set("Select")
        createDrop(self, self.sec, secondary).pack()

#Button to add item to order using the callback function createItem
        createButton(self, "Add", command =self.createItem).pack(pady=5)

#Button to finish order using the callback funtion finish
        createButton (self, "Finish", command =self.finish).pack(pady=5)

#Exit button, using the callback funtion exit
        createButton(self, "Exit", self.exit).pack(pady=5)

#Create empty list to store order data        
        self.order = []

#Create listbox to display created items
        self.orderListbox = tk.Listbox(self)
        self.orderListbox.pack(pady=10, padx=20)

#Function to create an item using user selections    
    def createItem(self):
        product = self.product.get()
        primary = self.prime.get()
        secondary = self.sec.get()

#Input validation. Prevents an item from being added if all slections are not made
        if product == "Select" or primary == "Select" or secondary == "Select":
            messagebox.showwarning("Missing Selection", "Please make all selections")
            return
#Add created item to the order list        
        self.order.append((product, primary, secondary))

#Create a string representation of the item and create a label
        orderLabel = str("Item added! " + product + ", Main color: " + primary + ", Secondary Color: " + secondary)
        self.orderListbox.insert(tk.END, orderLabel)

#Function for finish button, ensures at least one item has been added
    def finish(self):
        if not self.order:
            messagebox.showwarning("No items were added", "Please add an item to place an order")
            return

#Create an empty string for the order summary
        orderSummary = ""

#Add each item for the order list to the orderSummary string        
        for item in self.order:
            orderSummary += item[0] + " - " + item[1] + " - " + item[2] + "\n"

#Create messagebox with orderSummary string
        messagebox.showinfo("Order Summary", orderSummary + "Thank you")

#Close window
        self.destroy()
        
#Funtion for exit button. Stops program and closes window
    def exit(self):
        self.quit()
        self.destroy()

    
#Run mainloop
if __name__ == "__main__":
    app = CustomerInfo()
    app.mainloop()
