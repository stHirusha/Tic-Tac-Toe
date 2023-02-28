from tkinter import *
from tkinter import messagebox
import random

def mitiplayer():
   
   is_clicked = True
   count = 0
   winar = False
   
   def is_win():
      nonlocal winar
      winning_combinations = [(b1, b2, b3), (b4, b5, b6), (b7, b8, b9), (b1, b4, b7), (b2, b5, b8), (b3, b6, b9), (b1, b5, b9), (b3, b5, b7)]

      for combo in winning_combinations:
         if combo[0]['text'] == combo[1]['text'] == combo[2]['text'] and combo[0]['text'] != '':
               winner = combo[0]['text']
               combo[0].config(bg="Red")
               combo[1].config(bg="Red")
               combo[2].config(bg="Red")
               messagebox.showinfo("Winner!", f"{winner} Wins!")
               disable_buttons()
               winar = True

   def draw():
      if winar == False and count == 9:
         messagebox.showinfo("Draw", "It's a Draw")
         disable_buttons()

   def disable_buttons():
      b1.config(state=DISABLED)
      b2.config(state=DISABLED)
      b3.config(state=DISABLED)
      b4.config(state=DISABLED)
      b5.config(state=DISABLED)
      b6.config(state=DISABLED)
      b7.config(state=DISABLED)
      b8.config(state=DISABLED)
      b9.config(state=DISABLED)

   def clicked(b):
      nonlocal is_clicked, count
      if b['text'] == '':
         if is_clicked == True:
               b.config(text ="X")
               is_clicked = False
               count += 1
         elif is_clicked == False:
               b.config(text ="O")
               is_clicked = True
               count += 1
         is_win()
         draw()
      else:
         messagebox.showerror("Invalid Move!", "This box is already occupied. Choose an empty box to make your move.")
 
   window1 = Toplevel()
   window1.title("MutiPlayer")
   
   b1 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b1))
   b2 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b2))
   b3 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b3))
   b4 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b4))
   b5 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b5))
   b6 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b6))
   b7 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b7))
   b8 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b8))
   b9 = Button(window1, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b9))
   b1.grid(column = 0, row = 0)
   b2.grid(column = 1, row = 0)
   b3.grid(column = 2, row = 0)
   b4.grid(column = 0, row = 1)
   b5.grid(column = 1, row = 1)
   b6.grid(column = 2, row = 1)
   b7.grid(column = 0, row = 2)
   b8.grid(column = 1, row = 2)
   b9.grid(column = 2, row = 2)
   



def singleplayer():
   is_clicked = True
   winner = False
   def clicked(b):
      nonlocal is_clicked
      if b['text'] == '':
         if is_clicked == True:
               b.config(text ="X")
               is_clicked = False
               available_spaces.remove(b)
               is_win()
               draw()
               com()
               

   def com():
      nonlocal is_clicked
      nonlocal available_spaces
      if is_clicked == False and winner == False:
         if len(available_spaces) > 0 :
            computer_choice = random.choice(available_spaces)
            available_spaces.remove(computer_choice)
            computer_choice.config(text = "O")
            is_clicked = True
            is_win()
            draw()

   def is_win():
      winning_combinations = [(b1, b2, b3), (b4, b5, b6), (b7, b8, b9), (b1, b4, b7), (b2, b5, b8), (b3, b6, b9), (b1, b5, b9), (b3, b5, b7)]

      for combo in winning_combinations:
         if combo[0]['text'] == combo[1]['text'] == combo[2]['text'] and combo[0]['text'] != '':
               winner = combo[0]['text']
               combo[0].config(bg="Red")
               combo[1].config(bg="Red")
               combo[2].config(bg="Red")
               messagebox.showinfo("Winner!", f"{winner} Wins!")
               disable_buttons()
               winner = True
   
   def draw():
      if len(available_spaces) == 0 and winner == False:
         messagebox.showinfo("Draw","It's a Draw")
         disable_buttons()         

   def disable_buttons():
      b1.config(state=DISABLED)
      b2.config(state=DISABLED)
      b3.config(state=DISABLED)
      b4.config(state=DISABLED)
      b5.config(state=DISABLED)
      b6.config(state=DISABLED)
      b7.config(state=DISABLED)
      b8.config(state=DISABLED)
      b9.config(state=DISABLED)           
               
   
   window2 = Toplevel()
   window2.title("SinglePlayer")
   
   b1 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b1))
   b2 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b2))
   b3 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b3))
   b4 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b4))
   b5 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b5))
   b6 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b6))
   b7 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b7))
   b8 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b8))
   b9 = Button(window2, text='', font=('Arial', 20), bg='white', height=6, width=10, command=lambda: clicked(b9))
   b1.grid(column = 0, row = 0)
   b2.grid(column = 1, row = 0)
   b3.grid(column = 2, row = 0)
   b4.grid(column = 0, row = 1)
   b5.grid(column = 1, row = 1)
   b6.grid(column = 2, row = 1)
   b7.grid(column = 0, row = 2)
   b8.grid(column = 1, row = 2)
   b9.grid(column = 2, row = 2)

   available_spaces = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
   
root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")

label = Label(root,text="Tic Tac Toe",font=("Arial",50))
label.pack(pady=10)

btn1 = Button(root, text = "Multiplayer", font=("Arial",20),command=mitiplayer)
btn1.pack()

btn2 = Button(root, text = "Singleplayer", font=("Arial",20),command=singleplayer)
btn2.pack()


root.mainloop()
