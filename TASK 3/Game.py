from tkinter import *
from random import randint
import customtkinter as ct
from PIL import Image

ct.set_appearance_mode('dark')
ct.set_default_color_theme('Harlequin.json')

root = ct.CTk()
root.title('Rock Paper Scissors')
root.geometry('700x600')

rock = ct.CTkImage(dark_image=Image.open('Rock.png'),size=(300,300))
paper= ct.CTkImage(dark_image=Image.open('Hand.png'),size=(300,300))
scissor= ct.CTkImage(dark_image=Image.open('scissor.png'),size=(300,300))

image_list = [rock,paper,scissor]

#pick
pick_num =randint(0,2)

image_label = ct.CTkLabel(root,text="",image=image_list[pick_num],bg_color="transparent",fg_color='transparent')
image_label.pack(pady=20)

#functionality
def Spin():
    #picks a random no. 
    pick_num = randint(0,2)
    
    # show a image
    image_label.configure(image=image_list[pick_num])

    # 0 = rock
    # 1 = paper
    # 2 = scissor
# converting the choice value
    if choice.get()=='rock':
        choice_value = 0
    elif choice.get()=='paper':
        choice_value = 1
    elif choice.get()=='scissor':
        choice_value = 2
  #determing the winner 
    match choice_value:
        case 0:         #rock
            if pick_num == 0:
                win_lose_label.configure(text="Its a Tie")
    
            elif pick_num == 1:   
                win_lose_label.configure(text="Paper Wins against rock You Lose")
            
            elif pick_num == 2:
                win_lose_label.configure(text="rock Wins against scissor You Win")
    
        case 1:         #paper
            if pick_num == 0:
                win_lose_label.configure(text="Paper Wins against rock You Win")
    
            elif pick_num == 1:   
                win_lose_label.configure(text="Its a Tie")
    
            elif pick_num == 2:
                win_lose_label.configure(text="Paper Lose against scissor You Lose")
            

        case 2:         #scissor
            if pick_num == 0:
                win_lose_label.configure(text="scissor lose against rock You Lose")
            
            elif pick_num == 1:   
                win_lose_label.configure(text="scissor wins against paper You Win")
    
            elif pick_num == 2:
                win_lose_label.configure(text="Its a Tie") 
    

choice = ct.CTkComboBox(root,values=('rock','paper','scissor')) 
choice.pack(pady=10)   

spin_btn = ct.CTkButton(root,text="spin",command=Spin)
spin_btn.pack(pady=10)

win_lose_label = ct.CTkLabel(root,text="")
win_lose_label.pack(pady=10)



root.mainloop()