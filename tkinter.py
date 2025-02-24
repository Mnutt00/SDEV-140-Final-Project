import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Custom Order Form")

label = tk.Label(root, text="Custom Order Form", font=('Arial', 18))
label.pack(padx=20, pady=20)


fNameLabel = tk.Label(root, text="First Name:")
fNameLabel.pack()
fNameEntry = tk.Entry(root)
fNameEntry.pack()

lastNameLabel = tk.Label(root, text="Last Name:")
lastNameLabel.pack()
lastNameEntry = tk.Entry(root)
lastNameEntry.pack()

emailLabel = tk.Label(root, text="Email:")
emailLabel.pack()
emailEntry = tk.Entry(root)
emailEntry.pack()

mobileLabel = tk.Label(root, text="Mobile:")
mobileLabel.pack()
mobileEntry = tk.Entry(root)
mobileEntry.pack()






root.mainloop()
