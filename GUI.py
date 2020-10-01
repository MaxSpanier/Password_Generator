import tkinter as tk
from generator import genrate_password_weak, genrate_password_strong, genrate_password_extreme

app = tk.Tk()
app.geometry("700x200")

def insertPassword():
    password_string = genrate_password_extreme(15)
    password.delete(0, "end")
    password.insert(0, password_string)

def copyPassword():
    app.clipboard_clear()
    app.clipboard_append(password.get())

def printClipboard():
    text = app.clipboard_get()
    print(text)

lengthLabel = tk.Label(text="Length: ")
lengthLabel.pack()

password = tk.Entry()
password.pack()

createBtn = tk.Button(command=insertPassword, text="Create")
createBtn.pack()

copyBtn = tk.Button(command=copyPassword, text="Copy")
copyBtn.pack()

printClipboardBtn = tk.Button(command=printClipboard, text="Print")
printClipboardBtn.pack()

app.mainloop()