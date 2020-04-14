#Abiodun Scott
#Write a program that will create a GUI that prompts a user to click
#a button that delivers a popup asking if the user wants to proceed.
#The popup should proceed to deliver updated information about
#the user's choice.

from tkinter import *
import tkinter.messagebox as box

#the first step after imports is create a window
window = Tk()

#this shows up at the top of the frame
window.title('Message Box Example')

def dialog():
    #give the user the opportunity to choose 'Yes' or 'No'
    var = box.askyesno('Message Box', "Proceed?")
    if var == 1:
        #pop up box if user chooses 'Yes' - name of box and text in box
        box.showinfo('Yes Box', 'Proceeding...')
    else:
        #pop up box if user chooses 'No' - name of box and text in box
        #warning symbol occurs
        box.showwarning('No Box', 'Cancelling...')

#create a button lablled 'Click'
btn = Button(window, text='Click', command=dialog)

#pack the space around the button
btn.pack(padx=150, pady=50)

#start the action and keep it going
window.mainloop()

