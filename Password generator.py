from tkinter import *
import pyperclip
import random
root = Tk()
root.geometry("1000x500")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)
def generate(): # Function to generate the password
	pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
			'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
			'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
			'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
			'9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
			'*', '(', ')']
	password = ""
	for x in range(passlen.get()):
		password = password + random.choice(pass1)
	passwrd.set(password)
def copyclipboard():
	random_password = passwrd.get()
	pyperclip.copy(random_password)
Label(root, text="Password Generator", font="Arial 30 bold").pack()
Label(root, text="Enter the number to get password", font="Arial 15 bold").pack(pady=3)
Entry(root, textvariable=passlen,width=30, font="Arial 10 bold").pack(pady=10)
Button(root, text="Tap to get", font="Arial 15 bold", command=generate).pack(pady=3)
Entry(root, textvariable=passwrd, width=30, font="Arial 10 bold").pack(pady=10)
Button(root, text="Tap to copy clipboard", font="Arial 15 bold", command=copyclipboard).pack()
root.mainloop()
