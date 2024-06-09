import string
import random
from tkinter import *
import customtkinter as ct
from tkinter import messagebox


ct.set_appearance_mode("dark")
ct.set_default_color_theme("Cobalt.json")

root = ct.CTk()

root.title("Password generator")
root.geometry("350x350")

def submit():
    try:
        if __name__=="__main__":
             s1 = string.ascii_lowercase

             s2 = string.ascii_uppercase

             s3= string.digits

             s4 = string.punctuation

             s = []
             s.extend(list(s1))
             s.extend(list(s2))
             s.extend(list(s3))
             s.extend(list(s4))

             random.shuffle(s)
             k = "your password:" + "".join(s[0:int(Pass_len.get())])

             my_label.configure(text=k,text_color="#00CED1")
             print(k)
    except:
        messagebox.showerror('Error','Enter a valid input')
        


#Entry Field For the input length of the password
Pass_len = ct.CTkEntry(root,placeholder_text="Enter the length of password")
Pass_len.pack(pady=40)    

#Generate button for Generating the password
generate = ct.CTkButton(root,text="Generate", command=submit)  
generate.pack() 

my_label = ct.CTkLabel(root,text="")
my_label.pack(pady=10)

root.mainloop()
