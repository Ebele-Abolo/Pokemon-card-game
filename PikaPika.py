# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 08:23:10 2021

@author: joyab
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 07:56:04 2021

@author: joyab
"""

from tkinter import*
from PIL import ImageTk, Image
root=Tk()

root.title("Endless Pokemon Card Game")
root.geometry("600x400")

root.configure(background="orange")

img = ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1  = Label(root, text = "Player 1", bg = "red", fg = "White")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "White")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player1_Score_Label = Label(root, bg = "royal blue", fg = "White")
player1_Score_Label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player2_Score_Label = Label(root, bg = "royal blue", fg = "White")
player2_Score_Label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_Label = Label(root, bg = "white", fg = "White")
random_dice_Label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()

