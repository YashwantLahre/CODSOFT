from tkinter import *
import customtkinter as ct
from tkinter import messagebox

ct.set_appearance_mode('dark')
ct.set_default_color_theme('TrojanBlue.json')

Window = ct.CTk()
Window.title('Calculator')
Window.geometry('300x300')
Window.config(bg='#111')

font_1 = ('Helvetica', 20, 'bold')

def button_Entry(num):
    result_entry.insert(END,num)

def clear():
    result_entry.delete(0,END)
def calculate():
        try:
            result = result_entry.get()
            new_result = result.replace('x','*')
            result1 = eval(new_result)
            clear()
            result_entry.insert(0,result1)
        except ZeroDivisionError:
            messagebox.showerror('Errot','Can not divide by zero')   
        except:
            messagebox.showerror('Error','enter valid values and arguments')    

result_entry = ct.CTkEntry(Window,font = font_1,text_color="#fff", fg_color='black',placeholder_text_color='white',width=280,height=50)
result_entry.place(x=10,y=10)

btn1 = ct.CTkButton(Window, text='7',command=lambda:button_Entry('7'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn1.place(x=10,y=80)

btn2 = ct.CTkButton(Window, text='8',command=lambda:button_Entry('8'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn2.place(x=80,y=80)

btn3 = ct.CTkButton(Window, text='9',command=lambda:button_Entry('9'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn3.place(x=150,y=80)

btn4 = ct.CTkButton(Window, text='4',command=lambda:button_Entry('4'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn4.place(x=10,y=125)

btn5 = ct.CTkButton(Window, text='5',command=lambda:button_Entry('5'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn5.place(x=80,y=125)

btn6 = ct.CTkButton(Window, text='6',command=lambda:button_Entry('6'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn6.place(x=150,y=125)

btn7 = ct.CTkButton(Window, text='1',command=lambda:button_Entry('1'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn7.place(x=10,y=170)

btn8 = ct.CTkButton(Window, text='2',command=lambda:button_Entry('2'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn8.place(x=80,y=170)

btn9 = ct.CTkButton(Window, text='3',command=lambda:button_Entry('3'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn9.place(x=150,y=170)

btn10 = ct.CTkButton(Window, text='0',command=lambda:button_Entry('0'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn10.place(x=10,y=215)

btn11 = ct.CTkButton(Window, text='.',command=lambda:button_Entry('.'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn11.place(x=80,y=215)

btn12 = ct.CTkButton(Window, text='C',command=clear,border_width=2,width=60,cursor='hand2',corner_radius=2)
btn12.place(x=150,y=215)

btn13 = ct.CTkButton(Window, text='=',command=calculate,border_width=2,width=280,cursor='hand2',corner_radius=2)
btn13.place(x=10,y=255)

btn14 = ct.CTkButton(Window, text='+',command=lambda:button_Entry('+'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn14.place(x=220,y=80)

btn15 = ct.CTkButton(Window, text='-',command=lambda:button_Entry('-'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn15.place(x=220,y=125)

btn16 = ct.CTkButton(Window, text='x',command=lambda:button_Entry('x'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn16.place(x=220,y=170)

btn17= ct.CTkButton(Window, text='/',command=lambda:button_Entry('/'),border_width=2,width=60,cursor='hand2',corner_radius=2)
btn17.place(x=220,y=215)


Window.mainloop()