# Python Program to create Active Directory User(s)

from tkinter import *
import subprocess
import sys
from PIL import Image, ImageTk

root = Tk()

ShellPath = r'venv\Assets\CreateUser.ps1'

# initialize values to pull
first = StringVar()
last = StringVar()
selection = StringVar(root)
selection.set("Select Location") # Default Value

backgroundcolor = "#395B64"
wordsColor = "#2C3333"
textColor = "#E7F6F2"


# functions
def submit_clicked(*args):
    # Grabs Variables
    firstName = first.get()
    lastName = last.get()
    theLocation = selection.get()

    displayName = firstName + " " + lastName
    accountName = firstName[0].lower() + lastName.lower()
    emailAddress = accountName + "@larsonco.com"
    password = firstName[0].upper() + lastName[0].upper() + "welcome1!"
    empLocation = theLocation
    UPN = emailAddress

    # powershell

    p = subprocess.Popen(
        ["powershell.exe", ShellPath, "-File", firstName, lastName, accountName, UPN, password,
         emailAddress, empLocation], stdout=sys.stdout)
    p.communicate()

    first.set("")
    last.set("")
    selection.set("Select Location")


# Window Design
root.title("Create AD User")
root.geometry("450x600")
root.resizable(0, 0)
root.configure(
    bg=backgroundcolor
)

# this will create the widgets
img = Image.open(r"venv\Assets\Owl_logo.png")
pimg = ImageTk.PhotoImage(img)

header = Label(image=pimg)
header.image = pimg
header.grid(row=0, column=1, sticky=W, pady=25)
header.configure(
    width=250,
    bg=backgroundcolor,
)


fName = Label(
    root,
    text="First Name",
    font="Ariel 14 bold",
    padx=5,
    bg=backgroundcolor,
    fg=wordsColor,
)

lName = Label(
    root,
    text="Last Name",
    font="Ariel 14 bold",
    padx=5,
    bg=backgroundcolor,
    fg=wordsColor,

    )

location = OptionMenu(
    root,
    selection,
    "Clarkston",
    "Cambridge",
    "Fort Lauderdale",
    "FortWayne",
    "Gaylord",
    "GrandRapids",
    "Indianapolis",
    "Wildco",
    "Youngstown",
    "Executive"
)
location.configure(
    borderwidth=0,
    font="Ariel 14 bold",
    bg=backgroundcolor,
    fg=wordsColor,

)

submitBtn = Button(
    root,
    command=submit_clicked,
    text="Add User",
    fg=textColor,
    activeforeground=wordsColor,
    activebackground=textColor,
    width=10,
    height=1,
    borderwidth=5,
    font="Ariel 14",
    bg=wordsColor,
)

# grid method to arrange labels in respective
# rows and columns as specified
fName.grid(row=1, column=0, sticky=W, pady=20)
lName.grid(row=2, column=0, sticky=W, pady=20)
location.grid(row=3, column=0, sticky=W, pady=20)

submitBtn.grid(row=5, column=1, sticky=W, pady=50, padx=50)

# entry widgets, used to take entry from user
fNameInput = Entry(
    root,
    font="Ariel 14",
    textvariable=first,
    borderwidth=1,
    width=20,
    bg=backgroundcolor,
    fg=textColor,
)
lNameInput = Entry(
    root,
    font="Ariel 14",
    textvariable=last,
    borderwidth=1,
    width=20,
    bg = backgroundcolor,
    fg = textColor,
)

# this will arrange entry widgets
fNameInput.grid(row=1, column=1, pady=20)
lNameInput.grid(row=2, column=1, pady=20)

root.mainloop()  # end window
